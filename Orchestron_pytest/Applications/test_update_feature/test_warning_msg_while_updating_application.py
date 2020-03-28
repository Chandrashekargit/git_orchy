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


@mark.update_app_and_check_all_warning_msgs
def test_warning_messaege_while_updating_application(driver, create_app):
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementClickInterceptedException,
                                                                           ElementNotInteractableException,
                                                                           TimeoutException,
                                                                           ElementNotVisibleException])

    search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_tab.send_keys("DemoApplication")

    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='DemoApplication']")))
    select_individual_app.click()

    action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action.click()

    update_app = wait.until(EC.element_to_be_clickable((By.XPATH, update)))
    update_app.click()

    update_name = wait.until(EC.element_to_be_clickable((By.XPATH, update_app_name)))
    update_name.clear()
    update_name.send_keys("Demo " * 10)

    name_warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, update_name_warning_msg))).text
    assert "* Ensure this field has no more than 50 characters." in name_warning_msg

    update_URL = wait.until(EC.element_to_be_clickable((By.XPATH, update_url)))
    update_URL.clear()
    update_URL.send_keys("http://!1!!111.com")

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, update_submit_btn)))
    submit.click()
    time.sleep(1)

    url_warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, update_url_warning_msg))).text
    assert "* Enter a valid URL." in url_warning_msg
    time.sleep(1)
    close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close']")))
    close_popup.click()


