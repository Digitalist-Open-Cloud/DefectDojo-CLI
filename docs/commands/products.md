# Products

Manage products in DefectDojo.

## Subcommands

- `list` - List all products
- `create` - Create a new product
- `create-if-not-exists` - Create a product only if it doesn't exist

## list

List all products.

### Usage

```shell
defectdojo products list [OPTIONS]
```

### Options

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--page_size PAGE_SIZE` | Number of results to return per page |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo products list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY

defectdojo products list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --json
```

## `create`

Create a new product.

### Usage

```shell
defectdojo products create [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--name NAME` | Name of the product |
| `--description DESCRIPTION` | Product description |
| `--prod_type PROD_TYPE` | Product type ID |

### Options

| Argument | Description |
|----------|-------------|
| `--tags TAGS` | Comma-separated list of product tags |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo products create \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --name "My Product" \
  --description "Product description" \
  --prod_type 1
```

## `create-if-not-exists`

Create a product only if it doesn't already exist.

### Usage

```shell
defectdojo products create-if-not-exists [OPTIONS]
```

Same arguments as `create`.
