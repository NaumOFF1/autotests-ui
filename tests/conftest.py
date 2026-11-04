import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:  # type: ignore
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()  # type: ignore
    browser.close()
