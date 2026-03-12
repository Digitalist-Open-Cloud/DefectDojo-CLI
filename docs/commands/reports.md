# Reports

Generate reports for products and engagements.

## Subcommands

- `generate-for-product` - Generate a report for a product
- `generate-for-engagement` - Generate a report for an engagement

## generate-for-product

Generate a security report for a product.

### Usage

```shell
defectdojo reports generate-for-product [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--product_id PRODUCT_ID` | Product ID |

### Options

| Argument | Description | Default |
|----------|-------------|---------|
| `--report_type {HTML,PDF,JSON,CSV}` | Report type | HTML |
| `--include_executive_summary` | Include executive summary | False |
| `--include_finding_notes` | Include finding notes | False |
| `--include_finding_images` | Include finding images | False |
| `--include_table_of_contents` | Include table of contents | False |
| `--include_disclaimer` | Include disclaimer | False |
| `--title TITLE` | Report title | |
| `--active` | Filter to active findings only | False |
| `--verified {1,2,3}` | Include verified findings | |
| `--false_p {1,2,3}` | Include false positive findings | 2 |
| `--duplicate {1,2,3}` | Include duplicate findings | 2 |
| `--minimum_severity {Info,Low,Medium,High,Critical}` | Minimum severity | Info |
| `--filename FILENAME` | Save report to file | stdout |
| `--template TEMPLATE` | Custom HTML template file path | built-in template |

### Examples

```shell
# Generate HTML report to stdout
defectdojo reports generate-for-product \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --report_type HTML

# Generate JSON report and save to file
defectdojo reports generate-for-product \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --report_type JSON \
  --filename report.json

# Generate report with only active findings
defectdojo reports generate-for-product \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --active \
  --report_type HTML \
  --filename report.html

# Generate report with minimum severity High
defectdojo reports generate-for-product \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --minimum_severity High \
  --filename report.html

# Generate report with custom HTML template
defectdojo reports generate-for-product \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --template /path/to/custom_template.html \
  --filename report.html
```

## generate-for-engagement

Generate a security report for an engagement.

### Usage

```shell
defectdojo reports generate-for-engagement [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--engagement_id ENGAGEMENT_ID` | Engagement ID |

### Options

Same options as `generate-for-product`.

### Examples

```shell
# Generate HTML report for engagement
defectdojo reports generate-for-engagement \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --engagement_id 1 \
  --report_type HTML \
  --filename report.html

# Generate JSON report for engagement
defectdojo reports generate-for-engagement \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --engagement_id 1 \
  --report_type JSON
```

## Report Types

- **HTML** - Renders a modern HTML report with severity counts, product/engagement info, and findings list
- **JSON** - Raw JSON output from DefectDojo API
- **PDF** - PDF document (binary output)
- **CSV** - CSV spreadsheet

## Filtering Findings

The `--active` flag filters findings client-side to include only active findings. This is useful when you want to exclude mitigated or inactive findings from your report.

The `--minimum_severity` flag filters findings by severity level. Findings below the specified severity will be excluded.
