from Old.POM.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class LoginPage(BaseClass):

    EMAIL = (By.ID,"username")
    PASSWORD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"LoginBtn")
    SIGN_UP_LINK = (By.LINK_TEXT,"Sign up")

    def __int__(self,driver):
        super().__init__(driver)

    def do_login(self,username,password):
        self.send_keys(self.EMAIL,username)
        self.send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)