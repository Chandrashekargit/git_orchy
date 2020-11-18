from pytest import mark
from Applications.test_upload_scans.upload_results import upload_res
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *

sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
             ]

sca_names = ["OWASP Dependency", "snyk", "whitesource", "Retire", "npm", "snyk"]


@mark.smoke1
@mark.sca
class UploadScaScansAndCheckAllWarningMessagesTests:
    def test_sca_results(self, driver):
        for (tool3, name3) in zip(sca_tools, sca_names):
            # calling the function 'upload_res' to upload all SCA scan's.
            upload_res(driver, application="//label[contains(text(), 'all results')]", tool_name=name3, file_loc=tool3, scan_name=name3)

            # waits until the submit is invisible
            WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
            # waits until the Loading symbol is invisible
            WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
