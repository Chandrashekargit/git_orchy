import time
import pytest
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import *
from Settings.test_manageUsersAndTeams.domain_script import create_domain_script

"""
> Tests if we can create new domain
> Tests to create domains with positive and negative domain name formats.
> Tests the warning message if we try to create existing domain names.
> Tests to delete domain while users with that domain exist and asserts the warning message(if any).
> Tests if we can delete the domain.
> Tests if we can update the domain name while users with that domain name exist and assert the warning message(if any).
"""


@mark.parametrize('domain_names', [
                    "demo123.com", '@gmail.com', 'demo!@.com', 'demo.com ', ' demo.com']
                  )
def test_valid_and_invalid_domain_names(driver, domain_names):
    """
    These function lets us test negative domain names.
    """
    wait = WebDriverWait(driver, 6, poll_frequency=2, ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)
    time.sleep(1)
    domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
    domain.click()
    # driver.execute_script("window.scrollTo(0, 900);")
    time.sleep(1)
    create = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create)))
    create.click()
    domain_name = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_field)))
    domain_name.send_keys(domain_names)
    try:
        domain_submit = WebDriverWait(driver, 3, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
        domain_submit.click()
    except TimeoutException:
        print("\n***Domain can't be registered, please check the format***")
        close_pop_up = WebDriverWait(driver, 3, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, domain_create_popup_close)))
        close_pop_up.click()
        # driver.refresh()
