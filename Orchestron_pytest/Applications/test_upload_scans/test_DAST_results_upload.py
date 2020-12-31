from pytest import mark
from Applications.test_upload_scans.upload_results import upload_res
from xpath.Application_module_xpath import *
from spinner.spinner import *


dast_tools = [("/home/junaid/Downloads/results_supported_by_orchy/zap.xml", "ZAP (json,xml)"),
              ("/home/junaid/Downloads/results_supported_by_orchy/burp.xml", "Burp (json,xml)"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Arachni.json", "arachni"),
              ("/home/junaid/Downloads/results_supported_by_orchy/AppScan_DAST.xml", "AppScan - DAST"),
              ("/home/junaid/Downloads/results_supported_by_orchy/w3af.xml", "w3af"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Acunetix.xml", "acunetix"),
              ("/home/junaid/Downloads/results_supported_by_orchy/appspider.xml", "appspider")]

# dast_names = ["zap", "burp", "arachni", "AppScan - DAST", "w3af", "acunetix", "appspider"]


@mark.dast
def test_dast_results(driver):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    for (tool, name) in dast_tools:
        # calling the function 'upload_res' to upload all the DAST scans.
        upload_res(driver, application="//label[contains(text(), 'all results')]", scan_name=name, tool_name=name, file_loc=tool)
        stop_till_spinner_is_invisible(driver)
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
        stop_till_spinner_is_invisible(driver)