import allure

from selene.api import *
from selene.browser import open_url
from selene.support.jquery_style_selectors import s, ss

from config import BASE_URL, LOGIN, PASSWORD
from pages.dashboard.dash_page import DashboardPage


class AuthPage(object):

    username_input = '[id="name"]'
    password_input = '[id="password"]'
    submit_button = '[id="button_primary"]'

    @allure.step('Авторизуемся..')
    def auth(self):
        open_url(BASE_URL)
        s(self.username_input).set_value(LOGIN)
        s(self.password_input).set_value(PASSWORD)
        s(self.submit_button).click()
        return DashboardPage()

