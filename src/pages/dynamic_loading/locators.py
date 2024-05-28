from selenium.webdriver.common.by import By


class DynamicLoadingLocators:
    EXAMPLE_1 = (By.XPATH, './/a[@href="/dynamic_loading/1"]')
    BUTTON_START = (By.XPATH, './/div[@id="start"]/button')
    LOADING = (By.XPATH, './/div[@id="loading"]')
    FINISH = (By.XPATH, './/div[@id="finish"]')
