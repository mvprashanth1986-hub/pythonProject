import pytest
from Old.POM.Loginpage import LoginPage
from Old.POM.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Login(BaseTest):

    def Login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME,TestData.PASSWORD)
