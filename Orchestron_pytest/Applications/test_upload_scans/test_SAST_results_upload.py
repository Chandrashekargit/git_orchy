import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytest import mark
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *

sast_names = ["AppScan - SAST", "bandit", "brakeman", "checkmarx", "findsecbugs", "gosec",
              "hp", "nodejs", "veracode", "xanitizer"]

sast_tools = ["/home/junaid/Downloads/results_supported_by_orchy/AppScan_SAST.html",
              "/home/junaid/Downloads/results_supported_by_orchy/bandit.json",
              "/home/junaid/Downloads/results_supported_by_orchy/brakeman-4.7.json",
              "/home/junaid/Downloads/results_supported_by_orchy/Checkmarx.xml",
              "/home/junaid/Downloads/results_supported_by_orchy/FindSecBugs.xml",
              "/home/junaid/Downloads/results_supported_by_orchy/GoSec.json",
              "/home/junaid/Downloads/results_supported_by_orchy/HP.xml",
              "/home/junaid/Downloads/results_supported_by_orchy/nodejsScan.json",
              "/home/junaid/Downloads/results_supported_by_orchy/veracode.xml",
              "/home/junaid/Downloads/results_supported_by_orchy/xanitizer.xml"]

application1 = ["//label[contains(text(), 'SAST')]"]


@mark.smoke1
@mark.sast
def test_sast_results(driver):
    for app1 in application1:
        for (tool1, name1) in zip(sast_tools, sast_names):
            applicationtab = WebDriverWait(driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(
                (By.XPATH, application_tab)))
            applicationtab.click()

            app = WebDriverWait(driver, 20, poll_frequency=3).until(EC.element_to_be_clickable((By.XPATH, app1)))
            app.click()
            time.sleep(2)
            action = WebDriverWait(driver, 20, poll_frequency=3).until(EC.element_to_be_clickable(
                (By.XPATH, action_dropdown)))
            action.click()
            time.sleep(1)
            uploadresult = WebDriverWait(driver, 20, poll_frequency=3).until(EC.element_to_be_clickable(
                (By.XPATH, upload_results)))
            uploadresult.click()

            select_tool = WebDriverWait(driver, 20, poll_frequency=3).until(EC.presence_of_element_located(
                (By.XPATH, tool)))
            select_tool.click()
            select_tool.send_keys(name1)
            select_tool.send_keys(Keys.ARROW_DOWN)
            select_tool.send_keys(Keys.ENTER)

            file_name = WebDriverWait(driver, 20, poll_frequency=3).until(EC.presence_of_element_located(
                (By.XPATH, name)))
            file_name.send_keys(name1)

            upload_file = WebDriverWait(driver, 20, poll_frequency=3).until(EC.presence_of_element_located(
                (By.XPATH, file)))
            upload_file.send_keys(tool1)

            submit1 = WebDriverWait(driver, 20, poll_frequency=3).until(EC.presence_of_element_located(
                (By.XPATH, upload_results_submit)))
            submit1.click()
            time.sleep(8)
            driver.refresh()


