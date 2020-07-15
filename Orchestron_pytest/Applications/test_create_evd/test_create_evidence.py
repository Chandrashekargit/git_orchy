from Applications.test_create_evd.create_evd import *
from Applications.test_create_applications.create_app import *
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_delete_application.delete_app import *
from pytest import mark


@mark.create_manual_evd
class CreateEvidenceTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="test_to_create_manual_evd", url="http://QWERTY123.com")

    def test_create_manual_vul(self, driver):
        create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'test_to_create_manual_evd')]",
                          scan_name="Manual vul", Severity="Low", cwe_num="89:Sql")

    def test_create_manual_evd(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p")
        sca_evd(driver, module_name="abc.jar", version_id="3.2.66", cve_id="CVE-2014-201693")
        wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
        wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))

        sast_evd(driver, line_no="2666", line_range="2660-3000", code_snippet_location="/home/junaid/Desktop/request.txt",
                 path="bin/source/acticate", file_name="sast_evd", param="a!=1")
        wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
        wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))

        dast_evd(driver, enter_url="https://demo.com", enter_param="A!==1", enter_payload="c+d == 5", req_file_loc=
                 "/home/junaid/Desktop/request.txt", response_file_loc="/home/junaid/Desktop/Response.txt")
        wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
        wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'test_to_create_manual_evd')]")
