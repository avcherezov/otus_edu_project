from common import ICommand, func_info
from pages.base import BasePage
from pages.dynamic_loading.locators import DynamicLoadingLocators


class DynamicLoading(BasePage):
    @func_info
    def click_example_1(self):
        """Нажать кнопку - Example 1"""
        return self._click_element(self._driver, DynamicLoadingLocators.EXAMPLE_1)

    @func_info
    def click_start(self):
        """Нажать кнопку - Start"""
        return self._click_element(self._driver, DynamicLoadingLocators.BUTTON_START)

    @func_info
    def wait_loading(self):
        """Ждать окончание загрузки"""
        return self._wait_invisible_element(self._driver, DynamicLoadingLocators.LOADING, timeout=15)

    @func_info
    def find_text(self):
        """Найти текст после загрузки"""
        return self._find_element(self._driver, DynamicLoadingLocators.FINISH)


class ClickExample1(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.click_example_1()


class ClickStart(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.click_start()


class WaitLoading(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.wait_loading()


class FindText(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.find_text()
