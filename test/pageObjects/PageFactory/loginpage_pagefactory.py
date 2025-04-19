# page locators
# page actions

from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from test.utils.commn_utils import WebDriverWait


class LoginPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.highlight = True

    locators = {
        "username": ("XPATH", "//input[@id='login-username']"),
        "password": ("XPATH", "//input[@id='login-password']"),
        "submit_button": ("XPATH", "//button[@id='js-login-btn']"),
        "error_message": ("XPATH", "//div[@id='js-notification-box-msg']")
    }
