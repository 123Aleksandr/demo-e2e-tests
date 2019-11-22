import allure

from selene import config, browser
from selene.browsers import BrowserName
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config import *
from entities.project import Project
from pages.auth.auth_page import AuthPage


config.browser_name = BrowserName.CHROME
config.timeout = 10
config.poll_during_waits = 0.5


class TestProject:

    def setup_method(self, method):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        browser.set_driver(driver)

    def teardown_method(self, method):
        browser.driver().quit()

    @allure.title('Добавление проекта, раздела и кейса')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_new_section_and_case(self):
        my_project = Project()
        dash_page = AuthPage().auth()
        add_project_page = dash_page.click_add_project()
        add_project_page.set_name(my_project.name)
        add_project_page.set_announcement(my_project.announcement)
        add_project_page.select_show_announcement(my_project.show_announcement)
        add_project_page.select_project_view(my_project.view)
        projects_page = add_project_page.click_add_project()
        dash_page = projects_page.click_by_dashboard_item()
        dash_page




