from selenium.webdriver.common.by import By
import time
import pytest
from conftest import driver



@pytest.mark.usefixtures('setup')
class TestFirst:
    def testsetup_method(self):
        time.sleep(2)
        driver.find_element(By.ID, 'ru.vtb.msse:id/password_edit_text').click()
