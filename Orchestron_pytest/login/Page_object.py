import time
from pytest import mark
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.login_xpath import *
from xpath.Application_module_xpath import *


class PageObjectForLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
        self.url = url

    def go(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def wait(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    def enter_email_or_username(self, email_id):
        email = self.wait.until(EC.presence_of_element_located((By.XPATH, email_xpath)))
        email.clear()
        email.send_keys(email_id)

    def enter_password(self, password):
        pw = self.wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
        pw.clear()
        pw.send_keys(password)

    def click_login_btn(self):
        login = self.wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
        login.click()
