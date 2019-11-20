import allure

from selene.support.by import link_text
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

from pages.admin import *
from pages.common.common_page import CommonPage


class AdminPage(CommonPage):

    # todo
    @allure.step('Клик по пункту меню {name_item}')
    def click_by_menu_item(self, name_item):
        s(link_text(name_item)).click()
        if name_item == 'Overview':
            return
        elif name_item == 'Projects':
            return
        elif name_item == 'Users & Roles':
            return
        elif name_item == 'Customizations':
            return
        elif name_item == 'Integration':
            return
        elif name_item == 'Subscription':
            return
        elif name_item == 'Site Settings':
            return
        else:
            raise ValueError('В администраторском разделе нет пункта меню с указанным значением!')