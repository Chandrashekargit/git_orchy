from Applications.test_create_evd.create_evd import *
from Applications.test_create_applications.create_app import *
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_delete_application.delete_app import *
from pytest import mark
from spinner.spinner import *

modules = [" ", "abc.jar", " ", " ", " ", " ", " ", " "]
versions = [" ", " ", "1.75.2", " ", " ", " ", " ", " "]
cpes = [" ", " ", " ", "file:/a27f77f6f964a036d243dd631b80c21bff079f64", "cpe:/a:1024cms:1024_cms:0.7", " ", " ", " "]
image_digests = [" ", " ", " ", " ", "sha256:b2ad93b079b1495488cc01375de799c402d45086015a120c105ea00e1be0fd52", "qw321", " ", " "]
registry_conts = [" ", " ", " ", " ", " ", "hello-world", " ", " "]
image_names = [" ", " ", " ", " ", " ", " ", "Orchy-image1", " "]
image_repos = [" ", " ", " ", " ", " ", " ", " ", "docker-rits-devsecops-csec-local.pruregistry.intranet.asia:8443/vulnerable-apps/dvwa:latest"]
cves = [" ", " ", " ", " ", " ", " ", " ", " ", "CVE-2014-201636"]


@mark.warning_msgs_for_container
class CreateEvidenceTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="test_to_create_manual_evd", url="http://QWERTY123.com")

    def test_create_manual_vul(self, driver):
        create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'test_to_create_manual_evd')]",
                          scan_name="Manual vul", Severity="Low", cwe_num="89:Improper", Descrption="This is manual vul")

    def test_create_manual_evd_and_assert_wrng_msgs_for_empty_fields(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p",
                                  application_name_xpath="//label[contains(text(), 'test_to_create_manual_evd')]")
        stop_till_spinner_is_invisible(driver)
        click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
        click_on_create_evd_btn.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(1)
        container_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, container_toggle_btn)))
        container_evd_enable.click()

        stop_till_spinner_is_invisible(driver)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
        driver.execute_script("arguments[0].click();", submit)

        len_of_wrng_msg_for_empty_field = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
        wrng_msg_for_empty_field = wait.until(EC.presence_of_element_located((By.XPATH, wrng_msg_when_fields_are_empty)))
        assert len(len_of_wrng_msg_for_empty_field) == 8
        assert wrng_msg_for_empty_field.text == "* This field may not be blank."

        close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
        close_dast_evd_pop_up.click()

    def test_wrng_msgs_for_container_evd(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p",
                                  application_name_xpath="//label[contains(text(), 'test_to_create_manual_evd')]")

        stop_till_spinner_is_invisible(driver)
        for (module, version, cpe, image_digest, registry_cont, image_name, image_repo, cve) in zip(modules, versions, cpes, image_digests, registry_conts, image_names, image_repos, cves):
            if module == " " and version == " " and cpe == " " and image_digest == " ":
                container_evd(driver, enter_module=module, enter_version=version, enter_cpe=cpe, enter_image_digest=image_digest, enter_registry_container=registry_cont, enter_image_name=image_name, enter_image_repository=image_repo, enter_cve=cve)
                len_of_wrng_msg_for_empty_field = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                wrng_msg_for_empty_field = wait.until(EC.presence_of_element_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(len_of_wrng_msg_for_empty_field) == 8
                assert wrng_msg_for_empty_field.text == "* This field may not be blank."

                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif module == "abc.jar" or cpe == "file:/a27f77f6f964a036d243dd631b80c21bff079f64" or image_digest == "sha256:b2ad93b079b1495488cc01375de799c402d45086015a120c105ea00e1be0fd52"\
                    or registry_cont == "hello-world" or image_name == "Orchy-image1" or image_repo == "docker-rits-devsecops-csec-local.pruregistry.intranet.asia:8443/vulnerable-apps/dvwa:latest" or cve == "CVE-2014-201636":
                container_evd(driver, enter_module=module, enter_version=version, enter_cpe=cpe, enter_image_digest=image_digest, enter_registry_container=registry_cont, enter_image_name=image_name, enter_image_repository=image_repo, enter_cve=cve)
                len_of_wrng_msg_for_empty_field = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                wrng_msg_for_empty_field = wait.until(EC.presence_of_element_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(len_of_wrng_msg_for_empty_field) == 7
                assert wrng_msg_for_empty_field.text == "* This field may not be blank."

                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()