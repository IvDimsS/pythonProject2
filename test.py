from appium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from capabilities import desired_capabilities
from capabilities import driver


'''class TestFirst:
    def setup_method(self):
        driver.start_session(desired_capabilities)

    def test_01(self):
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.EditText/android.widget.TextView[1]").click()
        expected_text = "Добро\nпожаловать!"
        actual_text = driver.find_element(By.CLASS_NAME, 'android.widget.TextView').text
        assert expected_text == actual_text, f'NOOOOOOOOOOOOOOO'

    def test_02(self):
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.widget.EditText/android.widget.TextView[1]").click()
        driver.find_element(By.ID, 'ru.vtb.msse:id/login_edit_text').click()'''
