from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.base import BaseClass

class Create_Users(BaseClass):

    users = (By.XPATH,"//div[text()='Users']")
    user = (By.XPATH, "//span[text()='User']")
    firstname = (By.NAME, "firstName")
    lastname = (By.NAME, "lastName")
    email = (By.NAME, "email")
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    reenterpassword = (By.NAME, "passwordCopy")


    def __init__(self,driver):
        self.driver = driver

    def click_On_Users(self):
        return self.driver.find_element(*Create_Users.users).click()



    def click_On_User(self):
        return self.driver.find_element(*Create_Users.user).click()

    def set_first_name(self,fn):
        return self.driver.find_element(*Create_Users.firstname).send_keys(fn)

    def set_last_name(self,ln):
        return self.driver.find_element(*Create_Users.lastname).send_keys(ln)

    def set_email(self,email1):
        return self.driver.find_element(*Create_Users.email).send_keys(email1)

    def set_user_name(self,un):
        return self.driver.find_element(*Create_Users.username).send_keys(un)

    def set_password(self,pw):
        return self.driver.find_element(*Create_Users.password).send_keys(pw)

    def set_reenter_password(self,rpw):
        return self.driver.find_element(*Create_Users.reenterpassword).send_keys(rpw)

