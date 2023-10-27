
from utilities.base import BaseClass

from pageObjects.LoginPage import LoginPage

from pageObjects.Logout import Logout


class Test_Logout_Test(BaseClass):

    def test_verify_logout(self):
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforsometime()
        loginpage.clickonloginbutton()

        logout = Logout(self.driver)
        self.waitforsometime()
        logout.clickonlogoutbutton()
        self.waitforsometime()