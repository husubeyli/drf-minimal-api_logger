# drf-minimal-api-logger

A lightweight, dependency-free, and beautifully formatted execution time logger middleware for Django and Django REST Framework.

## Features

- 🚀 **Zero Dependencies** — Works out-of-the-box with standard Django, no extra packages needed.
- 🎨 **Color-Coded Output** — Highlights HTTP statuses: Green for 2xx, Yellow for 4xx, Red for 5xx.
- ⏱️ **Performance Tracking** — Measures exact request-response lifecycle duration in milliseconds.

## Installation

```bash
pip install drf-minimal-api-logger
```

## Setup

Add `drf_minimal_api_logger` to your `INSTALLED_APPS` and the middleware to `MIDDLEWARE` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'drf_minimal_api_logger',
]

MIDDLEWARE = [
    ...
    'drf_minimal_api_logger.middleware.MinimalAPILoggerMiddleware',
]
```

## Example Output

```
[DRF-LOGGER] GET /api/users/ -> 200 (12.34ms)
[DRF-LOGGER] POST /api/login/ -> 400 (5.67ms)
[DRF-LOGGER] DELETE /api/item/1/ -> 500 (3.21ms)
```

Status codes are color-coded in the terminal:
- **Green** — 2xx Success
- **Yellow** — 4xx Client Error
- **Red** — 5xx Server Error

## Requirements

- Python >= 3.8
- Django >= 4.0

## License

MIT License. See [LICENSE](LICENSE) for details.
# drf-minimal-api_logger
