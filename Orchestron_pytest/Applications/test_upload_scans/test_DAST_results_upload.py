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


dast_tools = [("/home/junaid/Downloads/results_supported_by_orchy/zap.xml", "zap"),
              ("/home/junaid/Downloads/results_supported_by_orchy/burp.xml", "burp"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Arachni.json", "arachni"),
              ("/home/junaid/Downloads/results_supported_by_orchy/AppScan_DAST.xml", "AppScan - DAST"),
              ("/home/junaid/Downloads/results_supported_by_orchy/w3af.xml", "w3af"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Acunetix.xml", "acunetix"),
              ("/home/junaid/Downloads/results_supported_by_orchy/appspider.xml", "appspider")]

# dast_names = ["zap", "burp", "arachni", "AppScan - DAST", "w3af", "acunetix", "appspider"]


@mark.smoke1
@mark.dast
def test_dast_results(driver):
    for (tool2, name2) in dast_tools:
        upload_res(driver, application="//label[contains(text(), 'DAST')]", tool_name=name2, file_loc=tool2)
        time.sleep(12)
        driver.refresh()
