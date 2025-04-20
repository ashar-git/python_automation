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


@allure.title("Automatic Scroll Executor")
@allure.description("Verify Automatic Scroll")
def test_verify_automatic_scroll():
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("--incognito")
    driver = webdriver.Chrome(chromeoptions)
    driver.get("https://selectorshub.com/xpath-practice-page")
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(5)
    driver.quit()
