import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *

categories = ["//label[contains(text(),'SAST')]",
              "//label[contains(text(),'DAST')]",
              "//label[contains(text(),'SCA')]"]


@mark.give_name_of_all_vulnerabilities
def test_give_name_of_all_vulnerabilities(driver):
    """
    > These function gives us names of all SAST category vulnerabilities.
    > Before running these file make sure you run below commands one after the other,
            - "pytest -m create_apps -s -v"     (Creates an application with name called 'SAST')
            - "pytest -m sast -s -v"            (uploads all SAST scans to 'SAST' application)
            - "pytest -m dast -s -v"            (uploads all DAST scans to 'DAST' application)
            - "pytest -m sca -s -v"             (uploads all SCA scans to 'SCA' application)
    """
    for category in categories:
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        app = wait.until(EC.element_to_be_clickable((By.XPATH, category)))
        app.click()

        open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        open_vul.click()

        perpage = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage.click()

        selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        selectAll.click()
        driver.execute_script("window.scrollTo(0, 900);")
        time.sleep(5)
        allVul = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody[@role='rowgroup']"))).text
        print(allVul)
        print('*' * 50)
        driver.refresh()

