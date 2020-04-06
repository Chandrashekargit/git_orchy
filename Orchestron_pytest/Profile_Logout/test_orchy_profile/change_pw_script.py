import time
from pytest import mark
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from xpath.profile_module_xpath import *


def change_pw(driver, Current_password=None, New_password=None, Confirm_new_password=None):
    wait = WebDriverWait(driver, 6, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, profile_dropdown)))
    dropdown.click()

    select_profile = wait.until(EC.element_to_be_clickable((By.XPATH, profile)))
    select_profile.click()

    move_to_change_pw_section = wait.until(EC.element_to_be_clickable((By.XPATH, change_pw_section)))
    move_to_change_pw_section.click()

    current_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, current_pw)))
    current_password_field.send_keys(Current_password)

    new_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, new_pw)))
    new_password_field.send_keys(New_password)

    confirm_new_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_new_pw)))
    confirm_new_password_field.send_keys(Confirm_new_password)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, change_pw_submit_btn)))
    submit.click()
