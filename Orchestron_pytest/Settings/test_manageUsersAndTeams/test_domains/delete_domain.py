import pytest
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
import time
from selenium.common.exceptions import *


def delete_domain(driver, domain_name=None):
    wait = WebDriverWait(driver, 10, poll_frequency=3, ignored_exceptions=[ElementClickInterceptedException,
                       ElementNotInteractableException, ElementNotVisibleException])
    domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
    domain.click()
    time.sleep(2)
    search = wait.until(EC.presence_of_element_located((By.XPATH, domain_search_field)))
    search.clear()
    search.send_keys(domain_name)
    time.sleep(2)
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, doamin_action_dropdown)))
    action_dp.click()
    time.sleep(1)
    delete = wait.until(EC.element_to_be_clickable((By.XPATH, domain_actiondp_delete)))
    delete.click()
    delete_domain_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, domain_delete_yes)))
    delete_domain_pop_up.click()
