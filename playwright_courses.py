from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
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

    context.storage_state(path="browser-state.json")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_list_title_text = page.get_by_test_id(
        'courses-list-toolbar-title-text')
    expect(courses_list_title_text).to_be_visible()
    expect(courses_list_title_text).to_have_text('Courses')

    courses_list_empty_view_title_text = page.get_by_test_id(
        'courses-list-empty-view-title-text')
    expect(courses_list_empty_view_title_text).to_be_visible()
    expect(courses_list_empty_view_title_text).to_have_text(
        'There is no results')

    courses_list_empty_view_icon = page.get_by_test_id(
        'courses-list-empty-view-icon')
    expect(courses_list_empty_view_icon).to_be_visible()

    ourses_list_empty_view_description_text = page.get_by_test_id(
        'courses-list-empty-view-description-text')
    expect(ourses_list_empty_view_description_text).to_be_visible()
    expect(ourses_list_empty_view_description_text).to_have_text(
        'Results from the load test pipeline will be displayed here')
