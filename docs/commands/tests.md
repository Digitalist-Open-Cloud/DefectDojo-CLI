# Tests

Manage tests in DefectDojo.

## Subcommands

- `list` - List tests
- `get` - Get a specific test
- `list-findings` - List findings for a test

## `list`

List tests.

### Usage

```shell
defectdojo tests list [OPTIONS]
```

### Options

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--engagement_id ENGAGEMENT_ID` | Filter by engagement ID |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo tests list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY

defectdojo tests list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --engagement_id 1
```

## `get`

Get a specific test.

### Usage

```shell
defectdojo tests get [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--test_id TEST_ID` | Test ID |

### Examples

```shell
defectdojo tests get \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --test_id 1
```

## `list-findings`

List findings for a test.

### Usage

```shell
defectdojo tests list-findings [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--test_id TEST_ID` | Test ID |

### Examples

```shell
defectdojo tests list-findings \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --test_id 1
```
