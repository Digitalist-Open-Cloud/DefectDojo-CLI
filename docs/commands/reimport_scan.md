# Reimport Scan

Reimport scan results into DefectDojo.

## Subcommands

- `create` - Reimport a scan

## create

Reimport scan results from a file.

### Usage

```shell
defectdojo reimport_scan create [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--file_name FILE_NAME` | Path to scan file |
| `--scan_type SCAN_TYPE` | Scan type (e.g., "Nmap Scan", "ZAP Scan") |
| `--engagement_id ENGAGEMENT_ID` | Engagement ID |

### Options

| Argument | Description |
|----------|-------------|
| `--active` | Set findings as active |
| `--verified` | Set findings as verified |
| `--minimum_severity {Critical,High,Medium,Low,Info}` | Minimum severity |
| `--scan_date SCAN_DATE` | Date of scan (YYYY-MM-DD) |
| `--json` | Output as JSON |

### Scan Types

Common scan types include:
- Nmap Scan
- ZAP Scan
- OpenVAS Scan
- Qualys Scan
- Nessus Scan
- Burp Scan
- Acunetix Scan
- Checkmarx Scan
- SonarQube Scan

### Examples

```shell
defectdojo reimport_scan create \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --file_name scan_results.xml \
  --scan_type "Nmap Scan" \
  --engagement_id 1

defectdojo reimport_scan create \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --file_name zap_results.xml \
  --scan_type "ZAP Scan" \
  --engagement_id 1 \
  --active \
  --verified
```
