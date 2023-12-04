from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time



desired_capabilities = {
        "platformName": "Android",
        "appium:appPackage": "ru.vtb.msse",
        "appium:appActivity": "ru.vtb.msse.MainActivity",
        "appium:app": "/Users/dmitry/Desktop/app-1.11.0-730-ift-public-debug.apk",
        "appium:deviceName": "Pixel 7",
        "appium:platformVersion": "13.0",
        "appium:automationName": "Appium"
    }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

@pytest.fixture
def setup():
    driver.start_session(desired_capabilities)
    time.sleep(2)
    driver.find_element(By.ID, 'ru.vtb.msse:id/login_edit_text').click()
    return driver

a = b
