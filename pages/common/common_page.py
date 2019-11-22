import allure

from selene.api import *
from selene.support.jquery_style_selectors import s, ss


class CommonPage(object):

    dashboard_menu_button = '#navigation-dashboard'
    admin_menu_button = '#navigation-admin'

    @allure.step('Клик по кнопке перехода на дешборд верхнего меню')
    def click_by_dashboard_item(self):
        from pages.dashboard.dash_page import DashboardPage
        s(self.dashboard_menu_button).click()
        return DashboardPage()

    @allure.step('Клик по кнопке перехода в раздел администрирования верхнего меню')
    def click_by_admin_item(self):
        from pages.admin.admin_page import AdminPage
        s(self.admin_menu_button).click()
        return AdminPage()

