from datetime import datetime
import json
import sys
import argparse
from tabulate import tabulate
from rich_argparse import RichHelpFormatter
from defectdojo_cli2.util import Util
from defectdojo_cli2.EnvDefaults import EnvDefaults

class Products(object):
    def parse_cli_args(self):
        parser = argparse.ArgumentParser(
            description="Perform <sub_command> related to products in DefectDojo",
            usage="""defectdojo project <sub_command> [<args>]

    You can use the following sub_commands:
        create                  Create product
        create-if-not-exists    Create product only if it does not already exist
""",
            formatter_class=RichHelpFormatter,
        )
        parser.add_argument("sub_command", help="Sub_command to run")
        # Get sub_command
        args = parser.parse_args(sys.argv[2:3])
        if not hasattr(self, "_" + args.sub_command):
            print("Unrecognized sub_command " + args.sub_command)
            parser.print_help()
            sys.exit(1)
        # Use dispatch pattern to invoke method with same name (that starts with _)
        getattr(self, "_" + args.sub_command)()

    def create(self, url, api_key, name, description, prod_type, tags="", **kwargs):
        api_url = url.rstrip("/") + "/api/v2/products/"

        payload = {
            "name": name,
            "prod_type": prod_type,
            "description": description,
            "tags": [t.strip() for t in tags.split(",") if t.strip()],
        }

        payload_json = json.dumps(payload)

        response = Util().request_apiv2(
            "POST",
            api_url,
            api_key,
            data=payload_json,
        )

        return response
    def get_by_name(self, url, api_key, name):
        api_url = url.rstrip("/") + "/api/v2/products/?name_exact=" + name.replace(" ", "%20")
        response = Util().request_apiv2("GET", api_url, api_key)
        return response

    def create_if_not_exists(self, url, api_key, name, description, prod_type, tags="", **kwargs):

        r = self.get_by_name(url, api_key, name)
        data = json.loads(r.text)

        if data.get("count", 0) > 0:
            return {"exists": True, "message": f"Product '{name}' exists", "id": data["results"][0]["id"]}

        # If not found → create
        create_response = self.create(
            url=url,
            api_key=api_key,
            name=name,
            description=description,
            prod_type=prod_type,
            tags=tags,
        )

        return {"exists": False, "created": True, "response": json.loads(create_response.text)}

    def _create(self):
        parser = argparse.ArgumentParser(
            description="Create product",
            usage="defectdojo project create [<args>]",
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
            "--name",
            action=EnvDefaults,
            help="Name of the product to create",
            envvar="DEFECTDOJO_PRODUCT_NAME",
            required=True,
        )
        required.add_argument(
            "--description",
            action=EnvDefaults,
            help="Description of the product",
            envvar="DEFECTDOJO_PRODUCT_DESCRIPTION",
            required=True,
        )
        required.add_argument(
            "--prod_type",
            action=EnvDefaults,
            help="Product type",
            envvar="DEFECTDOJO_PRODUCT_TYPE",
            required=True,
        )
        optional.add_argument(
            "--tags",
            action=EnvDefaults,
            help="Comma-separated list of product tags",
            envvar="DEFECTDOJO_PRODUCT_TAGS",
            default="",
        )
        optional.add_argument(
            "--json",
            help="Print output in JSON format",
            action="store_true",
            default=False,
        )

        parser._action_groups.append(optional)
        args = vars(parser.parse_args(sys.argv[3:]))

        response = self.create(
            url=args["url"],
            api_key=args["api_key"],
            name=args["name"],
            description=args["description"],
            prod_type=args["prod_type"],
            tags=args["tags"],
        )

        json_out = json.loads(response.text)

        if args["json"]:
            print(json.dumps(json_out, indent=4))
        else:
            print(json_out)

    def _create_if_not_exists(self):
        parser = argparse.ArgumentParser(
            description="Create product if it does not already exist",
            usage="defectdojo project create-if-not-exists [<args>]",
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
            "--name",
            action=EnvDefaults,
            help="Name of the product to create",
            envvar="DEFECTDOJO_PRODUCT_NAME",
            required=True,
        )
        required.add_argument(
            "--description",
            action=EnvDefaults,
            help="Description of the product",
            envvar="DEFECTDOJO_PRODUCT_DESCRIPTION",
            required=True,
        )
        required.add_argument(
            "--prod_type",
            action=EnvDefaults,
            help="Product type",
            envvar="DEFECTDOJO_PRODUCT_TYPE",
            required=True,
        )
        optional.add_argument(
            "--tags",
            action=EnvDefaults,
            help="Comma-separated list of product tags",
            envvar="DEFECTDOJO_PRODUCT_TAGS",
            default="",
        )
        optional.add_argument(
            "--json",
            help="Output in JSON format",
            action="store_true",
            default=False,
        )
        parser._action_groups.append(optional)

        args = vars(parser.parse_args(sys.argv[3:]))

        result = self.create_if_not_exists(
            url=args["url"],
            api_key=args["api_key"],
            name=args["name"],
            description=args["description"],
            prod_type=args["prod_type"],
            tags=args["tags"],
        )

        if args["json"]:
            print(json.dumps(result, indent=4))
        else:
            # Plain output
            if result.get("exists"):
                print(f"Product '{args['name']}' exists")
            else:
                print("Product created:")
                print(result["response"])