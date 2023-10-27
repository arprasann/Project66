from utilities.base import BaseClass
from pageObjects.LoginPage import LoginPage
from pageObjects.Administrator_PasswordChange import Administrator

class Test_Administartor_Changes(BaseClass):


    def test_administror_changes(self):
        log = self.getLogger()
        log.info("Script for Administror save changes")
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        log.info("Enter valid username")
        loginpage.setusername("admin")
        log.info("Enter the valid password")
        loginpage.setpassword("manager")
        self.waitforsometime()

        log.info("Click on Login Button")
        loginpage.clickonloginbutton()

        adminstror = Administrator(self.driver)
        self.waitforsometime()

        log.info("Click On administror system")
        adminstror.click_on_administrator_system()
        self.waitforsometime()
        log.info("set email id")
        adminstror.set_email_id("konga@gmail.com")
        self.waitforsometime()
        adminstror.set_cureent_password("manager")
        self.waitforsometime()
        adminstror.set_new_password("manager")
        self.waitforsometime()
        adminstror.set_retype_password("manager")
        self.waitforsometime()
        adminstror.click_on_save_change()
        log.info("adminstror script executed successfully...")

