#Импортуруем нужную библиотеку
from playwright.sync_api import sync_playwright, expect

#Запускаем playwright
with sync_playwright() as playwright:
    #Запускаем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    #Переходим на тестируемую страницу
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    #Находим элемент email на странице и вводим в него тестовое значение
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    #Находим элемент Username на странице и вводим в него тестовое значение
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    #Находим элемент Password на странице и вводим в него тестовое значение
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    #Находим кнопку Registration и нажимаем на нее
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    #Проверяем, что на странице отображается заголовок Dashboard
    dashboard_toolbar_title_text = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_toolbar_title_text).to_be_visible()
    expect(dashboard_toolbar_title_text).to_have_text('Dashboard') 



