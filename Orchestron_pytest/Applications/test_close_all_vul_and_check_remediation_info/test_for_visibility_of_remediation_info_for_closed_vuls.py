from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_close_all_vul_and_check_remediation_info.close_all_vulnerable import *
from Applications.test_close_all_vul_and_check_remediation_info.remediation_info_ import *
from Applications.test_delete_application.delete_app import *
from pytest import mark


@mark.check_remediation_info
class CheckRemediationInfoTests:
    """
    This function lets us check if remediation info is visible for all the closed vulnerabilities.
    """
    def test_create_app(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        create_apps(driver, application_name="check_remed_info_app", url="http://demo.com")

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_upload_scans(self, driver):
        upload_res(driver, application="//label[contains(text(),'check_remed_info_app')]", tool_name="ZAP (json,xml)",
                   scan_name="zap", file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/zap_2_7_0.xml")
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
        # waits until the Loading symbol is invisible
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    def test_close_all_vulnerable(self, driver):
        close_all_vulnerable(driver, app_name="//label[contains(text(),'check_remed_info_app')]")

    def test_visibility_of_remediation_info_of_closed_vuls(self, driver):
        checks_visibility_of_remediation_info_of_closed_vuls(driver, app_name="//label[contains(text(),'check_remed_info_app')]")
