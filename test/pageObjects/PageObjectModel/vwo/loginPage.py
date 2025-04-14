import pytest
import allure
from selenium.webdriver.common.by import By
from test.utils.commn_utils import webdriver_wait
import time


class LoginPage:
    vwo_username = (By.XPATH, "//input[@id='login-username']")
    vwo_password = (By.XPATH, "//input[@id='login-password']")
    submit_btn = (By.XPATH, "//button[@id='js-login-btn']")
    error_msg = (By.XPATH, "//div[@id='js-notification-box-msg']")

    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(*LoginPage.vwo_username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.vwo_password)

    def get_submit_btn(self):
        return self.driver.find_element(*LoginPage.submit_btn)

    def get_error_msg(self):
        webdriver_wait(driver=self.driver,element_tuple=self.error_msg,timeout=5)
        return self.driver.find_element(*LoginPage.error_msg)

    def login_to_vwo(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_btn().click()
        except Exception as e:
            print(e)

    def get_error_message_text(self):
        webdriver_wait(driver=self.driver,element_tuple=self.error_msg,timeout=5)
        return self.get_error_msg().text






