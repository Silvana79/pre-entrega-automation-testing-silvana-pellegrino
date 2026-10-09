from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

REPORTS_DIR = Path("reports")
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(
        service=service,
        options=options
    )

    browser.implicitly_wait(0)

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")

    if driver is None:
        return

    SCREENSHOTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    safe_test_name = "".join(
        character
        if character.isalnum() or character in ("-", "_")
        else "_"
        for character in item.nodeid
    )

    screenshot_path = (
        SCREENSHOTS_DIR
        / f"{safe_test_name}_{timestamp}.png"
    )

    try:
        driver.save_screenshot(
            str(screenshot_path)
        )
    except Exception:
        pass
        