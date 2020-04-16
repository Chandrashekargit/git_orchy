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

'''
> Note to self: For more info about param's: https://docs.pytest.org/en/latest/parametrize.html.
'''

usernames = ['chandrashekar@we45.com', 'chandrashekar@we45.com', 'chandrashekr@we45.com', 'Chandrashekar@we45.com',
             'chandra@we45.com', ' ', 'chandrashekar@we45.com', ' ', 'chandrashekar@we45.com']

passwords = ['Test@134', 'test@134', 'Test@1234', 'Test@1234', 'welcome@1234', 'Test@1234', ' ', ' ', 'Test@1234']


@mark.login
def test_login_warning_msg_for_invalid_credentials():
    """
    These function lets us test the warning message if we enter the invalid credentials, if we leave any fields empty.
    """
    for (username, password) in zip(usernames, passwords):
        driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
        # Enter the email, password and click on submit button.
        email = wait.until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
        email.clear()
        email.send_keys(username)
        pw = wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
        pw.clear()
        pw.send_keys(password)
        login = wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
        login.click()
        time.sleep(2)
        # Invalid pw, check for case sensitive in pw field, invalid un, check for case sensitive in un field,
        # invalid pw and invalid un.
        if username == 'chandrashekar@we45.com' and password == 'Test@134' or \
           username == 'chandrashekar@we45.com' and password == 'test@134' or \
           username == 'chandrashekr@we45.com' and password == 'Test@1234' or \
           username == 'Chandrashekar@we45.com' and password == 'Test@1234' or \
           username == 'chandra@we45.com' and password == 'welcome@1234':
            warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_message1))).is_displayed()
            print(warning_msg)
            print("\nInvalid cred's")

            warning_msg1 = wait.until(EC.presence_of_element_located((By.XPATH, warning_message1))).text
            print(warning_msg1)

            close_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, close_warning_message1)))
            close_warning_msg.click()

            assert "Unable to log in with provided credentials." in warning_msg1
            driver.quit()
        # check for blank username field, check for blank password field, both fields blank,
        elif username == ' ' and password == 'Test@1234' or username == 'chandrashekar@we45.com' and \
                password == ' ' or username == ' ' and password == ' ':
            WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, warning_message2))).is_displayed()
            print("\nemail or PW field can't be empty")
            warning_msg2 = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, warning_message2))).text
            assert warning_msg2 == "* This field may not be blank."
            driver.quit()
        # valid cred's
        elif username == 'chandrashekar@we45.com' and password == 'Test@1234':
            assert driver.current_url == url + 'org/dashboard'
