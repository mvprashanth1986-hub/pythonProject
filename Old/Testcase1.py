import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def test1_google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://testautomationpractice.blogspot.com/")
        print("My first case")
        self.driver.quit()

    def test2_google1(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://testautomationpractice.blogspot.com/")
        print("My second case")

if __name__ == "__main__":
    unittest.main()

