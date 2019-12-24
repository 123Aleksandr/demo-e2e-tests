import pytest
import allure

from selene import config, browser
from selene.browsers import BrowserName
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from entities.project import Project, Case
from pages.auth.auth_page import AuthPage


config.browser_name = BrowserName.CHROME
config.timeout = 10
config.poll_during_waits = 0.5


class TestCase:

    def setup_method(self, method):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        browser.set_driver(driver)

    def teardown_method(self, method):
        browser.driver().quit()

    @allure.title('Создание проекта и добавление кейса')
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
        project_page = dash_page.click_by_project_title(my_project.name)
        testcases_subpage = project_page.click_by_project_menu_item('Test Cases')
        add_testcase_subpage = testcases_subpage.click_add_case()
        my_case = Case('text_test_case')
        add_testcase_subpage.set_title(my_case.title)
        add_testcase_subpage.set_preconditions(my_case.preconditions)
        add_testcase_subpage.set_steps(my_case.steps)
        add_testcase_subpage.set_results(my_case.result)
        show_testcase_subpage = add_testcase_subpage.click_add_case()
        show_testcase_subpage.assert_title_is_correct(my_case.title)


    @pytest.mark.parametrize('title', [
        ('Текстовое название'),
        ('77934'),
        ('selene 可愛い ^^'),
    ])
    @allure.title('Создание кейса с определенным наименованием')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_case_title(self, title):
        my_project = Project()
        dash_page = AuthPage().auth()
        add_project_page = dash_page.click_add_project()
        add_project_page.set_name(my_project.name)
        add_project_page.select_project_view(my_project.view)
        projects_page = add_project_page.click_add_project()
        dash_page = projects_page.click_by_dashboard_item()
        project_page = dash_page.click_by_project_title(my_project.name)
        testcases_subpage = project_page.click_by_project_menu_item('Test Cases')
        add_testcase_subpage = testcases_subpage.click_add_case()
        add_testcase_subpage.set_title(title)
        show_testcase_subpage = add_testcase_subpage.click_add_case()
        show_testcase_subpage.assert_title_is_correct(title)

