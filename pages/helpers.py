# helpers

def checkbox_select(checkbox, check_value):
    if not isinstance(check_value, bool):
        raise TypeError('Указанное значение не является булевым!')
    # driver.execute_script(("return document.getElementById('%s').checked") % item)
    # element.get_attribute('checked')
    if (checkbox.is_selected() and check_value is True) or (not checkbox.is_selected() and check_value is False):
        return True
    elif (checkbox.is_selected() and check_value is False) or (not checkbox.is_selected() and check_value is True):
        checkbox.click()

