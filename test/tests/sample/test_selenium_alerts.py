import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("ALerts")
@allure.description("Verify JS Alert")
def test_selenium_js_alert():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    element_prompt = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert = driver._switch_to.alert
    alert.accept()
    result_text = driver.find_element(By.ID,"result").text
    assert result_text == "You successfully clicked an alert"
    time.sleep(5)


def test_selenium_js_confirm():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    element_prompt = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert = driver._switch_to.alert
    alert.dismiss()
    result_text = driver.find_element(By.ID,"result").text
    assert result_text == "You clicked: Cancel"
    time.sleep(5)

def test_selenium_js_prompt():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    element_prompt = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert = driver._switch_to.alert
    alert.send_keys("waquar")
    alert.accept()
    result_text = driver.find_element(By.ID,"result").text
    assert result_text == "You entered: ahmad"
    time.sleep(5)

