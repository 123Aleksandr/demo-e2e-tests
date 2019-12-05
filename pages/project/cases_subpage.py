import allure
from selene.support.by import link_text
from selene.support.jquery_style_selectors import s, ss

from pages.project.common import CommonProjectPage
from pages.modal_windows import AddSectionModal
from pages.admin.projects_subpage import AddProjectSubPage
from pages.admin.admin_page import AdminPage


class CaseSubPage(CommonProjectPage):

    add_section_start_button = '#addSectionInline'
    add_case_start_button = '#addSectionInline ~ a'
    add_case_right_button = '#addTestCaseButtonSidebar'

    @allure.step('Клик по кнопке добавления нового раздела')
    def click_add_section(self):
        s(self.add_section_start_button).click()
        return AddSectionModal()

    @allure.step('Клик по кнопке перехода на страницу добавления кейса')
    def click_add_case(self):
        s(self.add_case_right_button).click()
        return AddCaseSubPage()


class AddCaseSubPage(CommonProjectPage):

    title_input = '#title'
    preconditions_input = '#custom_preconds'
    steps = '#custom_steps'
    results = '#custom_expected'

    @allure.step('Ввод заголовка {name} нового кейса')
    def set_title(self, title):
        input = s(self.title_input)
        input.clear()
        input.set_value(title)







