import os

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from OrangeHRM_Project.businessFunctions.HomePageBFs import *
import unittest


class LoginTestCases(unittest.TestCase):
    #cap = DesiredCapabilities().FIREFOX
    #cap["marionette"] = False
    #driver = webdriver.Firefox(capabilities=cap, executable_path=r'F://PythonSelenium/pythonSeleniumProject/drivers/geckodriver.exe')

    driver = webdriver.Chrome(executable_path=r'F:/PythonSelenium/pythonSeleniumProject/drivers/chromedriver.exe')

    @classmethod
    def setUp(self):
        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.google.com")

    def tearDown(self):
        self.driver.close()
        print("\n Test case completed successfully")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
