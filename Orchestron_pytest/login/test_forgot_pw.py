import pytest
import time
from pytest import mark
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.login_xpath import *
from xpath.Application_module_xpath import *


@mark.forgot_pw
def test_for_warning_message_when_invalid_email_entered():
    """
    These function lets us check the warning message when we enter the invalid email (not registered with orchy).
    """
    driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    forgot_pw = wait.until(EC.element_to_be_clickable((By.XPATH, forgot_password)))
    assert forgot_pw.text == "Forgot Password ?"
    forgot_pw.click()

    enter_email_to_receive_pw_reset_link = wait.until(EC.element_to_be_clickable((By.XPATH, enter_email)))
    enter_email_to_receive_pw_reset_link.send_keys("Orchydemo1@we45.com")

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, submit_btn)))
    submit.click()
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
    warning_message = wait.until(EC.element_to_be_clickable((By.XPATH, warning_message3))).text
    assert "* Please Provide Valid Email" in warning_message
    driver.quit()

# please make sure to check with valid email manually. Not written script coz if we enter the valid email and click
# submit, we gonna receive a re-set pw link and existing account will be revoked (its a pain).

