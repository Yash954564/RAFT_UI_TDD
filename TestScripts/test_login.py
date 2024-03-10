import pytest


from PageObjects.Logins import LoginPaged
from TestScripts.BaseTest import BaseTest
from Utilities import data_reader



class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address, password",data_reader.get_data_from_excel("TestData/data.xlsx", "LoginTest"))
    def test_login_with_valid_credentials(self, email_address, password):
        login_page = LoginPaged(self.driver)
        login_page = login_page.login_to_application(email_address,password)