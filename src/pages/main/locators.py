from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_AB_TESTING = (By.XPATH, './/a[@href="/abtest"]')
    BUTTON_ADD_REMOVE_ELEMENTS = (By.XPATH, './/a[@href="/add_remove_elements/"]')
    BUTTON_CHECKBOXES = (By.XPATH, './/a[@href="/checkboxes"]')
    BUTTON_DYNAMIC_LOADING = (By.XPATH, './/a[@href="/dynamic_loading"]')
