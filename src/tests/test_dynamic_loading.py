from pages.main.page import *
from pages.dynamic_loading.page import *


def test_dynamic_loading(driver, command):
    command.add_command(ClickDynamicLoading(driver.main_page))
    command.run_command()

    command.add_command(ClickExample1(driver.dynamic_loading))
    command.run_command()

    command.add_command(ClickStart(driver.dynamic_loading))
    command.run_command()

    command.add_command(WaitLoading(driver.dynamic_loading))
    command.run_command()

    command.add_command(FindText(driver.dynamic_loading))
    status = command.run_command().text
    assert 'Hello World!' in status, f'Error - {status}'
