import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from xpath.Application_module_xpath import *


@mark.create_app_positive_tc
@mark.parametrize('app, url_field', [
                  ('!@#$%^&*() 1234567890! createapp with alphanum,spl', 'http://demo.com'),
                  ('1234567890', 'http://demo.com'),
                  ('D', 'http://D.com'),
])
def test_positive_tc_application_Boundary_value_analysis(driver, app, url_field):
    applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
    EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    create_btn = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.presence_of_element_located((By.XPATH, app_create_button)))
    create_btn.click()

    name = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.presence_of_element_located(
            (By.XPATH, app_name)))
    name.send_keys(app)

    url = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.presence_of_element_located((By.XPATH, app_url)))
    url.send_keys(url_field)

    platform_type = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.presence_of_element_located((By.XPATH, app_platform_type)))
    platform_type.send_keys("Python")
    platform_type.send_keys(Keys.ARROW_DOWN)
    platform_type.send_keys(Keys.ENTER)

    select_team = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, app_team)))
    select_team.click()

    submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, app_submit)))
    submit_1.click()



