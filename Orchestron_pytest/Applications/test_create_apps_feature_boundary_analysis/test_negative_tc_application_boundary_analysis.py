import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from xpath.Application_module_xpath import *


'''
These func lets us check the negative test-cases of create application feature.
> First func checks for invalid url and its error message 
> second func checks for empty space in name field and its error message
> Third func checks for 'No value' in name field and its error message
> fourth function acts as a bait for 5th func to check if existing application is creating or not and if its not creating checks the error message.
'''


@mark.create_app_negative_tc
class ApplicationNegativeBoundaryValueAnalysisTcTests:
    def test_negative_tc_invalid_url(self, driver):
        applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        create_btn = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located((By.XPATH, app_create_button)))
        create_btn.click()

        name = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_name)))
        name.send_keys('!')

        url = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_url)))
        url.send_keys("http://!.com")

        platform_type = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_platform_type)))
        platform_type.send_keys("Python")
        platform_type.send_keys(Keys.ARROW_DOWN)
        platform_type.send_keys(Keys.ENTER)

        team = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_team)))
        team.click()
        # team.send_keys('Testing')
        # team.send_keys(Keys.ARROW_DOWN)
        # team.send_keys(Keys.ENTER)

        try:
            submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()

        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")

        if WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(),' * Enter a valid URL.')]"))).is_displayed():
            print('\nurl is invalid')
        else:
            print("\nurl is valid")
        time.sleep(2)
        close = WebDriverWait(driver, 5, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        # driver.quit()

    # def test_negative_tc_empty_space_in_name_field(self, driver):
    #     applicationTab = WebDriverWait(driver, 10, poll_frequency=3).until(
    #         EC.element_to_be_clickable((By.XPATH, application_tab)))
    #     applicationTab.click()
    #
    #     create_btn = WebDriverWait(driver, 10, poll_frequency=3).until(
    #         EC.presence_of_element_located((By.XPATH, app_create_button)))
    #     create_btn.click()
    #
    #     name = WebDriverWait(driver, 10, poll_frequency=1).until(
    #         EC.presence_of_element_located((By.XPATH, app_name)))
    #     name.send_keys(' ')
    #
    #     url = WebDriverWait(driver, 10, poll_frequency=1).until(
    #         EC.presence_of_element_located((By.XPATH, app_url)))
    #     url.send_keys("http://demo.com")
    #
    #     platform_type = WebDriverWait(driver, 10, poll_frequency=1).until(
    #         EC.presence_of_element_located((By.XPATH, app_platform_type)))
    #     platform_type.send_keys("Python")
    #     platform_type.send_keys(Keys.ARROW_DOWN)
    #     platform_type.send_keys(Keys.ENTER)

        # team = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, app_team)))
        # team.click()
        # team.send_keys('Testing')
        # team.send_keys(Keys.ARROW_DOWN)
        # team.send_keys(Keys.ENTER)

        # try:
        #     submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(
        #         EC.element_to_be_clickable((By.XPATH, app_submit)))
        #     submit_1.click()
        #
        # except (ElementClickInterceptedException, TimeoutException):
        #     print("submit button not visible")
        #
        # if WebDriverWait(driver, 10, poll_frequency=1).until(
        #         EC.presence_of_element_located((By.XPATH, "//p[contains(text(), ' * This field may not be blank.')]"))).is_displayed():
        #     print("'name' field or/and 'url' field is empty, these fields can't be empty please enter valid input")
        #
        # time.sleep(2)
        # close = WebDriverWait(driver, 5, poll_frequency=1).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "/html/body/div/div/div[2]/section/div/div[2]/div/div[1]/div/div/header/button")))
        # close.click()

    def test_negative_tc_no_value_in_name_field(self, driver):
        applicationTab = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        create_btn = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.presence_of_element_located((By.XPATH, app_create_button)))
        create_btn.click()

        name = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located(
                (By.XPATH, app_name)))
        name.send_keys('')

        url = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_url)))
        url.send_keys("http://demo.com")

        platform_type = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_platform_type)))
        platform_type.send_keys("Python")
        platform_type.send_keys(Keys.ARROW_DOWN)
        platform_type.send_keys(Keys.ENTER)

        # footer = WebDriverWait(driver, 10, poll_frequency=1).until(
        #     EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div/footer/div")))
        # footer.click()

        team = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_team)))
        team.click()
        # team.send_keys('Testing')
        # team.send_keys(Keys.ARROW_DOWN)
        # team.send_keys(Keys.ENTER)

        try:
            submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()

        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")

        close = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        time.sleep(2)

    def test_negative_tc_all_valid_inputs(self, driver):
        applicationTab = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        create_btn = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.presence_of_element_located((By.XPATH, app_create_button)))
        create_btn.click()

        name = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located(
                (By.XPATH, app_name)))
        name.send_keys('demo application')

        url = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_url)))
        url.send_keys("http://demo.com")

        platform_type = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_platform_type)))
        platform_type.send_keys("Python")
        platform_type.send_keys(Keys.ARROW_DOWN)
        platform_type.send_keys(Keys.ENTER)

        team = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_team)))
        team.click()
        # team.send_keys('Testing')
        # team.send_keys(Keys.ARROW_DOWN)
        # team.send_keys(Keys.ENTER)

        try:
            submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()

        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")

    def test_negative_tc_existing_app_name(self, driver):
        applicationTab = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        create_btn = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.presence_of_element_located((By.XPATH, app_create_button)))
        create_btn.click()

        name = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_name)))
        name.send_keys('demo application')

        url = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_url)))
        url.send_keys("http://demo.com")

        platform_type = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, app_platform_type)))
        platform_type.send_keys("Python")
        platform_type.send_keys(Keys.ARROW_DOWN)
        platform_type.send_keys(Keys.ENTER)

        team = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, app_team)))
        team.click()
        # team.send_keys('Testing')
        # team.send_keys(Keys.ARROW_DOWN)
        # team.send_keys(Keys.ENTER)

        try:
            submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()

        except (ElementClickInterceptedException, TimeoutException):
            print("\nsubmit button not visible")

        if WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(),' * application with this name already exists.')]"))).is_displayed():
            print("\nApplication with these name already existed")
        else:
            print("\nApplication is created")



