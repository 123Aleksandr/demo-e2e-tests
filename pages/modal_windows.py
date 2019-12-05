import allure
from selene.support.jquery_style_selectors import s

from pages.helpers import *


class DeleteProjectModal(object):

    delete_window_modal = '#dialog-ident-deleteDialog'
    confirm_project_check = '[name="deleteCheckbox"]'
    ok_button = 'a.button.button-ok'
    cancel_button = 'a.button.button-cancel'

    @allure.step('Чекбокс подтверждения удаления проекта: {check_value}')
    def select_confirm_project(self, check_value):
        checkbox = s(self.delete_window_modal).s(self.confirm_project_check)
        checkbox_select(checkbox, check_value)

    @allure.step('Клик по кнопке подтверждения удаления проекта')
    def click_delete(self):
        from pages.admin.projects_subpage import ProjectsSubPage
        s(self.delete_window_modal).s(self.ok_button).click()
        return ProjectsSubPage()

    @allure.step('Клик по кнопке отмены удаления проекта')
    def click_cancel(self):
        from pages.admin.projects_subpage import ProjectsSubPage
        s(self.delete_window_modal).s(self.cancel_button).click()
        return ProjectsSubPage()


class AddSectionModal(object):

    section_name_input = '#editSectionName'
    section_description_input = '#editSectionDescription'
    ok_section_button = '#editSectionSubmit'
    cancel_section_button = '#editSectionForm > div.button-group.dialog-buttons-highlighted > a'

    @allure.step('Ввод названия {name} нового раздела')
    def set_name(self, name):
        input = s(self.section_name_input)
        input.set_value(name)

    @allure.step('Ввод описания {desc} нового проекта')
    def set_announcement(self, desc):
        input = s(self.section_description_input)
        input.set_value(desc)

    @allure.step('Клик по кнопке подтверждения создания раздела')
    def click_add_section(self):
        from pages.project.cases_subpage import CaseSubPage
        s(self.ok_section_button).click()
        return CaseSubPage()

