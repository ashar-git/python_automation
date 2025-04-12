import allure

def take_screen_shot(driver):
    allure.attach(driver.get_screenshot_as_png(),
                  attachment_type=allure.attachment_type.PNG)