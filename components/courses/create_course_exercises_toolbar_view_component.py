from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import re


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id(
            'create-course-exercises-box-toolbar-title-text'
        )
        self.create_exercise_button = page.get_by_test_id(
            'create-course-exercises-box-toolbar-create-exercise-button'
        )

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Exercises')

        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        expect(self.create_exercise_button).to_be_visible()
        self.create_exercise_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))