# Generated by Selenium IDE
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWholeFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_wholeFlow(self):
        print('Selenium Client: Unknown.')


if __name__ == "__main__":
    unittest.main()
