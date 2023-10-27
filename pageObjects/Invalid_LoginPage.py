from selenium.webdriver.common.by import By
from utilities.base import BaseClass

class Invalid_LoginPage(BaseClass):

    errormsg = (By.XPATH,"(//span[@class='errormsg'])[1]")

    def __init__(self,driver):
        self.driver = driver


    def verify_error_msg(self):
        self.verify_element_presence(By.XPATH,"(//span[@class='errormsg'])[1]")
        error = self.driver.find_element(*Invalid_LoginPage.errormsg)
        assert error.text == "abcd"
        if error.is_displayed():
            print("True: It is Inavlaid LoginPage ")
        else:
            print("False: It is not a Inavlaid LoginPage ")
