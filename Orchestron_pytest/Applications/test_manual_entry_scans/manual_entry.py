import time
from selenium.webdriver.common.keys import Keys
from xpath.Application_module_xpath import *
from spinner.spinner import *


def create_manual_vul(driver, individual_app_xpath, scan_name, Severity, cwe_num, Descrption):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # search_tab = wait.until(EC.presence_of_element_located((By.XPATH, search)))
    # search_tab.clear()
    # time.sleep(1)
    # search_tab.click()
    # search_tab.send_keys()

    stop_till_spinner_is_invisible(driver)
    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, individual_app_xpath)))
    select_individual_app.click()

    stop_till_spinner_is_invisible(driver)
    stop_till_spinner_is_invisible(driver)
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()
    manual_entry_option = wait.until(EC.element_to_be_clickable((By.XPATH, manual_entry)))
    manual_entry_option.click()

    stop_till_spinner_is_invisible(driver)
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
    descrption.send_keys(Descrption)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, man_submit)))
    submit.click()

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Manual vulnerability has been created successfully!']")))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, "//p[text()='Manual vulnerability has been created successfully!']")))
