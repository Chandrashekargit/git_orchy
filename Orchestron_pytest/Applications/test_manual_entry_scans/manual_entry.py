import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from xpath.Application_module_xpath import *


def create_manual_vul(driver, individual_app_xpath=None, scan_name=None, Severity=None, cwe_num=None):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # search_tab = wait.until(EC.presence_of_element_located((By.XPATH, search)))
    # search_tab.clear()
    # time.sleep(1)
    # search_tab.click()
    # search_tab.send_keys()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, individual_app_xpath)))
    select_individual_app.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()
    manual_entry_option = wait.until(EC.element_to_be_clickable((By.XPATH, manual_entry)))
    manual_entry_option.click()

    scanName = wait.until(EC.element_to_be_clickable((By.XPATH, man_scan_name)))
    scanName.send_keys(scan_name)

    select_severity = wait.until(EC.element_to_be_clickable((By.XPATH, severity)))
    select_severity.send_keys(Severity)
    select_severity.send_keys(Keys.ARROW_DOWN)
    select_severity.send_keys(Keys.ENTER)

    cwe = wait.until(EC.presence_of_element_located((By.XPATH, man_cwe)))
    cwe.send_keys(cwe_num)
    time.sleep(1)
    cwe.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    cwe.send_keys(Keys.ENTER)

    descrption = wait.until(EC.presence_of_element_located((By.XPATH, man_desc)))
    descrption.send_keys("This is manually added vulnerability")

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, man_submit)))
    submit.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Manual vulnerability has been created successfully!']")))
