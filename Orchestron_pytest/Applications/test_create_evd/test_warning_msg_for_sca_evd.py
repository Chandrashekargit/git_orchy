from Applications.test_create_evd.create_evd import *
from Applications.test_create_applications.create_app import *
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_delete_application.delete_app import *
from pytest import mark

module_names = [" ", "abc.jar", " ", " ", "abc.jar"]
version_ids = [" ", " ", "1.75.2", " ", "2.325.356.366"]
cve_ids = [" ", " ", " ", "CVE-2014-201636", "CVEE-2014639-20163655"]


@mark.warning_msgs_for_sca
class CreateEvidenceTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="test_to_create_manual_evd", url="http://QWERTY123.com")

    def test_create_manual_vul(self, driver):
        create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'test_to_create_manual_evd')]",
                          scan_name="Manual vul", Severity="Low", cwe_num="89:Sql")

    def test_wrng_msg_of_sca_evd(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p")
        for (module, version, cve) in zip(module_names, version_ids, cve_ids):
            if module == " " and version == " " and cve == " ":
                sca_evd(driver, module_name=module, version_id=version, cve_id=cve)
                sca_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(sca_wrng_msg) == 3
                close_sca_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_sca_evd_pop_up.click()

            elif (module == "abc.jar" and version == " " and cve == " ") or (module == " " and version == "1.75.2" and cve == " ") or \
                    (module == " " and version == " " and cve == "CVE-2014-201636"):
                sca_evd(driver, module_name=module, version_id=version, cve_id=cve)
                sca_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(sca_wrng_msg) == 2
                close_sca_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_sca_evd_pop_up.click()

            else:
                sca_evd(driver, module_name=module, version_id=version, cve_id=cve)
                version_wrng_msg = wait.until(EC.presence_of_element_located((By.XPATH, version_id_wrng_msg)))
                assert version_wrng_msg.text == "* Ensure this field has no more than 12 characters."
                cve_wrng_msg = wait.until(EC.presence_of_element_located((By.XPATH, cve_id_wrng_msg)))
                assert cve_wrng_msg.text == "* Ensure this field has no more than 20 characters."
                close_sca_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_sca_evd_pop_up.click()

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'test_to_create_manual_evd')]")
