import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_empty_courses_list(
            self,
            courses_list_page:
            CoursesListPage
    ):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.check_visible_empty_view()

    def test_create_course(
            self,
            courses_list_page: CoursesListPage,
            create_course_page: CreateCoursePage
    ):
        # Открыть страницу
        create_course_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page.toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        # Проверить, что форма создания курса отображается и содержит значения по умолчанию
        create_course_page.create_course_form.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )
        create_course_page.exercises_toolbar_view.check_visible()
        # Убедиться, что отображается блок с пустыми заданиями
        create_course_page.check_visible_exercises_empty_view()
        # Загрузить изображение для превью курса
        create_course_page.image_upload_widget.upload_preview_image(file='./testdata/files/image.png')
        # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        # Заполнить форму создания курса значениями
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        # Нажать на кнопку создания курса
        create_course_page.toolbar_view.click_create_course_button()

        # После создания курса произойдет редирект на страницу со списком курсов
        courses_list_page.toolbar_view.check_visible()
        # Проверить корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score=100,
            min_score=10,
            estimated_time="2 weeks"
        )

    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_form.fill(
            title='Физика',
            estimated_time='3 часа',
            description='Курс по физике',
            max_score='100',
            min_score='10'
        )
        create_course_page.image_upload_widget.upload_preview_image(
            file='./testdata/files/image.png'
        )
        create_course_page.toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Физика',
            estimated_time='3 часа',
            max_score='100',
            min_score='10'
        )
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title='Математика',
            estimated_time='2 часа',
            description='Курс по математике',
            max_score='500',
            min_score='100'
        )
        create_course_page.toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Математика',
            estimated_time='2 часа',
            max_score='500',
            min_score='100'
        )
