import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSelenium:
    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.chromeoptions = webdriver.ChromeOptions()
        self.chromeoptions.add_argument("--incognito")
        self.driver = webdriver.Chrome(self.chromeoptions)
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.maximize_window()

    def test_js(self):
        title = self.driver.execute_script("return document.title")
        current_url = self.driver.execute_script("return document.URL")
        print(title)
        print(current_url)

    def close_browser(self):
        time.sleep(3)
        self.driver.quit()


test = TestSelenium()
test.open_browser()
test.test_js()
test.close_browser()