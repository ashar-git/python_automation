import time
from selenium import  webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from test.utils.Utils import *
import os


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO login with invalid credentials")
@allure.feature("VWO login with invalid credentials")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    match os.getenv("BROWSER"):
        case "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(chrome_options)
        case "edge":
            edge_options = Options()
            edge_options.add_argument("--inprivate")
            driver = webdriver.Edge(edge_options)
        case "firefox":
            firefox_options = Options()
            firefox_options.add_argument("-private")
            driver = webdriver.Firefox(firefox_options)
        case _:
            print("Browser not found")
            exit(1)

    driver.get(os.getenv("url"))
    email_web_element=driver.find_element(By.ID,"login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    password_web_element=driver.find_element(By.NAME,"password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    login_btn_web_element=driver.find_element(By.ID,"js-login-btn")
    login_btn_web_element.click()

    time.sleep(3)

    error_msg_notification=driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_notification.text)

    take_screen_shot(driver=driver)
    assert error_msg_notification.text == os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit()




