import time
import unittest

from unittestzero import Assert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options



class FirstAutomationTests(unittest.TestCase):

    if __name__ == "__main__":
        unittest.main()

    def install_webdriver(self):
        driver = webdriver.Edge()
        driver.get("https://www.google.com/")

    def setUp(self):
        self.edge_options = Options()
        self.edge_options.add_experimental_option("detach", True)
        self.edge_options.add_argument("==profile-directory=Default")
        self.browser = webdriver.Edge(options=self.edge_options)
        self.base_url = 'https://www.google.com'


    def test_gmail_button(self):
        self.browser.get(self.base_url)
        search_input = self.browser.find_element(By.CLASS_NAME, 'gb_v')
        search_input.click()
        URL = self.browser.current_url
        Assert.not_none(URL)


    def tearDown(self):
        time.sleep(30)
        self.browser.close()


