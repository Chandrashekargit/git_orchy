import time
from pytest import mark
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from xpath.Application_module_xpath import *
from Applications.test_upload_scans.test_upload_results import upload_res

sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
             ]

sca_names = ["OWASP", "snyk", "whitesource", "Retire", "npm", "snyk"]


@mark.smoke1
@mark.sca
class UploadScaScansAndCheckAllWarningMessagesTests:
    def test_sca_results(self, driver):
        for (tool3, name3) in zip(sca_tools, sca_names):
            # calling the function 'upload_res' to upload all SCA scan's.
            upload_res(driver, application="//label[contains(text(), 'SCA')]", tool_name=name3, file_loc=tool3)
            time.sleep(10)
            driver.refresh()

    # def test_for_warning_msg_if_we_upload_scans_with_same_name(self, driver):
    #     # calling the function 'upload_res' to upload zap scan
    #     upload_res(driver, application="//label[contains(text(), 'SCA')]", tool_name="snyk",
    #                file_loc="/home/junaid/Downloads/results_supported_by_orchy/snyk.json")
    #
    #     # assert if we are able to see the warning message when we upload the scans with existing scan name
    #     warning_msg1 = WebDriverWait(driver, 2, poll_frequency=1).until(
    #         EC.presence_of_element_located((By.XPATH, "//p[text()=' * Scan name should be unique']"))).text
    #     print("\n", warning_msg1)
    #     assert "* Scan name should be unique" in warning_msg1
    #
    #     # assert if we are able to see the warning message when the scan name reaches max limit of characters.
    #     scan_name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH,
    #     "//div[@class='container-fluid']//input[@class='inline-form-control-count-with-box orchy_font_family orchy_font_md orchy_font_color form-control is-valid']")))
    #     scan_name.clear()
    #     scan_name.send_keys("1" * 100)
    #     warning_msg2 = WebDriverWait(driver, 2, poll_frequency=1).until(
    #         EC.presence_of_element_located((By.XPATH, "//p[text()=' * Max Length is 100 Characters']"))).text
    #     print(warning_msg2)
    #     assert "* Max Length is 100 Characters" in warning_msg2
