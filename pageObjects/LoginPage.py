from selenium.webdriver.common.by import By

class LoginPage:
    username = (By.ID,"username")
    password = (By.NAME,"pwd")
    loginButton = (By.ID,"loginButton")


    def __init__(self,driver):
        self.driver = driver

    def setusername(self,un):
        return self.driver.find_element(*LoginPage.username).send_keys(un)

    def setpassword(self,pw):
        return self.driver.find_element(*LoginPage.password).send_keys(pw)

    def clickonloginbutton(self):
        return self.driver.find_element(*LoginPage.loginButton).click()

