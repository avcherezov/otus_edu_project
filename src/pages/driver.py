from abc import ABC, abstractmethod

from selenium import webdriver

from pages.main.page import MainPage
from pages.ab_test_control.page import ABTestControl
from pages.add_remove_elements.page import AddRemoveElements


class IObject(ABC):
    @abstractmethod
    def instance(self):
        pass

    @abstractmethod
    def _get_driver(self):
        pass

    @abstractmethod
    def _return_driver(self):
        pass


class UObject(IObject):
    __instance = None

    @staticmethod
    def instance():
        if UObject.__instance is None:
            UObject.__instance = UObject._return_driver()
        return UObject.__instance

    @staticmethod
    def _return_driver():
        UObject.__driver = UObject._get_driver()
        return UObject(UObject.__driver)

    @staticmethod
    def _get_driver():
        driver = webdriver.Safari()
        driver.get('http://the-internet.herokuapp.com')
        return driver

    def __init__(self, driver):
        self.driver = driver

    def close_browser(self):
        self.driver.quit()
    
    def get_main_page(self):
        self.driver.get('http://the-internet.herokuapp.com')

    @property
    def main_page(self):
        return MainPage(self.driver)
    
    @property
    def ab_test_control(self):
        return ABTestControl(self.driver)

    @property
    def add_remove_elements(self):
        return AddRemoveElements(self.driver)
