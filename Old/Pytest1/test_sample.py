import pytest
from selenium import webdriver
import time

@pytest.fixture(scope='class')
def init_driver(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.quit()

@pytest.mark.usefixtures("init_driver")
class Base_Class:
    pass

class Test_Google(Base_Class):
    def test_Google_Title(self):
        self.driver.get("http://www.google.com")
        print(self.driver.title)
        assert self.driver.title == "Google"