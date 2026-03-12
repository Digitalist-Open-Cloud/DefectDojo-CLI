# Announcements

Manage announcements in DefectDojo.

## Subcommands

- `list` - List announcements
- `create` - Create an announcement
- `update` - Update an announcement
- `delete` - Delete an announcement

## `list`

List announcements.

### Usage

```shell
defectdojo announcements list [OPTIONS]
```

### Options

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo announcements list \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY
```

## `create`

Create an announcement.

### Usage

```shell
defectdojo announcements create [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--message MESSAGE` | Announcement message |
| `--title TITLE` | Announcement title |

### Options

| Argument | Description |
|----------|-------------|
| `--type {info,success,warning,danger}` | Announcement type |
| `--active` | Make announcement active |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo announcements create \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --title "System Maintenance" \
  --message "System will be down for maintenance on Sunday" \
  --type warning
```

## `update`

Update an announcement.

### Usage

```shell
defectdojo announcements update [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--announcement_id ANNOUNCEMENT_ID` | Announcement ID |

### Options

| Argument | Description |
|----------|-------------|
| `--message MESSAGE` | New message |
| `--title TITLE` | New title |
| `--type {info,success,warning,danger}` | New type |
| `--active` | Set active status |
| `--json` | Output as JSON |

### Examples

```shell
defectdojo announcements update \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --announcement_id 1 \
  --message "Maintenance completed"
```

## `delete`

Delete an announcement.

### Usage

```shell
defectdojo announcements delete [OPTIONS]
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--url URL` | DefectDojo URL |
| `--api_key API_KEY` | API v2 Key |
| `--announcement_id ANNOUNCEMENT_ID` | Announcement ID |

### Examples

```shell
defectdojo announcements delete \
  --url https://defectdojo.example.com \
  --api_key YOUR_API_KEY \
  --announcement_id 1
```
