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
def test_shadow_dom_using_js_executor():
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("--incognito")
    driver = webdriver.Chrome(chromeoptions)
    driver.get("https://selectorshub.com/xpath-practice-page")
    driver.maximize_window()
    username_div = driver.find_element(By.XPATH,"//div[@id='userName']")
    driver.execute_script("arguments[0].scrollIntoView(true);",username_div)
    #To go into shadow DOM element
    input_box = driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector("
                                      "'#app2').shadowRoot.querySelector('#pizza');")
    input_box.send_keys("farmhouse")
    time.sleep(5)
    driver.quit()
