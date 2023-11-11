from common import ICommand, func_info
from pages.base import BasePage
from pages.ab_test_control.locators import ABTestControlLocators


class ABTestControl(BasePage):
    @func_info
    def find_title_ab_test_control(self):
        """Найти заголовок раздела A/B Testing"""
        return self._find_element(self._driver, ABTestControlLocators.TITLE)


class FindTitleABTestControl(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.find_title_ab_test_control()
