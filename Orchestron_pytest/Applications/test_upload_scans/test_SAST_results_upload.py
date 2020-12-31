from pytest import mark
from Applications.test_upload_scans.upload_results import upload_res
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from spinner.spinner import *


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


@mark.sast
def test_sast_results(driver):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    for (tool, name) in zip(sast_tools, sast_names):
        upload_res(driver, application="//label[contains(text(), 'all results')]", tool_name=name, scan_name=name, file_loc=tool)
        stop_till_spinner_is_invisible(driver)
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
        stop_till_spinner_is_invisible(driver)
