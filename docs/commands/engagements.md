# Engagements

Manage engagements in DefectDojo.

## Subcommands

- `list` - List engagements
- `get` - Get a specific engagement
- `create` - Create a new engagement
- `close` - Close an engagement
- `list-notes` - List notes for an engagement

## list

List engagements.

### Usage

```shell
defectdojo engagements list [OPTIONS]
```

### Options

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--product_id PRODUCT_ID` | Filter by product ID |
| `--status STATUS` | Filter by status |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo engagements list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY

defectdojo engagements list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1
```

## get

Get a specific engagement.

### Usage

```shell
defectdojo engagements get [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--engagement_id ENGAGEMENT_ID` | Engagement ID |

### Examples

```shell
defectdojo engagements get \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --engagement_id 1
```

## create

Create a new engagement.

### Usage

```shell
defectdojo engagements create [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--product_id PRODUCT_ID` | Product ID |
| `--name NAME` | Engagement name |

### Options

| Argument | Description |
|----------|-------------|
| `--description DESCRIPTION` | Engagement description |
| `--target_start TARGET_START` | Target start date (YYYY-MM-DD) |
| `--target_end TARGET_END` | Target end date (YYYY-MM-DD) |
| `--status STATUS` | Engagement status |
| `--engagement_type {Interactive,CI/CD}` | Engagement type |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo engagements create \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --name "Q1 Security Review" \
  --target_start 2026-01-01 \
  --target_end 2026-03-31
```

## close

Close an engagement.

### Usage

```shell
defectdojo engagements close [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--engagement_id ENGAGEMENT_ID` | Engagement ID |

### Options

| Argument | Description |
|----------|-------------|
| `--json` | Output as JSON |

### Examples

```shell
defectdojo engagements close \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --engagement_id 1
```

## list-notes

List notes for an engagement.

### Usage

```shell
defectdojo engagements list-notes [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--engagement_id ENGAGEMENT_ID` | Engagement ID |

### Examples

```shell
defectdojo engagements list-notes \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --engagement_id 1
```
