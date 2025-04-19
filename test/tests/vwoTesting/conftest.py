import os

from selenium import webdriver
from selenium.webdriver import Chrome
import pytest

from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Edge()


@pytest.fixture(scope='class')
def setup(request):
    driver.maximize_window()
    username = os.getenv("USERNAME_VWO")
    password = os.getenv("PASSWORD_VWO")

    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password

    yield driver
    driver.quit()







