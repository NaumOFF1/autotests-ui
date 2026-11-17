from components.base_component import BaseComponent

from playwright.sync_api import Page, expect


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str, title: str):
        super().__init__(page)

        self.title_text = title
        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.title_text)
        expect(self.chart).to_be_visible()
