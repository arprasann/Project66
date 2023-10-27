import pytest

from utilities.base import BaseClass
from pageObjects.LoginPage import LoginPage
from pageObjects.Users import Create_Users

class Test_Verify_Users(BaseClass):

    def test_verify_users(self):
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforsometime()
        loginpage.clickonloginbutton()

        users = Create_Users(self.driver)
        self.waitforsometime()
        self.waitforsometime()
        users.click_On_Users()
        self.waitforsometime()
        users.click_On_User()
        self.waitforsometime()
        users.set_first_name("Dinga100")
        users.set_last_name("Manga2002")
        users.set_email("dinga100@gmail.com")
        users.set_user_name("prasanna")
        users.set_password("1234567")
        users.set_reenter_password("1234567")
        self.waitforsometime()

