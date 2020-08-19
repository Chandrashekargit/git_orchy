from pytest import mark
from Applications.test_upload_scans.upload_results import upload_res
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *

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
    for (tool2, name2) in dast_tools:
        # calling the function 'upload_res' to upload all the DAST scans.
        upload_res(driver, application="//label[contains(text(), 'DAST')]", tool_name=name2, file_loc=tool2)

        # waits until the submit is invisible
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
        # waits until the Loading symbol is invisible
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
