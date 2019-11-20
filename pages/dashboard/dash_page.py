import allure
from selene.support.jquery_style_selectors import s, ss

from pages.common.common_page import CommonPage
from pages.admin.admin_page import AdminPage


class DashboardPage(CommonPage):

    add_project_button = 'a.sidebar-button'

    @allure.step('Клик по кнопке добавления нового проекта')
    def click_add_project(self):
        s(self.add_project_button).click()
        return AdminPage()

