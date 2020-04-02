import time
from pytest import mark
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from xpath.profile_module_xpath import *


def ProfileScript(driver, firstName=None, secondName=None):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, profile_dropdown)))
    dropdown.click()

    select_profile = wait.until(EC.element_to_be_clickable((By.XPATH, profile)))
    select_profile.click()

    first_name = wait.until(EC.element_to_be_clickable((By.XPATH, firstname)))
    first_name.clear()
    first_name.send_keys(firstName)

    second_name = wait.until(EC.element_to_be_clickable((By.XPATH, secondname)))
    second_name.clear()
    second_name.send_keys(secondName)

    # submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, submit)))
    # submit_btn.click()
