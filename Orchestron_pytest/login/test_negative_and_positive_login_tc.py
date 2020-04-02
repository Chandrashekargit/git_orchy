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
> These function lets us check login functionality with positive and negative credentials
> Note to self: For more info about param's: https://docs.pytest.org/en/latest/parametrize.html.
'''


@mark.login
class LoginNegativeTestCasesTests:
    @mark.parametrize('username, password', [
        ('chandrashekar@we45.com', 'Test@134'),   # Invalid PW
        ('chandrashekar@we45.com', 'test@1234'),  # checking case-sensitive for PW field
        ('chandrashekr@we45.com', 'Test@1234'),   # Invalid UN
        ('Chandrashekar@we45.com', 'Test@1234'),  # checking case-sensitive for UN
        ('chandra@we45.com', 'welcome@1234')      # Invalid PW, UN
    ])
    def test_login_warning_msg_for_invalid_credentials(self, username, password):
        """
        These function lets us test the warning message if we enter the invalid credentials.
        """
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

        warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_message1))).is_displayed()
        print(warning_msg)
        print("\nInvalid cred's")

        warning_msg1 = wait.until(EC.presence_of_element_located((By.XPATH, warning_message1))).text
        print(warning_msg1)

        close_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, close_warning_message1)))
        close_warning_msg.click()

        assert "Unable to log in with provided credentials." in warning_msg1
        driver.quit()

    @mark.parametrize('username, password', [
        (' ', 'Test@1234'),                 # Email is empty
        ('chandrashekar@we45.com', ' '),    # Password is empty
        (' ', ' ')                          # Both are empty.
    ])
    def test_login_warning_msg_for_empty_fields(self, username, password):
        """
        These function lets us test the warning message if one of them (username/email and password) or both fields
        are empty.
        """
        driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)

        email = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
        email.clear()
        email.send_keys(username)
        pw = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
        pw.clear()
        pw.send_keys(password)
        login = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
        login.click()
        time.sleep(2)

        WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, warning_message2))).is_displayed()
        print("\nemail or PW field can't be empty")
        warning_msg2 = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, warning_message2))).text
        assert warning_msg2 == "* This field may not be blank."
        driver.quit()

    @mark.parametrize('username, password', [
        ('chandrashekar@we45.com', 'Test@1234')
    ])
    def test_login_for_valid_credentials(self, username, password):
        """
        These function lets us test with valid credentials and asserts the URL.
        """
        driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)

        email = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
        email.clear()
        email.send_keys(username)
        pw = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
        pw.clear()
        pw.send_keys(password)
        login = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
        login.click()
        time.sleep(2)
        assert driver.current_url == url + 'org/dashboard'
