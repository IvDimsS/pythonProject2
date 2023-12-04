from appium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


'''
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


driver.implicitly_wait(5)

driver.find_element(By.ID, 'ru.vtb.msse:id/edit_text_login_username').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/edit_text_login_username').send_keys(input())

driver.find_element(By.ID, 'ru.vtb.msse:id/edit_text_login_username').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/edit_text_login_password').set_text('A1s1d112131415141312!!')

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_login_enter').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_2').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_6').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_7').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_8').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_2').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_6').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_7').click()

driver.find_element(By.ID, 'ru.vtb.msse:id/btn_num_8').click()

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[1]/android.view.View").click()

driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[10]/android.view.View[2]").click()
'''

'''
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


class TestFirst:
    def load():
        desired_capabilities

    def test_01(self):
        time.sleep(3)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.EditText/android.widget.TextView[1]").click()

    def test_02(self):
        time.sleep(3)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.widget.EditText/android.widget.TextView[1]").click()
        time.sleep(3)

    def teardown_method(self):
        driver.quit()
'''
