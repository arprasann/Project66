
from pageObjects.LoginPage import LoginPage

from utilities.base import BaseClass

class Test_LoginPage(BaseClass):

    def test_loginpage(self):
        log = self.getLogger()
         # Everify valid
        log.info("Valid Login Page Script started...")
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        log.info("Enter the valid Username")
        loginpage.setusername("admin")

        log.info("Succssfully fetched data from dataload")
        self.waitforsometime()
        log.info("Enter The Valid Password")
        loginpage.setpassword("manager")
        self.waitforsometime()
        log.info("Click On Login Button")
        loginpage.clickonloginbutton()
        self.waitforsometime()
        log.info("Login Page scrip successfully Executed")
