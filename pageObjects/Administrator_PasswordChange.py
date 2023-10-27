from selenium.webdriver.common.by import By
from utilities.base import BaseClass
from selenium.webdriver.common.keys import Keys

class Administrator(BaseClass):

    administrator = (By.XPATH,"//a[contains(text(),'Administrator')]")
    email_field = (By.ID,"userProfilePopup_emailField")
    currentpassword= (By.ID,"userProfilePopup_oldPasswordField")
    newpassword = (By.ID,"userProfilePopup_passwordField")
    retypepassword = (By.ID,"userProfilePopup_passwordCopyField")
    savechanges  = (By.ID,"userProfilePopup_commitBtn")


    def __init__(self,driver):
        self.driver = driver

    def click_on_administrator_system(self):
        return self.driver.find_element(*Administrator.administrator).click()

    def set_email_id(self,email2):
        self.waitforsometime()
        self.driver.find_element(*Administrator.email_field).send_keys(Keys.CONTROL+"a",Keys.DELETE)
        self.waitforsometime()
        self.driver.find_element(*Administrator.email_field).send_keys(email2)


    def set_cureent_password(self,cpw):
        self.waitforsometime()
        self.driver.find_element(*Administrator.currentpassword).send_keys(cpw)


    def set_new_password(self,npw):
        self.waitforsometime()
        self.driver.find_element(*Administrator.newpassword).send_keys(npw)



    def set_retype_password(self,rpw):
        self.waitforsometime()
        self.driver.find_element(*Administrator.retypepassword).send_keys(rpw)


    def click_on_save_change(self):
        return self.driver.find_element(*Administrator.savechanges).click()

