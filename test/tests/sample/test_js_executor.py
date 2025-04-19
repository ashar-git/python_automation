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


@allure.title("JS Executor")
@allure.description("Verify JS Executor")
def test_verify_JS_Executor():
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("--incognito")
    driver = webdriver.Chrome(chromeoptions)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    driver.execute_script("alert(1)")
    time.sleep(5)
    driver.quit()
