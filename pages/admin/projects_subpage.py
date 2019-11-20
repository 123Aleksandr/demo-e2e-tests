import allure

from selene.support.by import link_text
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s, ss

from pages.admin.admin_page import AdminPage


class ProjectsSubPage(AdminPage):

    add_project_button = 'button.button-left.button-add'
    projects_table = 'tr.hoverSensitive'
    element_row = 'td:nth-child(1) > a'
    edit_icon = 'td > a > div.icon-small-edit'
    delete_icon = 'td > a > div.icon-small-delete'


    def _search_project_in_table(self, name):
        for item in ss(self.projects_table):
            if item.s(self.element_row).text == name:
                return item
        return None

    @allure.step('Проверка существования проекта {name} в таблице проектов')
    def assert_name_is_exist_in_list(self, name):
        item = self._search_project_in_table(name)
        assert item is not None

    @allure.step('Проверка отсутствия проекта {name} в таблице проектов')
    def assert_name_is_not_exist_in_list(self, name):
        item = self._search_project_in_table(name)
        assert item is None

    @allure.step('Клик по названию проекта {name} в таблице проектов')
    def click_project_name(self, name):
        s(link_text(name)).click()
        return EditProjectSubPage()

    @allure.step('Клик по значку редактирования проекта {name} в таблице проектов')
    def click_project_edit_icon(self, name):
        item = self._search_project_in_table(name)
        item.s(self.edit_icon).click()
        return EditProjectSubPage()

    @allure.step('Клик по значку удаления проекта {name} в таблице проектов')
    def click_project_edit_icon(self, name):
        item = self._search_project_in_table(name)
        item.s(self.delete_icon).click()

    @allure.step('Клик по кнопке добавления нового проекта')
    def click_add_project(self):
        s(self.add_project_button).click()
        return AddProjectSubPage()


class AddProjectSubPage(AdminPage):

    name_input = '[id="name"]'
    announcement_input = '[id="announcement"]'
    show_announcement_check = '[id="show_announcement"]'
    radio_suite_mode_single = '[id="suite_mode_single"]'
    radio_suite_mode_single_baseline = '[id="suite_mode_single_baseline"]'
    radio_suite_mode_multi = '[id="suite_mode_multi"]'
    add_project_button = 'button.button-left.button-positive.button-ok'

    @allure.step('Ввод названия "{name}" нового проекта')
    def set_name(self, name):
        s(self.name_input).set_value(name)

    @allure.step('Ввод описания "{announcement}" нового проекта')
    def set_announcement(self, announcement):
        s(self.announcement_input).set_value(announcement)

    @allure.step('Чекбокс отображения описания на странице: {check_value}')
    def select_show_announcement(self, check_value):
        if not isinstance(check_value, bool):
            raise TypeError('Указанное значение не является булевым!')
        # driver.execute_script(("return document.getElementById('%s').checked") % item)
        # element.get_attribute('checked')
        checkbox = s(self.show_announcement_check)
        if (checkbox.is_selected() and check_value is True) or (not checkbox.is_selected() and check_value is False):
            return True
        elif (checkbox.is_selected() and check_value is False) or (not checkbox.is_selected() and check_value is True):
            checkbox.click()

    @allure.step('Выбор представления проекта: {param}')
    def select_project_view(self, param):
        if param == 'suite_mode_single':
            s(self.radio_suite_mode_single).click()
        elif param == 'suite_mode_single_baseline':
            s(self.radio_suite_mode_single_baseline).click()
        elif param == 'suite_mode_multi':
            s(self.radio_suite_mode_multi).click()
        else:
            raise ValueError('Указанного параметра не существует!')

    @allure.step('Клик по кнопке добавления нового проекта')
    def click_add_project(self):
        s(self.add_project_button).click()
        return ProjectsSubPage()


class EditProjectSubPage(AddProjectSubPage):

    is_completed_check = '[id="is_completed"]'

    @allure.step('Чекбокс окончания проекта: {check_value}')
    def select_is_completed(self, check_value):
        if not isinstance(check_value, bool):
            raise TypeError('Указанное значение не является булевым!')
        # driver.execute_script(("return document.getElementById('%s').checked") % item)
        # element.get_attribute('checked')
        checkbox = s(self.is_completed_check)
        if (checkbox.is_selected() and check_value is True) or (not checkbox.is_selected() and check_value is False):
            return True
        elif (checkbox.is_selected() and check_value is False) or (not checkbox.is_selected() and check_value is True):
            checkbox.click()

