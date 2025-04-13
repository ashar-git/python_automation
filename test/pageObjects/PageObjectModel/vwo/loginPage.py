import pytest
import allure
from selenium.webdriver.common.by import By
from test.utils.commn_utils import webdriver_wait


class LoginPage:
    vwo_username = (By.XPATH, "//input[@id='login-username']")
    vwo_password = (By.XPATH, "//input[@id='login-password']")
    submit_btn = (By.XPATH, "//button[@id='js-login-btn']")
    error_msg = (By.XPATH, "//div[@id='js-notification-box-msg']")

    def __init__(self, driver):
        self.driver = driver

    def getusername(self):
        return self.driver.find_element(*LoginPage.vwo_username)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.vwo_password)

    def getsubmitbtn(self):
        return self.driver.find_element(*LoginPage.submit_btn)

    def get_error_msg(self):
        return self.driver.find_element(*LoginPage.error_msg)

    def get_error_message_text(self):
        webdriver_wait(driver=self.driver,element_tuple=self.error_msg,timeout=5)
        return self.get_error_msg().text






