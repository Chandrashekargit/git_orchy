from Applications.test_upload_scans.upload_results import *
from Applications.test_create_applications.create_app import *
from pytest import mark
from Applications.test_delete_application.delete_app import *


@mark.wrng_msg_for_upload_scans
class warning_msg_of_upload_scan_feature_Tests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="Demo app", url="http://demo.com")

    def test_wrng_msg_when_we_upload_wrong_format(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        upload_res(driver, application="//label[contains(text(), 'Demo app')]", tool_name="zap 2.9", scan_name= "zap(JSON)",
                   file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/zap_2_7_0.xml")

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        warng_msg_for_file_format = wait.until(EC.visibility_of_element_located((By.XPATH, warning_msg_for_file_format)))
        assert warng_msg_for_file_format.text == "* Supported formats are json"

        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_upload_results_pop_up)))
        close_pop_up.click()

    def test_wrng_msg_when_we_upload_wrong_file_for_zap_tool(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        upload_res(driver, application="//label[contains(text(), 'Demo app')]", tool_name="zap 2.9", scan_name="zap(JSON)",
                   file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/snyk.json")

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        warng_msg_for_file_format = wait.until(EC.visibility_of_element_located((By.XPATH, wrng_msg_when_we_upload_wrong_file)))
        assert warng_msg_for_file_format.text == "* Not a ZAP 2.9.0 file"

        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_upload_results_pop_up)))
        close_pop_up.click()

    def test_wrng_msg_when_we_upload_scan_with_existing_scan_name(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        # upload Snyk scan results
        upload_res(driver, application="//label[contains(text(), 'Demo app')]", tool_name="Snyk", scan_name="Snyk",
                   file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/snyk.json")
        # waits until the results are parsed
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

        # Again upload the snyk scan results with same scan name.
        upload_res(driver, application="//label[contains(text(), 'Demo app')]", tool_name="Snyk", scan_name="Snyk",
                   file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/snyk.json")

        warning_msg1 = wait.until(EC.visibility_of_element_located((By.XPATH, wrng_msg_for_existing_scan_name))).text
        assert warning_msg1 == "* Scan name should be unique"

        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_upload_results_pop_up)))
        close_pop_up.click()

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'Demo app')]")
