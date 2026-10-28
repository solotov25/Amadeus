# Avianca Round-Trip Tests (Playwright + Python)

Automated UI tests for the round-trip booking flow on https://www.avianca.com/en.

## Requirements

- Python 3.9 or newer
- Google Chrome (the tests run in real Chrome, not the bundled Chromium)
- A normal home or office internet connection (see "Troubleshooting")

## Installation

1. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv .venv

   # macOS / Linux
   source .venv/bin/activate

   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   ```

2. **Install the dependencies:**

   ```bash
   pip install pytest pytest-playwright
   ```

3. **Install Chrome for Playwright:**

   ```bash
   playwright install chrome
   ```

   This is required. The site's bot protection (Akamai) returns an "Access Denied" page to the bundled headless Chromium, so the tests use the `chrome` channel in headed mode. If Chrome is already installed on your machine, Playwright will use it, and the command above makes sure it is available.

## Configuration

Create a `conftest.py` in the project root so the tests launch real Chrome with a fixed locale:

```python
import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "channel": "chrome",   # real Chrome instead of bundled Chromium
        "headless": False,     # headless is blocked by the site
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "locale": "en-US",     # keeps date format and labels stable
        "viewport": {"width": 1366, "height": 768},
    }
```

## Project structure

```
.
├── conftest.py
├── pages/
│   ├── home_page.py
│   └── flight_page.py
└── tests/
    └── test_round_trip.py
```

## Running the tests

Run the round-trip test:

```bash
pytest tests/test_round_trip.py --headed
```

Run the whole suite:

```bash
pytest --headed
```

Useful options:

| Option | What it does |
| --- | --- |
| `--slowmo 500` | Slows each action by 500 ms so you can watch the flow |
| `--tracing on` | Records a trace of the run |
| `-s` | Shows `print` output in the terminal |
| `-k round_trip` | Runs only tests whose name contains `round_trip` |

To inspect a trace after a failure:

```bash
playwright show-trace test-results/<test-folder>/trace.zip
```

To debug interactively, add `page.pause()` inside the test and run with `--headed`.

## Troubleshooting

- **"Access Denied" page (reference from `errors.edgesuite.net`):** the site blocked the automated browser. Make sure you run with `--headed`, that Chrome is installed (`playwright install chrome`), and that you are not on a VPN, corporate proxy, cloud VM, or Docker container. Try again from a normal home connection.
- **Locator not found:** the site's markup can change. Use `playwright codegen https://www.avianca.com/en` to regenerate the locator, and update the page object.
- **Date format assertion fails:** the site currently shows `MM/DD/YYYY`. If the format or the language of the labels changes, confirm that `locale` is set to `en-US` in `conftest.py`.
- **Timeouts on the booking page:** results can load slowly. Rerun, or increase the timeouts in `flight_page.py`.

## Notes

- Dates are calculated at run time (the first enabled day after today), so the tests do not go stale.
- The test plan expects dates in `DD/MM/YYYY`, but the site renders `MM/DD/YYYY`. The tests follow the site's actual behavior.
- Do not use these tests for load testing or run them at high frequency. Respect the site's terms of use.