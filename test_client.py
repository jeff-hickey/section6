# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestWholeFlow():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_wholeFlow(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1280, 711)
        self.driver.find_element(By.NAME, "keyword").click()
        self.driver.find_element(By.NAME, "keyword").send_keys("toronto")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "<< Back to Hotel List").click()
        self.driver.find_element(By.NAME, "keyword").click()
        element = self.driver.find_element(By.NAME, "keyword")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "keyword").send_keys("comfort")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "View Rooms >>").click()
        self.driver.find_element(By.ID, "book").click()
        assert self.driver.switch_to.alert.text == "Thank you. Room is booked."
