import pytest

from pages.driver import UObject
from common import Command


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = UObject.instance()
    yield driver
    driver.close_browser()


@pytest.fixture(autouse=True)
def command():
    command = Command()
    yield command
    command.clear()


@pytest.fixture(autouse=True)
def get_main_page(driver):
    yield 
    driver.get_main_page()
