import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
from xpath.Application_module_xpath import *
from Applications.test_delete_application.delete_app import delete_app


@mark.create_app_negative_tc
class ApplicationNegativeBoundaryValueAnalysisTcTests:
    def create_app(self, driver, name_value=None, url_value=None):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException
        ])
        wait1 = WebDriverWait(driver, 5, poll_frequency=1)
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, app_create_button)))
        create_btn.click()

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        name = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        name.clear()
        name.send_keys(name_value)

        url = wait.until(EC.element_to_be_clickable((By.XPATH, app_url)))
        url.clear()
        url.send_keys(url_value)

        platform_type = wait.until(EC.element_to_be_clickable((By.XPATH, app_platform_type)))
        platform_type.clear()
        platform_type.send_keys("Python")
        platform_type.send_keys(Keys.ARROW_DOWN)
        platform_type.send_keys(Keys.ENTER)

        team = wait.until(EC.element_to_be_clickable((By.XPATH, app_team)))
        team.click()
        # team.send_keys('Testing')
        # team.send_keys(Keys.ARROW_DOWN)
        # team.send_keys(Keys.ENTER)

    def test_negative_tc_invalid_url(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        self.create_app(driver, name_value="!", url_value="http://!.com")
        try:
            submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()
        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")

        if wait.until(EC.presence_of_element_located((By.XPATH, invalid_url_wrng_msg))).is_displayed():
            print('\nurl is invalid')
        else:
            print("\nurl is valid")
        time.sleep(2)
        close = wait.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()

    def test_negative_tc_no_value_in_name_field(self, driver):
        wait1 = WebDriverWait(driver, 5, poll_frequency=1)
        self.create_app(driver, name_value=" ", url_value="http://demo.com")
        try:
            submit_1 = wait1.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()
        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")
        close = wait1.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        time.sleep(2)

    def test_negative_tc_no_value_in_url_field(self, driver):
        wait1 = WebDriverWait(driver, 5, poll_frequency=1)
        self.create_app(driver, name_value="Demo", url_value=" ")
        try:
            submit_1 = wait1.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()
        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")

        close = wait1.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        time.sleep(2)

    def test_negative_tc_all_valid_inputs(self, driver):
        wait1 = WebDriverWait(driver, 5, poll_frequency=1)
        self.create_app(driver, name_value="demo application", url_value="http://demo.com")
        try:
            submit_1 = wait1.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()
        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")
        success_msg = wait1.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Application has been created successfully!']")))
        if success_msg.is_displayed():
            print("Application has been created successfully!")

    def test_negative_tc_existing_app_name(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        self.create_app(driver, name_value="demo application", url_value="http://demo.com")
        try:
            submit_1 = wait.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()
        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")

        if wait.until(EC.presence_of_element_located((By.XPATH, existing_application_warning_msg))).is_displayed():
            print("\nApplication with these name already existed")
        else:
            print("\nApplication is created")
        close = wait.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        time.sleep(2)

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'demo application')]")  # calling the function 'delete_app'
