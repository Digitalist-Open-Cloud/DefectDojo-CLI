# API Token

Manage API token authentication for DefectDojo.

## Subcommands

- `api-token-auth` - Get API token details

## api-token-auth

Get information about the API token.

### Usage

```shell
defectdojo api_token api-token-auth [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |

### Options

| Argument | Description |
|----------|-------------|
| `--json` | Output as JSON |

### Examples

```shell
defectdojo api_token api-token-auth \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY

defectdojo api_token api-token-auth \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --json
```
