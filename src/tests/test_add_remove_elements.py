from pages.main.page import *
from pages.add_remove_elements.page import *


def test_ab_testing(driver, command):
    command.add_command(ClickAddRemoveElements(driver.main_page))
    command.run_command()

    command.add_command(FindTitleAddRemoveElements(driver.add_remove_elements))
    status = command.run_command().text
    assert status == 'Add/Remove Elements', f'Error - {status}'

    command.add_command(ClickAddElement(driver.add_remove_elements))
    command.run_command()

    command.add_command(FindButtonDelete(driver.add_remove_elements))
    status = command.run_command().text
    assert status == 'Delete', f'Error - {status}'

    command.add_command(ClickButtonDelete(driver.add_remove_elements))
    command.run_command()

    try:
        command.add_command(FindButtonDelete(driver.add_remove_elements))
        status = command.run_command().text
    except:
        assert True
