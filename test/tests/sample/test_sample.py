import pytest
import allure
import time

from selenium import webdriver


@allure.title("dry run of the framework 1")
@allure.description("verify that dry run is working 1")
@allure.feature("TC#0 - Sample Test Run")
@pytest.mark.sample
def test_sample_pass():
    print("Hello sample")
    assert True == True


@allure.title("dry run of the framework 2")
@allure.description("verify that dry run is working 2")
@allure.feature("TC#1 - Sample Test Run")
@pytest.mark.sample
def test_sample_fail():
    print("Hello sample")
    assert True == False
