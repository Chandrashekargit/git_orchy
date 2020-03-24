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
from xpath.Engagement_module_xpath import *


@mark.engagement_boundary_value_analysis_negative
class EngagementNegativeBoundaryValueAnalysisTcTests:
    def test_negative_tc_empty_space_in_name_field(self, driver):
        eng_tab = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, Engagement_tab)))
        eng_tab.click()

        create_btn = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, eng_create_btn)))
        create_btn.click()

        name = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, eng_name)))
        name.send_keys(' ')

        desc = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, eng_desc)))
        desc.send_keys('*' * 200)

        eng_date = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, eng_date_btn)))
        eng_date.click()
        eng_date_popup1 = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][1]//td[@class='curMonth today']")))
        eng_date_popup1.click()
        eng_date_popup2 = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][2]//td[@title='28/02/2020']")))
        eng_date_popup2.click()

        bucket_type = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, eng_bucket_type)))
        bucket_type.click()
        bucket_type.send_keys("All")
        bucket_type.send_keys(Keys.ARROW_DOWN)
        bucket_type.send_keys(Keys.ENTER)

        app_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, eng_app_dropdown)))
        app_dropdown.send_keys("SCA")
        app_dropdown.send_keys(Keys.ARROW_DOWN)
        app_dropdown.send_keys(Keys.ENTER)

        try:
            submit = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, eng_submit)))
            submit.click()

        except (ElementClickInterceptedException, TimeoutException):
            print('submit button not visible')

        if WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, "//p[text()=' * This field may not be blank.']"))).is_displayed():
            print('\nName field cant be empty, please enter valid name')




