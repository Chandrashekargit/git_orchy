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


def login_orchy(username=None, password=None):
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
