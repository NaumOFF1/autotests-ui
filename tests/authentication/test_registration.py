import allure
import pytest
from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.severity(Severity.CRITICAL)
    @allure.title("Successful user registration")
    def test_successful_registration(
        self, registration_page: RegistrationPage, dashboard_page: DashboardPage
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        registration_page.registration_form.fill(
            email="user@example.com", username="username", password="password"
        )
        registration_page.registration_form.check_visible(
            email="user@example.com", username="username", password="password"
        )
        registration_page.click_registration_button()
        dashboard_page.toolbar_view.check_visible()
