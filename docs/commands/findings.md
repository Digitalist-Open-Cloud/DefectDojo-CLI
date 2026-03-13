# Findings

Manage findings in DefectDojo.

## Subcommands

- `list` - List findings
- `get` - Get a specific finding
- `modify` - Modify a finding
- `accept-risk` - Accept risk for a finding
- `delete` - Delete a finding

## `list`

List findings.

### Usage

```shell
defectdojo findings list [OPTIONS]
```

### Options

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--product_id PRODUCT_ID` | Filter by product ID |
| `--engagement_id ENGAGEMENT_ID` | Filter by engagement ID |
| `--test_id TEST_ID` | Filter by test ID |
| `--severity {Critical,High,Medium,Low,Info}` | Filter by severity |
| `--active` | Filter active findings |
| `--verified` | Filter verified findings |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo findings list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY

defectdojo findings list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --severity High
```

## `get`

Get a specific finding by ID.

### Usage

```shell
defectdojo findings get [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--finding_id FINDING_ID` | Finding ID |

### Examples

```shell
defectdojo findings get \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --finding_id 123
```

## `modify`

Modify a finding.

### Usage

```shell
defectdojo findings modify [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--finding_id FINDING_ID` | Finding ID |

### Options

| Argument | Description |
|----------|-------------|
| `--severity {Critical,High,Medium,Low,Info}` | New severity |
| `--active {true,false}` | Active status |
| `--verified {true,false}` | Verified status |
| `--false_p {true,false}` | False positive status |
| `--duplicate {true,false}` | Duplicate status |
| `--risk_accepted {true,false}` | Risk accepted status |
| `--mitigation MITIGATION` | Mitigation text |
| `--impact IMPACT` | Impact text |
| `--description DESCRIPTION` | Description text |
| `--title TITLE` | Title |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo findings modify \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --finding_id 123 \
  --severity High \
  --mitigation "Applied fix XYZ"
```

## `accept-risk`

Accept risk for a finding.

### Usage

```shell
defectdojo findings accept-risk [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--finding_id FINDING_ID` | Finding ID |

### Options

| Argument | Description |
|----------|-------------|
| `-- expiration_date EXPIRATION_DATE` | Risk acceptance expiration date (YYYY-MM-DD) |
| `--owner OWNER` | Owner of risk acceptance |
| `--notes NOTES` | Notes |

### Examples

```shell
defectdojo findings accept-risk \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --finding_id 123 \
  --expiration_date 2026-12-31 \
  --owner "Security Team"
```

## `delete`

Delete a finding.

### Usage

```shell
defectdojo findings delete [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--finding_id FINDING_ID` | Finding ID |

### Examples

```shell
defectdojo findings delete \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --finding_id 123
```
