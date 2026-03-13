import json
import sys
import argparse
import os
import re
from jinja2 import Environment, FileSystemLoader
import markdown
from rich_argparse import RichHelpFormatter
from defectdojo_cli2.util import Util
from defectdojo_cli2.EnvDefaults import EnvDefaults


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def _convert_bare_urls_to_markdown(text):
    url_pattern = re.compile(r'(?<!\[)(?<!\])(https?://[^\s\)"\'<>]+)')
    return url_pattern.sub(r'[\1](\1)', text)


def _markdown_convert(text):
    text = _convert_bare_urls_to_markdown(text)
    html = markdown.markdown(
        text,
        extensions=['nl2br', 'tables', 'fenced_code']
    )
    html = html.replace('<h1>', '<h4>').replace('</h1>', '</h4>')
    html = html.replace('<h2>', '<h4>').replace('</h2>', '</h4>')
    html = html.replace('<h3>', '<h4>').replace('</h3>', '</h4>')
    return html


def _render_html_from_json(json_data, active_only=False, template_path=None):
    findings = json_data.get("findings", [])
    if active_only:
        findings = [f for f in findings if f.get("active", False)]

    for finding in findings:
        if finding.get("description"):
            finding["description_html"] = _markdown_convert(finding["description"])
        if finding.get("mitigation"):
            finding["mitigation_html"] = _markdown_convert(finding["mitigation"])
        if finding.get("impact"):
            finding["impact_html"] = _markdown_convert(finding["impact"])
        if finding.get("steps_to_reproduce"):
            finding["steps_to_reproduce_html"] = _markdown_convert(finding["steps_to_reproduce"])
        if finding.get("references"):
            finding["references_html"] = _markdown_convert(finding["references"])
        if finding.get("file_path"):
            finding["file_path_html"] = finding["file_path"]
        if finding.get("line"):
            finding["line_html"] = finding["line"]
        
        req_resp = finding.get("request_response", {})
        req_list = req_resp.get("req_resp", [])
        if req_list:
            req_resp_md = ""
            for idx, item in enumerate(req_list):
                if idx > 0:
                    req_resp_md += "\n\n---\n\n"
                req_resp_md += "**Request:**\n```\n" + item.get("request", "") + "\n```\n\n**Response:**\n```\n" + item.get("response", "") + "\n```"
            finding["request_response_html"] = _markdown_convert(req_resp_md)

    severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
    for finding in findings:
        sev = finding.get("severity", "Info")
        sev_lower = sev.lower()
        if sev_lower in severity_counts:
            severity_counts[sev_lower] += 1

    if template_path:
        if os.path.isfile(template_path):
            custom_env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
            template = custom_env.get_template(os.path.basename(template_path))
        else:
            raise FileNotFoundError(f"Template file not found: {template_path}")
    else:
        template = jinja_env.get_template("report.html")

    return template.render(
        report_name=json_data.get("report_name", "Security Report"),
        report_info=json_data.get("report_info", ""),
        product=json_data.get("product"),
        engagement=json_data.get("engagement"),
        findings=findings,
        severity_counts=severity_counts,
        team_name=json_data.get("team_name", "Security Team"),
    )


class Reports(object):
    def parse_cli_args(self):
        parser = argparse.ArgumentParser(
            description="Perform <sub_command> related to reports in DefectDojo",
            usage="""defectdojo reports <sub_command> [<args>]

    You can use the following sub_commands:
        generate-for-engagement    Generate a report for an engagement
        generate-for-product      Generate a report for a product
""",
            formatter_class=RichHelpFormatter,
        )
        parser.add_argument("sub_command", help="Sub_command to run")
        args = parser.parse_args(sys.argv[2:3])
        method_name = "_" + args.sub_command.replace("-", "_")
        if not hasattr(self, method_name):
            print("Unrecognized sub_command " + args.sub_command)
            parser.print_help()
            sys.exit(1)
        getattr(self, method_name)()

    def generate_for_engagement(
        self,
        url,
        api_key,
        engagement_id,
        report_type="HTML",
        include_executive_summary=False,
        include_finding_notes=False,
        include_finding_images=False,
        include_table_of_contents=False,
        title="",
        filename=None,
        **kwargs,
    ):
        api_url = url.rstrip("/") + f"/api/v2/engagements/{engagement_id}/generate_report/"

        payload = {
            "report_type": report_type,
            "include_executive_summary": include_executive_summary,
            "include_finding_notes": include_finding_notes,
            "include_finding_images": include_finding_images,
            "include_table_of_contents": include_table_of_contents,
        }

        if title:
            payload["title"] = title

        payload_json = json.dumps(payload)

        response = Util().request_apiv2(
            "POST",
            api_url,
            api_key,
            data=payload_json,
        )

        if filename and response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)

        return response

    def _generate_for_engagement(self):
        parser = argparse.ArgumentParser(
            description="Generate a report for an engagement",
            usage="defectdojo reports generate-for-engagement [<args>]",
            formatter_class=RichHelpFormatter,
        )

        optional = parser._action_groups.pop()
        required = parser.add_argument_group("required arguments")

        required.add_argument(
            "--url",
            action=EnvDefaults,
            envvar="DEFECTDOJO_URL",
            help="DefectDojo URL",
            required=True,
        )
        required.add_argument(
            "--api_key",
            action=EnvDefaults,
            envvar="DEFECTDOJO_API_KEY",
            help="API v2 Key",
            required=True,
        )
        required.add_argument(
            "--engagement_id",
            action=EnvDefaults,
            envvar="DEFECTDOJO_ENGAGEMENT_ID",
            help="Engagement ID",
            required=True,
        )

        optional.add_argument(
            "--report_type",
            help="Report type",
            choices=["HTML", "JSON"],
            default="HTML",
        )
        optional.add_argument(
            "--include_executive_summary",
            help="Include executive summary in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--include_finding_notes",
            help="Include finding notes in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--include_finding_images",
            help="Include finding images in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--include_table_of_contents",
            help="Include table of contents in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--title",
            help="Report title",
            default="",
        )
        optional.add_argument(
            "--active",
            help="Filter to active findings only (client-side)",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--filename",
            help="Save report to file (default: output to stdout for JSON/HTML)",
        )
        optional.add_argument(
            "--template",
            help="Custom HTML template file path (default: built-in template)",
        )

        parser._action_groups.append(optional)
        args = vars(parser.parse_args(sys.argv[3:]))

        response = self.generate_for_engagement(**args)

        if response.status_code == 200:
            active_only = args.get("active", False)
            template_path = args.get("template")

            if args.get("filename"):
                if args["report_type"] == "HTML":
                    json_data = json.loads(response.text)
                    if active_only:
                        json_data["findings"] = [f for f in json_data["findings"] if f.get("active", False)]
                    html_content = _render_html_from_json(json_data, active_only=active_only, template_path=template_path)
                    with open(args["filename"], "w") as f:
                        f.write(html_content)
                else:
                    with open(args["filename"], "wb") as f:
                        f.write(response.content)
                print(f"Report saved to {args['filename']}")
            elif args["report_type"] == "JSON":
                try:
                    json_out = json.loads(response.text)
                    if active_only:
                        json_out["findings"] = [f for f in json_out["findings"] if f.get("active", False)]
                    print(json.dumps(json_out, indent=4))
                except json.JSONDecodeError:
                    print(response.text)
            elif args["report_type"] == "HTML":
                json_data = json.loads(response.text)
                print(_render_html_from_json(json_data, active_only=active_only, template_path=template_path))
            else:
                print(response.text)
        else:
            print(response.text)
            exit(1)

    def generate_for_product(
        self,
        url,
        api_key,
        product_id,
        report_type="HTML",
        include_executive_summary=False,
        include_finding_notes=False,
        include_finding_images=False,
        include_table_of_contents=False,
        title="",
        filename=None,
        **kwargs,
    ):
        api_url = url.rstrip("/") + f"/api/v2/products/{product_id}/generate_report/"

        payload = {
            "report_type": report_type,
            "include_executive_summary": include_executive_summary,
            "include_finding_notes": include_finding_notes,
            "include_finding_images": include_finding_images,
            "include_table_of_contents": include_table_of_contents,
        }

        if title:
            payload["title"] = title

        payload_json = json.dumps(payload)

        response = Util().request_apiv2(
            "POST",
            api_url,
            api_key,
            data=payload_json,
        )

        if filename and response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)

        return response

    def _generate_for_product(self):
        parser = argparse.ArgumentParser(
            description="Generate a report for a product",
            usage="defectdojo reports generate-for-product [<args>]",
            formatter_class=RichHelpFormatter,
        )

        optional = parser._action_groups.pop()
        required = parser.add_argument_group("required arguments")

        required.add_argument(
            "--url",
            action=EnvDefaults,
            envvar="DEFECTDOJO_URL",
            help="DefectDojo URL",
            required=True,
        )
        required.add_argument(
            "--api_key",
            action=EnvDefaults,
            envvar="DEFECTDOJO_API_KEY",
            help="API v2 Key",
            required=True,
        )
        required.add_argument(
            "--product_id",
            action=EnvDefaults,
            envvar="DEFECTDOJO_PRODUCT_ID",
            help="Product ID",
            required=True,
        )

        optional.add_argument(
            "--report_type",
            help="Report type",
            choices=["HTML", "JSON"],
            default="HTML",
        )
        optional.add_argument(
            "--include_executive_summary",
            help="Include executive summary in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--include_finding_notes",
            help="Include finding notes in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--include_finding_images",
            help="Include finding images in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--include_table_of_contents",
            help="Include table of contents in report",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--title",
            help="Report title",
            default="",
        )
        optional.add_argument(
            "--active",
            help="Filter to active findings only (client-side)",
            action="store_true",
            default=False,
        )
        optional.add_argument(
            "--filename",
            help="Save report to file (default: output to stdout for JSON/HTML)",
        )
        optional.add_argument(
            "--template",
            help="Custom HTML template file path (default: built-in template)",
        )

        parser._action_groups.append(optional)
        args = vars(parser.parse_args(sys.argv[3:]))

        response = self.generate_for_product(**args)

        if response.status_code == 200:
            active_only = args.get("active", False)
            template_path = args.get("template")
            if args.get("filename"):
                if args["report_type"] == "HTML":
                    json_data = json.loads(response.text)
                    if active_only:
                        json_data["findings"] = [f for f in json_data["findings"] if f.get("active", False)]
                    html_content = _render_html_from_json(json_data, active_only=active_only, template_path=template_path)
                    with open(args["filename"], "w") as f:
                        f.write(html_content)
                else:
                    with open(args["filename"], "wb") as f:
                        f.write(response.content)
                print(f"Report saved to {args['filename']}")
            elif args["report_type"] == "JSON":
                try:
                    json_out = json.loads(response.text)
                    if active_only:
                        json_out["findings"] = [f for f in json_out["findings"] if f.get("active", False)]
                    print(json.dumps(json_out, indent=4))
                except json.JSONDecodeError:
                    print(response.text)
            elif args["report_type"] == "HTML":
                json_data = json.loads(response.text)
                print(_render_html_from_json(json_data, active_only=active_only, template_path=template_path))
            else:
                print(response.text)
        else:
            print(response.text)
            exit(1)
