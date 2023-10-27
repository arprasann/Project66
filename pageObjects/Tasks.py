from selenium.webdriver.common.by import By

from utilities.base import BaseClass

class Tasks(BaseClass):

    task = (By.XPATH,"//div[text()='Tasks']")
    filtertaskByName = (By.NAME,"visiableFilterString")
    applyFilter = (By.ID,"tasksFilterSubmitButton")

    def __init__(self,driver):
        self.driver = driver

    def clickonTask(self):
        self.verify_element_clickable(By.XPATH,"//div[text()='Tasks']")
        return self.driver.find_element(*Tasks.task).click()

    def sendtextfiltertaskbyName(self,text):
        return self.driver.find_element(*Tasks.filtertaskByName).send_keys(text)

    def clcikonapplyfilter(self):
        return self.driver.find_element(By.XPATH,"rrrrr").click()

