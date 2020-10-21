import unittest
from selenium import webdriver

class Assert_equal(unittest.TestCase):
    def test_asserttrue(self):
        driver = webdriver.Chrome()
        driver.get("http://www.google.com")
        title = driver.title
        self.assertLess()
        self.assertLessEqual()

if __name__ ==  "main":
    unittest.main()