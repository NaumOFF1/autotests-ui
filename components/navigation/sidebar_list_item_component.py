from re import Pattern

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(
            page, "{identifier}-drawer-list-item-icon", "Sidebar list item icon"
        )
        self.title = Text(
            page, "{identifier}-drawer-list-item-title-text", "Sidebar list item title"
        )
        self.button = Button(
            page, "{identifier}-drawer-list-item-button", "Sidebar list item button"
        )

    @allure.step("Check visible '{title}' sidebar list item")
    def check_visible(self, identifier: str, title: str):
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        self.button.check_visible(identifier=identifier)

    def navigate(self, expected_url: Pattern[str], identifier: str):
        self.button.click(identifier=identifier)
        self.check_current_url(expected_url)
