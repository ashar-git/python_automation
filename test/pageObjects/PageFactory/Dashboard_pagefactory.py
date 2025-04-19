import time
from seleniumpagefactory.Pagefactory import PageFactory
from test.utils.commn_utils import *

class DashboardPage(PageFactory):
    def __init__(self, driver):
        # super().__init__()
        self.driver = driver
        self.highlight = True

    locators = {
        "username_logged_in" : ("XPATH", "//span[@data-qa='lufexuloga']")
    }

    def get_user_logged_in_text(self):
        webdriver_wait(driver=self.driver,timeout=10)
        return self.username_logged_in.get_text()



