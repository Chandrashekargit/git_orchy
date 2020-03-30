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
from Applications.test_manual_entry_scans.manual_entry import manual_entry_vul


@mark.manually_enter_vul
def test_manual_entry(driver, create_app):
    manual_entry_vul(driver, search_key="DemoApplication", individual_app_xpath="//label[contains(text(),'DemoApplication')]",
                     scan_name="Manual scan", vul_name="SQL injection", cwe_num=89, owasp_status="injection")


































# wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
#     NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
#
# applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
# applicationTab.click()
#
# search_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
# search_tab.clear()
# time.sleep(1)
# search_tab.click()
# search_tab.send_keys("DemoApplication")
#
# select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'DemoApplication')]")))
# select_individual_app.click()
# time.sleep(2)
#
# action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
# action_dp.click()
#
# manual_entry_option = wait.until(EC.element_to_be_clickable((By.XPATH, manual_entry)))
# manual_entry_option.click()
#
# scan_name = wait.until(EC.element_to_be_clickable((By.XPATH, man_scan_name)))
# scan_name.send_keys("Manual scan")
#
# vulnerability_name = wait.until(EC.presence_of_element_located((By.XPATH, man_vul_name)))
# vulnerability_name.send_keys("SQL injection")
#
# cwe = wait.until(EC.presence_of_element_located((By.XPATH, man_cwe)))
# ActionChains(driver).move_to_element(cwe).click(cwe).send_keys("89").send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
#
# owasp = wait.until(EC.presence_of_element_located((By.XPATH, man_owasp)))
# owasp.send_keys("injection")
# owasp.send_keys(Keys.ARROW_DOWN)
# owasp.send_keys(Keys.ENTER)
#
# if 'Next' in driver.page_source:
#     print("Next button visible")
# else:
#     print("Unable to see the 'Next' button")
#
# next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_btn)))
# next.click()
#
# descrption = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, man_desc)))
# descrption.send_keys("xyz " * 20)
#
# remediation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, man_remed)))
# remediation.send_keys("xyz " * 20)
#
# previous_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, previous_btn)))
# previous_button.click()
#
# next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_btn)))
# next.click()
#
# if 'Submit' in driver.page_source:
#     print("submit button visible")
# else:
#     print("submit button not visible")
#
# submit = wait.until(EC.element_to_be_clickable((By.XPATH, man_submit)))
# submit.click()
# time.sleep(3)