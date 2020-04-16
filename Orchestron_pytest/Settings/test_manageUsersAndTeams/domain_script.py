import time
import pytest
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import TimeoutException


def create_domain_script(driver, domain_names=None):
    """
    These function lets us test negative domain names.
    """
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
    domain.click()
    driver.execute_script("window.scrollTo(0, 900);")
    create = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create)))
    create.click()
    domain_name = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_field)))
    domain_name.send_keys(domain_names)
    domain_submit = WebDriverWait(driver, 3, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
    domain_submit.click()
