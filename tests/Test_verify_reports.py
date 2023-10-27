
from utilities.base import BaseClass

from pageObjects.LoginPage import LoginPage
from pageObjects.Logout import Logout
from pageObjects.Reports import Reports


class Test_Verify_Export_CSV_Reports(BaseClass):

    def test_verify_reports(self):
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforsometime()
        loginpage.clickonloginbutton()
        self.waitforsometime()

        reports = Reports(self.driver)
        self.waitforsometime()
        reports.clcikonreport()
        self.waitforsometime()
        reports.clcikoncreatereport()
        self.waitforsometime()
        reports.clcikonconfigurereport()
        self.waitforsometime()
        reports.clcikongeneratereport()
        self.waitforsometime()
        reports.clcikonexportcsvreport()

        logout = Logout(self.driver)
        self.waitforsometime()
        logout.clickonlogoutbutton()
        self.waitforsometime()

