from common import ICommand, func_info
from pages.base import BasePage
from pages.add_remove_elements.locators import AddRemoveElementsLocators


class AddRemoveElements(BasePage):
    @func_info
    def find_title_add_remove_elements(self):
        """Найти заголовок раздела - Add/Remove Elements"""
        return self._find_element(self._driver, AddRemoveElementsLocators.TITLE)
    
    @func_info
    def click_add_element(self):
        """Нажать кнопку - Add Element"""
        return self._click_element(self._driver, AddRemoveElementsLocators.BUTTON_ADD_ELEMENT)
    
    @func_info
    def find_button_delete(self):
        """Найти кнопку - Delete"""
        return self._find_element(self._driver, AddRemoveElementsLocators.BUTTON_DELETE)


class FindTitleAddRemoveElements(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.find_title_add_remove_elements()


class ClickAddElement(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.click_add_element()


class FindButtonDelete(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        return self.__executor.find_button_delete()