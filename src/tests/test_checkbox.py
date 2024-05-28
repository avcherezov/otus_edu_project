from pages.main.page import *
from pages.checkboxes.page import *


def test_checkbox(driver, command):
    command.add_command(ClickCheckboxes(driver.main_page))
    command.run_command()

    command.add_command(ClickCheckbox1(driver.checkboxes))
    command.run_command()

    command.add_command(FindStatusCheckbox1(driver.checkboxes))
    status = command.run_command().is_selected()
    assert status, f'Error - {status}'

    command.add_command(ClickCheckbox1(driver.checkboxes))
    command.run_command()

    command.add_command(FindStatusCheckbox1(driver.checkboxes))
    status = command.run_command().is_selected()
    assert not status, f'Error - {status}'
