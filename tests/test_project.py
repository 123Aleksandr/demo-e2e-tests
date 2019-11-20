import uuid
import pytest

import allure

from selenium import webdriver

from selene import config, browser
from selene.browsers import BrowserName

from pages.auth.auth_page import AuthPage
from pages.dashboard.dash_page import DashboardPage
from config import *


config.browser_name = BrowserName.CHROME
config.timeout = 10
config.poll_during_waits = 0.5


class TestProject:

    def setup_method(self, method):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=CHROMEDRIVER_PATH)
        browser.set_driver(driver)

    def teardown_method(self, method):
        browser.driver().quit()

    @allure.title('Создание нового проекта')
    def test_add_new_project_from_dashboard(self):
        dash_page = AuthPage().auth()
        dash_page.click_add_project()




        # dash_page.check_page_title('Поиск и ведение объектов НСИ')

    def test_add_new_project_from_admin_page(self):
        dash_page = AuthPage().auth()



