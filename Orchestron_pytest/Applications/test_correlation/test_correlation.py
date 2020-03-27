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
# from Applications.test_create_applications.test_create_application import *


@pytest.mark.run(order=1)
def test_create_apps(driver, create_app):
    time.sleep(2)


@pytest.mark.run(order=2)
# @mark.man_entry
def test_manual_entry(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    search_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_tab.clear()
    time.sleep(1)
    search_tab.click()
    search_tab.send_keys("DemoApplication")

    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'DemoApplication')]")))
    select_individual_app.click()
    time.sleep(2)

    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()

    manual_entry_option = wait.until(EC.element_to_be_clickable((By.XPATH, manual_entry)))
    manual_entry_option.click()

    scan_name = wait.until(EC.element_to_be_clickable((By.XPATH, man_scan_name)))
    scan_name.send_keys("Manual scan")

    vulnerability_name = wait.until(EC.presence_of_element_located((By.XPATH, man_vul_name)))
    vulnerability_name.send_keys("SQL injection")

    cwe = wait.until(EC.presence_of_element_located((By.XPATH, man_cwe)))
    ActionChains(driver).move_to_element(cwe).click(cwe).send_keys("89").send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    owasp = wait.until(EC.presence_of_element_located((By.XPATH, man_owasp)))
    owasp.send_keys("injection")
    owasp.send_keys(Keys.ARROW_DOWN)
    owasp.send_keys(Keys.ENTER)

    if 'Next' in driver.page_source:
        print("Next button visible")
    else:
        print("Unable to see the 'Next' button")

    next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_btn)))
    next.click()

    descrption = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, man_desc)))
    descrption.send_keys("xyz " * 20)

    remediation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, man_remed)))
    remediation.send_keys("xyz " * 20)

    previous_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, previous_btn)))
    previous_button.click()

    next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_btn)))
    next.click()

    if 'Submit' in driver.page_source:
        print("submit button visible")
    else:
        print("submit button not visible")

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, man_submit)))
    submit.click()
    time.sleep(3)


@pytest.mark.run(order=3)
@mark.upload_results
def test_uploadresult(driver, tool='ZAP (json,xml)', name='zap scan',
                      file="/home/junaid/Downloads/results_supported_by_orchy/zap.xml"):
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    search_tab = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_tab.clear()
    time.sleep(1)
    search_tab.send_keys("DemoApplication")

    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'DemoApplication')]")))
    select_individual_app.click()

    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()

    uploadresult = wait.until(EC.element_to_be_clickable((By.XPATH, upload_results)))
    uploadresult.click()

    selectTool = wait.until(EC.element_to_be_clickable((By.XPATH, tool)))
    selectTool.click()
    selectTool.send_keys(tool)
    selectTool.send_keys(Keys.ARROW_DOWN)
    selectTool.send_keys(Keys.ENTER)

    file_name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, name)))
    file_name.send_keys(name)

    uploadFile = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, file)))
    uploadFile.send_keys(file)

    submit1 = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
    submit1.click()
    time.sleep(0.5)
    driver.refresh()
    time.sleep(2)


@pytest.mark.run(order=4)
def test_check_for_correlation(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_tab.send_keys("DemoApplication")

    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'DemoApplication')]")))
    select_individual_app.click()

    open_vulnerabilities = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vulnerabilities.click()

    driver.execute_script("window.scrollTo(0, 900)")

    sql1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[@title='Sql Injection']")))
    sql1.click()

    tools = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/section/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div[1]/table/tr[1]")))
    # print(tools.text)
    assert tools.text == 'Tool : Manual,ZAP' or tools.text == 'Tool : ZAP,Manual', "correlation isn't happening"

