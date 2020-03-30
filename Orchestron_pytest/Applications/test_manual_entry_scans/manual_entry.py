import time
from pytest import mark
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from xpath.Application_module_xpath import *


def manual_entry_vul(driver, search_key=None, individual_app_xpath=None, scan_name=None, vul_name=None,
                 cwe_num=None, owasp_status=None):
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    search_tab = wait.until(EC.presence_of_element_located((By.XPATH, search)))
    search_tab.clear()
    time.sleep(1)
    search_tab.click()
    search_tab.send_keys(search_key)

    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, individual_app_xpath)))
    select_individual_app.click()
    time.sleep(2)

    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()

    manual_entry_option = wait.until(EC.element_to_be_clickable((By.XPATH, manual_entry)))
    manual_entry_option.click()

    scanName = wait.until(EC.element_to_be_clickable((By.XPATH, man_scan_name)))
    scanName.send_keys(scan_name)

    vulnerability_name = wait.until(EC.presence_of_element_located((By.XPATH, man_vul_name)))
    vulnerability_name.send_keys(vul_name)

    cwe = wait.until(EC.presence_of_element_located((By.XPATH, man_cwe)))
    ActionChains(driver).move_to_element(cwe).click(cwe).send_keys(cwe_num).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    owasp = wait.until(EC.presence_of_element_located((By.XPATH, man_owasp)))
    owasp.send_keys(owasp_status)
    owasp.send_keys(Keys.ARROW_DOWN)
    owasp.send_keys(Keys.ENTER)

    # if 'Next' in driver.page_source:
    #     print("Next button visible")
    # else:
    #     print("Unable to see the 'Next' button")

    next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_btn)))
    next.click()

    descrption = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, man_desc)))
    descrption.send_keys("xyz " * 20)

    remediation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, man_remed)))
    remediation.send_keys("xyz " * 20)

    # previous_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, previous_btn)))
    # previous_button.click()

    # next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_btn)))
    # next.click()

    # if 'Submit' in driver.page_source:
    #     print("submit button visible")
    # else:
    #     print("submit button not visible")

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, man_submit)))
    submit.click()
    time.sleep(3)