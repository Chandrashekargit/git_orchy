from pytest import mark
from Applications.test_upload_scans.upload_results import upload_res
from xpath.Application_module_xpath import *
from spinner.spinner import *
import time

sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
             ]

sca_names = ["OWASP Dependency", "snyk", "whitesource", "Retire", "npm"]


@mark.sca
class UploadScaScansAndCheckAllWarningMessagesTests:
    def test_sca_results(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        for (tool, name) in zip(sca_tools, sca_names):

            # calling the function 'upload_res' to upload all SCA scan's.
            upload_res(driver, application="//label[contains(text(), 'SCA')]", tool_name=name, file_loc=tool, scan_name=name)
            stop_till_spinner_is_invisible(driver)
            wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
            wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
            stop_till_spinner_is_invisible(driver)
