from pages.main.page import *
from pages.ab_test_control.page import *


def test_ab_testing(driver, command):
    command.add_command(ClickABTesting(driver.main_page))
    command.run_command()

    command.add_command(FindTitleABTestControl(driver.ab_test_control))
    status = command.run_command().text

    assert status in ['A/B Test Control', 'A/B Test Variation 1'], f'Error - {status}'
