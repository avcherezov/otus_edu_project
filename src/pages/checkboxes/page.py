from common import ICommand, func_info
from pages.base import BasePage
from pages.checkboxes.locators import CheckboxLocators


class Checkboxes(BasePage):
    @func_info
    def click_checkbox_1(self):
        """Нажать чекбокс - checkbox 1"""
        return self._click_element(self._driver, CheckboxLocators.CHECKBOX_1)

    @func_info
    def find_status_checkbox_1(self):
        """Найти статус - checkbox 1"""
        return self._find_element(self._driver, CheckboxLocators.CHECKBOX_1)


class ClickCheckbox1(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.click_checkbox_1()


class FindStatusCheckbox1(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.find_status_checkbox_1()
