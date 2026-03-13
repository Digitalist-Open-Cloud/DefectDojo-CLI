# Import Languages

Import language information into DefectDojo.

## Subcommands

- `create` - Import languages from a CSV file

## `create`

Import languages from a CSV file.

### Usage

```shell
defectdojo import_languages create [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--file_name FILE_NAME` | Path to CSV file |

### Options

| Argument | Description |
|----------|-------------|
| `--product_id PRODUCT_ID` | Associate with a product |
| `--engagement_id ENGAGEMENT_ID` | Associate with an engagement |
| `--json` | Output as JSON |

### CSV Format

The CSV file should contain the following columns:

- `name` - Language name (e.g., "Python")
- `files` - Number of files
- `blank` - Blank lines
- `comment` - Comment lines
- `code` - Lines of code

### Examples

```shell
defectdojo import_languages create \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --file_name languages.csv

defectdojo import_languages create \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --file_name languages.csv \
  --product_id 1
```
