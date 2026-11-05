import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture  # Фикстура создает новую страницу в браузере
def chromium_page(playwright: Playwright) -> Page:  # type: ignore
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()  # type: ignore
    browser.close()


# Фикстура регистрирует нового пользователя и сохраняет состояние браузера для последующего использования
@pytest.fixture(scope="session", autouse=False)
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим элемент email на странице и вводим в него тестовое значение
    email_input = page.get_by_test_id(
        'registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Находим элемент Username на странице и вводим в него тестовое значение
    username_input = page.get_by_test_id(
        'registration-form-username-input').locator('input')
    username_input.fill('username')

    # Находим элемент Password на странице и вводим в него тестовое значение
    password_input = page.get_by_test_id(
        'registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id(
        'registration-page-registration-button')
    registration_button.click()

    # Добавил ожидание networkidle, без него localStorage не успевал записаться в файл
    page.wait_for_load_state('networkidle')

    yield context.storage_state(path="browser-state.json")

    browser.close()


# фикстура открывает новую страницу браузера, используя сохраненное состояние из файла browser-state.json
@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:  # type: ignore
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state="browser-state.json")

    yield context.new_page()  # type: ignore

    browser.close()
