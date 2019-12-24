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
    add_case_right_button = '#sidebar-cases-add'

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
    # from text test case
    preconditions_input = '#custom_preconds'
    steps_input = '#custom_steps'
    results_input = '#custom_expected'
    add_case_button = '#accept'

    @allure.step('Ввод заголовка нового кейса: {title}')
    def set_title(self, title):
        input = s(self.title_input)
        input.clear()
        input.set_value(title)

    @allure.step('Ввод пред.условий нового кейса: {preconditions}')
    def set_preconditions(self, preconditions):
        input = s(self.preconditions_input)
        input.clear()
        input.set_value(preconditions)

    @allure.step('Ввод шагов нового кейса: {steps}')
    def set_steps(self, steps):
        input = s(self.steps_input)
        input.clear()
        input.set_value(steps)

    @allure.step('Ввод ожидаемого результата нового кейса: {results}')
    def set_results(self, results):
        input = s(self.results_input)
        input.clear()
        input.set_value(results)

    @allure.step('Клик по кнопке добавления нового кейса')
    def click_add_case(self):
        s(self.add_case_button).click()
        return ShowCaseSubPage()


class ShowCaseSubPage(CommonProjectPage):

    title_input = '.content-header-title.page_title'

    @allure.step('Проверка заголовка {title} при просмотре кейса')
    def assert_title_is_correct(self, title):
        assert s(self.title_input).text == title

