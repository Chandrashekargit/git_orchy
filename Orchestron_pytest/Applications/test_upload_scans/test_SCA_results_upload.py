import time
from pytest import mark
from selenium.common.exceptions import *
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
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
            ]

sca_names = ["OWASP", "snyk", "whitesource", "Retire", "npm", "snyk"]

application3 = ["//label[contains(text(), 'SCA')]"]



@mark.smoke1
@mark.sca
class UploadScaScansAndCheckAllWarningMessagesTests:
    def test_sca_results(self, driver):
        for app3 in application3:
            for (tool3, name3) in zip(sca_tools, sca_names):
                wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
                    NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

                applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, application_tab)))
                applicationTab.click()
                time.sleep(1.5)
                app = WebDriverWait(driver, 10, poll_frequency=1.5).until(EC.element_to_be_clickable((By.XPATH, app3)))
                app.click()

                action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
                action.click()

                uploadresult = wait.until(EC.element_to_be_clickable((By.XPATH, upload_results)))
                uploadresult.click()

                selectTool = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, tool)))
                selectTool.click()
                selectTool.send_keys(name3)
                selectTool.send_keys(Keys.ARROW_DOWN)
                selectTool.send_keys(Keys.ENTER)

                file_name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, name)))
                file_name.send_keys(name3)

                uploadFile = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, file)))
                uploadFile.send_keys(tool3)

                submit1 = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
                submit1.click()
                time.sleep(8)
                driver.refresh()

    def test_for_warning_msg_if_we_upload_scans_with_same_name(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()
        time.sleep(1.5)
        app = WebDriverWait(driver, 10, poll_frequency=1.5).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'SCA')]")))
        app.click()

        action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        action.click()

        uploadresult = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, upload_results)))
        uploadresult.click()

        selectTool = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, tool)))
        selectTool.click()
        selectTool.send_keys("snyk")
        selectTool.send_keys(Keys.ARROW_DOWN)
        selectTool.send_keys(Keys.ENTER)

        file_name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, name)))
        file_name.send_keys("snyk")

        uploadFile = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, file)))
        uploadFile.send_keys("/home/junaid/Downloads/results_supported_by_orchy/snyk.json")

        submit1 = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
        submit1.click()
        time.sleep(8)

        warning_msg1 = WebDriverWait(driver, 2, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()=' * Scan name should be unique']"))).text
        print("\n", warning_msg1)
        assert "* Scan name should be unique" in warning_msg1
        file_name.clear()
        file_name.send_keys("1" * 100)
        warning_msg2 = WebDriverWait(driver, 2, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()=' * Max Length is 100 Characters']"))).text
        print(warning_msg2)
        assert "* Max Length is 100 Characters" in warning_msg2

