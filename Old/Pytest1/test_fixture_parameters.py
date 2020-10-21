import pytest
from selenium import webdriver
import time


@pytest.fixture(params=["chrome","firefox"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.firefox(executable_path="C:\pythonutils\chromedriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.quit()

@pytest.mark.usefixtures("init_driver")
class Base_Class:
    pass

@pytest.mark.parametrize("username,password"[("automation","password0"),("manual testing","password1"),("api"),("password2")])
class Test_Google(Base_Class):
    def test_Google_Title(self):
        self.driver.get("http://www.google.com")
        print(self.driver.title)
        assert self.driver.title == "Google"