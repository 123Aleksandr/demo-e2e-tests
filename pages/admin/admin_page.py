import allure
from selene.support.by import link_text
from selene.support.jquery_style_selectors import s

from pages.common.common_page import CommonPage


class AdminPage(CommonPage):

    @allure.step('Клик по пункту меню {name_item}')
    def click_by_menu_item(self, name_item):
        from pages.admin.projects_subpage import ProjectsSubPage
        s(link_text(name_item)).click()
        if name_item == 'Overview':
            return self
        elif name_item == 'Projects':
            return ProjectsSubPage()
        elif name_item == 'Users & Roles':
            pass
        elif name_item == 'Customizations':
            pass
        elif name_item == 'Integration':
            pass
        elif name_item == 'Subscription':
            pass
        elif name_item == 'Site Settings':
            pass
        else:
            raise ValueError('В администраторском разделе нет пункта меню с указанным значением!')

    # Project
    @allure.step('Клик по заголовку блока проектов')
    def click_by_link_view_projects(self):
        from pages.admin.projects_subpage import ProjectsSubPage
        s(link_text('Projects')).click()
        return ProjectsSubPage()

    @allure.step('Клик по линку просмотра проектов')
    def click_by_link_view_projects(self):
        from pages.admin.projects_subpage import ProjectsSubPage
        s(link_text('View projects')).click()
        return ProjectsSubPage()

    @allure.step('Клик по линку добавления нового проекта')
    def click_add_project(self):
        from pages.admin.projects_subpage import AddProjectSubPage
        s(link_text('Add a new project')).click()
        return AddProjectSubPage()

