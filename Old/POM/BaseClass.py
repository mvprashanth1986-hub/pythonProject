import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,loc):
        loc.click()

    def send_keys(self,loc,text):
        loc.send_keys(text)

    def get_element_text(self,loc):
        return loc.text

    def is_enabled(self,loc):
        ele = loc.is_enabled()
        return bool(ele)

    def get_title(self,title):
        return self.driver.title



