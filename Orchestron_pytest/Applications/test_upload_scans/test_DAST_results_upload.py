import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from pytest import mark
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


dast_tools = [("/home/junaid/Downloads/results_supported_by_orchy/zap.xml", "zap"),
              ("/home/junaid/Downloads/results_supported_by_orchy/burp.xml", "burp"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Arachni.json", "arachni"),
              ("/home/junaid/Downloads/results_supported_by_orchy/AppScan_DAST.xml", "AppScan - DAST"),
              ("/home/junaid/Downloads/results_supported_by_orchy/w3af.xml", "w3af"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Acunetix.xml", "acunetix"),
              ("/home/junaid/Downloads/results_supported_by_orchy/appspider.xml", "appspider")]

# dast_names = ["zap", "burp", "arachni", "AppScan - DAST", "w3af", "acunetix", "appspider"]

application2 = ["//label[contains(text(), 'DAST')]"]


@mark.smoke1
@mark.dast
def test_dast_results(driver):
    for app2 in application2:
        for (tool2, name2) in dast_tools:
            wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

            applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
                            EC.element_to_be_clickable((By.XPATH, application_tab)))
            applicationTab.click()

            app = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, app2)))
            app.click()

            action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
            action.click()

            upload_result = wait.until(EC.element_to_be_clickable((By.XPATH, upload_results)))
            upload_result.click()

            selectTool = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, tool)))
            selectTool.click()
            selectTool.send_keys(name2)
            selectTool.send_keys(Keys.ARROW_DOWN)
            selectTool.send_keys(Keys.ENTER)

            tool_name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, name)))
            tool_name.send_keys(name2)

            uploadFile = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, file)))
            uploadFile.send_keys(tool2)

            submit1 = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
            submit1.click()
            time.sleep(10)
            driver.refresh()
