import allure
import pytest
import time

from selenium import webdriver
from test.utils.Utils import *

#Script Flow
#Webdriver start
#user interaction = Assertiond
#close webdriver

from test.constants.constants import Constants
from test.pageObjects.PageObjectModel.vwo.loginPage import LoginPage
from test.pageObjects.PageObjectModel.vwo.dashboardPage import DashboardPage
from dotenv import load_dotenv
import os


@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.title("VWO Login Test")
@allure.description("TC#01 - vwo App Negative test")
@allure.feature("Feature | vwo app negative test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver=setup
    login_page=LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("INVALID_USERNAME"), pwd=os.getenv("INVALID_PASSWORD"))
    error_message=login_page.get_error_message_text()
    take_screen_shot(driver=driver, name = "screenshot_1")
    assert error_message == os.getenv("error_message_expected")


@allure.title("VWO Login Test")
@allure.description("TC#02 - vwo App positive test")
@allure.feature("Feature | vwo app positive test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver=setup
    driver.get(Constants.app_url())
    login_page=LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("USERNAME_VWO"), pwd=os.getenv("PASSWORD_VWO"))
    dashboard_page=DashboardPage(driver=driver)
    take_screen_shot(driver=driver, name= "screenshot_2")
    assert os.getenv("USERNAME_LOGGED_IN") in dashboard_page.user_logged_in_text()

