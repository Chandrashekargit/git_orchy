import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from xpath.Application_module_xpath import *


sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json"]

sca_names = ["OWASP", "snyk", "whitesource", "Retire", "npm", "snyk"]

application3 = ["//label[contains(text(), 'SCA')]"]


@mark.smoke1
@mark.sca
def test_sca_results(driver):
    for app3 in application3:
        for (tool3, name3) in zip(sca_tools, sca_names):
            applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, application_tab)))
            applicationTab.click()
            time.sleep(1.5)
            app = WebDriverWait(driver, 10, poll_frequency=1.5).until(EC.element_to_be_clickable((By.XPATH, app3)))
            app.click()

            action = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
            action.click()

            uploadresult = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, upload_results)))
            uploadresult.click()

            selectTool = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, tool)))
            selectTool.click()
            selectTool.send_keys(name3)
            selectTool.send_keys(Keys.ARROW_DOWN)
            selectTool.send_keys(Keys.ENTER)

            file_name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, name)))
            file_name.send_keys(name3)

            uploadFile = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, file)))
            uploadFile.send_keys(tool3)

            submit1 = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
            submit1.click()
            time.sleep(8)

            warning_msg = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, "//p[text()=' * Scan name should be unique']"))).is_displayed()
            try:
                if warning_msg:
                    print("Scan with these name already exist")
            except:
                print("scan successfully created")

