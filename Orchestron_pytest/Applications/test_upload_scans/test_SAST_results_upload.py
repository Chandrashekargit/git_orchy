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
from Applications.test_upload_scans.test_upload_results import upload_res

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


@mark.smoke1
@mark.sast
def test_sast_results(driver):
    for (tool1, name1) in zip(sast_tools, sast_names):
        upload_res(driver, application="//label[contains(text(), 'SAST')]", tool_name=name1, file_loc=tool1)
        time.sleep(10)
        driver.refresh()
