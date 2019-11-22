import allure
from selene.support.by import link_text
from selene.support.jquery_style_selectors import s, ss

from pages.common.common_page import CommonPage
from pages.admin.projects_subpage import AddProjectSubPage


class DashboardPage(CommonPage):

    add_project_button = 'a.sidebar-button'
    projects_table = '#content-inner > div.table.summary.summary-auto'

    def _search_project_in_table(self, name):
        for item in ss(self.projects_table):
            if item.s(link_text(name)).text == name:
                return item
        return None

    @allure.step('Клик по кнопке добавления нового проекта')
    def click_add_project(self):
        s(self.add_project_button).click()
        return AddProjectSubPage()

    @allure.step('Клик по заголовку проекта: {title}')
    def click_by_project_title(self, title):
        item = self._search_project_in_table(title)
        item.s(link_text(title)).click()
        return





