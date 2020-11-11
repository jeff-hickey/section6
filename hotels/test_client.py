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
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1280, 711)
        # Look for the correct label and go to login.
        login = self.driver.find_element(By.ID, "login_first")
        assert login.text == "Please Login to search."
        login.click()
        # Find and populate the login form, then login.
        self.driver.find_element(By.NAME, "username").send_keys("test")
        self.driver.find_element(By.NAME, "password").send_keys("test")
        self.driver.find_element(By.NAME, "login").click()

        # Perform a search for hotels.
        self.driver.find_element(By.NAME, "keyword").send_keys("comfort")
        self.driver.find_element(By.NAME, "search").click()

        # Select a room and book.
        self.driver.find_element(By.ID, "rooms-1").click()
        self.driver.find_element(By.ID, "book").click()
        assert self.driver.switch_to.alert.text == "Thank you. Room is booked."
        print('Selenium Client: OK')


if __name__ == "__main__":
    unittest.main()
