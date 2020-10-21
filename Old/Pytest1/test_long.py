import pytest
from selenium import webdriver
import time

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    yield
    driver.quit()

def test_url(init_driver):
    time.sleep(5)
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"

@pytest.mark.usefixtures("init_driver")
def test_title():
    time.sleep(5)
    assert driver.title == "Google"
