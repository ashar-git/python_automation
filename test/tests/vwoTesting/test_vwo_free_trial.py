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
from test.pageObjects.PageObjectModel.vwo.freeTrial import FreeTrialPage
from dotenv import load_dotenv
import os


@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.title("VWO Free Trial")
@allure.description("TC#01 - vwo Free Trial test")
@allure.feature("Feature | vwo Free Trial test")
@pytest.mark.negative
def test_vwo_ft_negative(setup):
    driver=setup
    login_page=LoginPage(driver=driver)
    login_page.free_trial_btn_click()
    take_screen_shot(driver=driver, name="test_vwo_ft_negative")
    free_trial_page = FreeTrialPage(driver=driver)
    free_trial_page.enter_free_trial_details_invalid(invalid_email="admin")
    error_msg_text = free_trial_page.get_error_msg_invalid_email_text()
    assert error_msg_text == "The email address you entered is incorrect."


