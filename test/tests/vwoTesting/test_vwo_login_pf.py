import time
import pytest
import selenium
import allure
import logging

from selenium import webdriver
from test.pageObjects.PageFactory.loginpage_pagefactory import LoginPage
from test.pageObjects.PageFactory.Dashboard_pagefactory import DashboardPage
from test.constants.constants import Constants
from test.tests.vwoTesting.conftest import *

@allure.epic("VWO App")
@allure.feature("PF Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self,setup):
        try:
            LOGGER = logging.getLogger("__name__")
            driver = setup
            driver.get(Constants.app_url())
            loginpage = LoginPage(driver)
            loginpage.login_to_vwo(usr=self.username,pwd=123)
            error_msg_element = loginpage.error_msg()
            assert error_msg_element == "Your email, password, IP address or location did not match"
        except Exception as e:
            print(e)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_dshboard_page_positive(self,setup):
        driver = setup()
        driver.get(Constants.app_url())
        loginpage = LoginPage(driver)
        loginpage.login_to_vwo(usr=self.username, pwd=self.password)
        dashboardpage = DashboardPage(driver)
        username = dashboardpage.get_user_logged_in_text()
        assert "Aman" == username





