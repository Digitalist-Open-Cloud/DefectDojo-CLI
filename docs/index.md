# DefectDojo CLI

A CLI wrapper for DefectDojo using API v2.

## Overview

DefectDojo CLI provides a command-line interface to interact with DefectDojo, allowing you to manage products, engagements, findings, tests, and generate reports directly from the terminal.

## Features

- Manage products and engagements
- View and filter findings
- Import and reimport scan results
- Generate reports in multiple formats (HTML, JSON, PDF, CSV)
- Manage API tokens
- And more...

## Quick Start

```shell
# View help
defectdojo --help

# View version
defectdojo --version

# Generate a report
defectdojo reports generate-for-product \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --product_id 1 \
  --report_type HTML \
  --filename report.html
```

## Commands

- [announcements](commands/announcements.md) - Manage announcements
- [api_token](commands/api_token.md) - API token operations
- [engagements](commands/engagements.md) - Manage engagements
- [findings](commands/findings.md) - Manage findings
- [import_languages](commands/import_languages.md) - Import languages
- [products](commands/products.md) - Manage products
- [reports](commands/reports.md) - Generate reports
- [reimport_scan](commands/reimport_scan.md) - Reimport scan results
- [tests](commands/tests.md) - Manage tests
