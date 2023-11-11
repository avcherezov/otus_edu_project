from common import ExceptionHandler

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    timeout = 3

    def __init__(self, driver):
        self._driver = driver

    def _find_element(self, element, locator, time=timeout):
        try:
            return WebDriverWait(element, time).until(
                ec.visibility_of_element_located(locator),
                message="Can't find element by locator {}".format(locator),
            )
        except Exception as e:
            return ExceptionHandler.handle(e, self)

    def _find_elements(self, element, locator, time=timeout):
        try:
            return WebDriverWait(element, time).until(
                ec.visibility_of_all_elements_located(locator),
                message="Can't find elements by locator {}".format(locator),
            )
        except Exception as e:
            return ExceptionHandler.handle(e, self)

    def _click_element(self, element, locator, time=timeout):
        try:
            wait = WebDriverWait(element, time)
            wait.until(
                ec.element_to_be_clickable(locator),
                message="Not clickable element {}".format(locator),
            ).click()
        except Exception as e:
            return ExceptionHandler.handle(e, self)

    def _send_keys(self, element, locator, data, time=timeout):
        try:
            wait = WebDriverWait(element, time)
            wait.until(
                ec.visibility_of_element_located(locator),
                message="Not visibility element {}".format(locator),
                ).send_keys(data)
        except Exception as e:
            return ExceptionHandler.handle(e, self)

    def _wait_invisible_element(self, element, locator, time=timeout):
        try:
            wait = WebDriverWait(element, time)
            wait.until(
                ec.invisibility_of_element_located(locator),
                message="Not visibility element {}".format(locator),
                )
        except Exception as e:
            return ExceptionHandler.handle(e, self)
