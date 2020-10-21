import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def init_driver(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.quit()