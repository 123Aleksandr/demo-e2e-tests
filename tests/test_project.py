import uuid
import pytest

import allure

from selenium import webdriver
from selene import config, browser
from selene.browsers import BrowserName

from utils import *
from config import *
from pages.auth.auth_page import AuthPage
from pages.dashboard.dash_page import DashboardPage


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




    @allure.title('Добавление нового проекта (с дешборда), проверка отображения в списке проектов, удаление')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_new_project_from_admin_page(self):
        dash_page = AuthPage().auth()
        add_project_page = dash_page.click_add_project()
        add_project_page.set_name(get_object_name())
        add_project_page.set_announcement(get_text(max_chars=160))
        add_project_page.select_show_announcement(True)
        add_project_page.select_project_view('suite_mode_single_baseline')
        add_project_page.click_add_project()

