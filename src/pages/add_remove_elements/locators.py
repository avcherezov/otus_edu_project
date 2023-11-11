from selenium.webdriver.common.by import By


class AddRemoveElementsLocators:
    TITLE = (By.XPATH, './/div[@id="content"]/h3')
    BUTTON_ADD_ELEMENT = (By.XPATH, './/div[@class="example"]/button')
    BUTTON_DELETE = (By.XPATH, './/button[@class="added-manually"]')
