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

