import pytest
from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome()
    driver.get("http://www.facebook.com")
    assert driver.title == "Facebook"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome()
    driver.get("http://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome()
    driver.get("http://www.gmail.com")
    assert driver.title == "Gmail"
    driver.quit()
