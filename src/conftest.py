import pytest

from pages.driver import UObject
from common import Command, IOCContainer


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = UObject.instance()
    yield driver
    driver.close_browser()


@pytest.fixture(autouse=True)
def command():
    ioc = IOCContainer()
    ioc.register('command', Command)
    command = ioc.resolve('command')
    yield command
    command.clear()


@pytest.fixture(autouse=True)
def get_main_page(driver):
    yield
    driver.get_main_page()
