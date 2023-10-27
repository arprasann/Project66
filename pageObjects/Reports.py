from selenium.webdriver.common.by import By

from utilities.base import BaseClass

class Reports(BaseClass):

    report = (By.XPATH,"//div[text()='Reports']")

    createReport = (By.XPATH,"//span[text()='Create Report']")

    configurereport = (By.ID,"configureReportParametersButton")

    generatereport = (By.ID,"generateReport")

    exportcsvreport = (By.ID, "exportToCsv")

    def __init__(self,driver):
        self.driver = driver

    def clcikonreport(self):
        self.verify_element_clickable(By.XPATH,"//div[text()='Reports']")
        return self.driver.find_element(*Reports.report).click()

    def clcikoncreatereport(self):
        self.verify_element_clickable(By.XPATH,"//span[text()='Create Report']")
        return self.driver.find_element(*Reports.createReport).click()

    def clcikonconfigurereport(self):
        self.verify_element_clickable(By.ID,"configureReportParametersButton")
        return self.driver.find_element(*Reports.configurereport).click()

    def clcikongeneratereport(self):
        self.verify_element_clickable(By.ID,"generateReport")
        return self.driver.find_element(*Reports.generatereport).click()

    def clcikonexportcsvreport(self):
        self.verify_element_clickable(By.ID, "exportToCsv123")
        return self.driver.find_element(*Reports.exportcsvreport).click()