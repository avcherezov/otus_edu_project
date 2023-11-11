from common import ICommand, func_info
from pages.base import BasePage
from pages.main.locators import MainPageLocators


class MainPage(BasePage):
    @func_info
    def click_ab_testing(self):
        """Нажать кнопку - A/B Testing"""
        self._click_element(self._driver, MainPageLocators.BUTTON_AB_TESTING)

    @func_info
    def click_add_remove_elements(self):
        """Нажать кнопку - Add/Remove Elements"""
        self._click_element(self._driver, MainPageLocators.BUTTON_ADD_REMOVE_ELEMENTS)


class ClickABTesting(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        self.__executor.click_ab_testing()


class ClickAddRemoveElements(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        self.__executor.click_add_remove_elements()
