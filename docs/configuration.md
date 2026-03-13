# Configuration

DefectDojo CLI supports configuration via environment variables or command-line arguments.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DEFECTDOJO_URL` | DefectDojo instance URL |
| `DEFECTDOJO_API_KEY` | API v2 Key for authentication |

## Command-line Arguments

All commands accept the following arguments:

| Argument | Description |
|----------|-------------|
| `--url` | DefectDojo URL |
| `--api_key` | API v2 Key |

## Examples

### Using environment variables

```shell
export DEFECTDOJO_URL=https://defectdojo.example.com
export DEFECTDOJO_API_KEY=your_api_key_here

defectdojo products list
```

### Using command-line arguments

```shell
defectdojo products list \
  --url https://defectdojo.example.com \
  --api_key your_api_key_here
```

## Getting an API Key

1. Log in to DefectDojo
2. Go to API v2 (in the dropdown under your username)
3. Click "Generate Token"
4. Use the generated token as your `api_key`
