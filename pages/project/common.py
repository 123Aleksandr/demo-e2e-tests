import allure

from selene.api import *
from selene.support.jquery_style_selectors import s, ss

from pages.common.common_page import CommonPage


class CommonProjectPage(CommonPage):

    overview_button = '#navigation-projects'
    todo_button = '#navigation-todos'
    milestone_button = '#navigation-milestones'
    test_run_button = '#navigation-runs'
    test_case_button = '#navigation-suites'
    report_button = '#navigation-reports'

    def click_by_dashboard_item(self):
        raise Exception('Метод не доступен в данном контексте!')

    @allure.step('Клик по по кнопке перехода в раздел {item_name} проекта')
    def click_by_project_menu_item(self, item_name):
        if item_name == 'Overview':
            from pages.project.overview_subpage import OverviewSubPage
            s(self.overview_button).click()
            return OverviewSubPage()
        elif item_name =='Todo':
            pass
        elif item_name =='Milestones':
            pass
        elif item_name =='Test Runs & Results':
            pass
        elif item_name =='Test Cases':
            from pages.project.cases_subpage import CaseSubPage
            s(self.test_case_button).click()
            return CaseSubPage()
        elif item_name =='Reports':
            pass
        else:
            raise ValueError('В проекте нет пункта меню с указанным значением!')

