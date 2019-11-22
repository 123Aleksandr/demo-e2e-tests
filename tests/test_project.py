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

    @allure.title('Добавление с дешборда нового проекта и удаление')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_new_project_from_admin_page(self):
        my_project = Project(view='suite_mode_single_baseline')
        dash_page = AuthPage().auth()
        add_project_page = dash_page.click_add_project()
        add_project_page.set_name(my_project.name)
        add_project_page.set_announcement(my_project.announcement)
        add_project_page.select_show_announcement(my_project.show_announcement)
        add_project_page.select_project_view(my_project.view)
        projects_page = add_project_page.click_add_project()
        projects_page.assert_name_is_exist_in_list(my_project.name)
        delete_modal_window = projects_page.click_project_delete_icon(my_project.name)
        delete_modal_window.select_confirm_project(True)
        delete_modal_window.click_delete()
        projects_page.assert_name_is_not_exist_in_list(my_project.name)

    @allure.title('Создание нового проекта со страницы администрирования')
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_new_project_from_dashboard(self):
        my_project = Project()
        dash_page = AuthPage().auth()
        admin_page = dash_page.click_by_admin_item()
        add_project_page = admin_page.click_add_project()
        add_project_page.set_name(my_project.name)
        add_project_page.set_announcement(my_project.announcement)
        add_project_page.select_show_announcement(my_project.show_announcement)
        add_project_page.select_project_view(my_project.view)
        projects_page = add_project_page.click_add_project()
        projects_page.assert_name_is_exist_in_list(my_project.name)

    @allure.title('Изменение названия проекта')
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_project_name(self):
        my_project = Project()
        dash_page = AuthPage().auth()
        add_project_page = dash_page.click_add_project()
        add_project_page.set_name(my_project.name)
        add_project_page.set_announcement(my_project.announcement)
        add_project_page.select_show_announcement(my_project.show_announcement)
        add_project_page.select_project_view(my_project.view)
        projects_page = add_project_page.click_add_project()
        edit_page = projects_page.click_project_name(my_project.name)
        my_project.name = Project().name
        edit_page.set_name(my_project.name)
        projects_page = edit_page.click_add_project()
        projects_page.assert_name_is_exist_in_list(my_project.name)

    @allure.title('Отказ от удаления проекта')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_cancel(self):
        my_project = Project()
        dash_page = AuthPage().auth()
        add_project_page = dash_page.click_add_project()
        add_project_page.set_name(my_project.name)
        add_project_page.set_announcement(my_project.announcement)
        add_project_page.select_show_announcement(my_project.show_announcement)
        add_project_page.select_project_view(my_project.view)
        projects_page = add_project_page.click_add_project()
        delete_modal_window = projects_page.click_project_delete_icon(my_project.name)
        delete_modal_window.select_confirm_project(True)
        delete_modal_window.click_cancel()
        projects_page.assert_name_is_exist_in_list(my_project.name)

