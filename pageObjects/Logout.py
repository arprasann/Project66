from selenium.webdriver.common.by import By


class Logout:

    logout = (By.ID,"logoutLink1")
    
    def __init__(self,driver):
        self.driver = driver


    def clickonlogoutbutton(self):
        return self.driver.find_element(*Logout.logout).click()