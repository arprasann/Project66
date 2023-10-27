from selenium.webdriver.common.by import By


class CheckBox:

    checkBox = (By.ID, "keepLoggedInCheckBox")

    def __init__(self,driver):
        self.driver = driver

    def clickoncheckbox(self):
        return self.driver.find_element(*CheckBox.checkBox).click()
