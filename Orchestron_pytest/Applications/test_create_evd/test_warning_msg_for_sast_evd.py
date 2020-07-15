from Applications.test_create_evd.create_evd import *
from Applications.test_create_applications.create_app import *
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_delete_application.delete_app import *
from pytest import mark

line_nos = []
line_ranges = []
code_snippets = []
path = []
file = []
param = []


@mark.warning_msgs_for_sast
class CreateEvidenceTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="test_to_create_manual_evd", url="http://QWERTY123.com")

    def test_create_manual_vul(self, driver):
        create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'test_to_create_manual_evd')]",
                          scan_name="Manual vul", Severity="Low", cwe_num="89:Sql")

    def test_create_manual_evd_and_assert_wrng_msgs_for_empty_fields(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p")

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
        click_on_create_evd_btn.click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        sast_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, sast_toggle_btn)))
        sast_evd_enable.click()

        submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
        submit.click()

        sast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
        assert len(sast_wrng_msg) == 3
        line_no_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_for_empty_line_no)))
        assert len(line_no_wrng_msg) == 1
        code_snippet_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, code_snippet_wrng_msg_for_empty_field)))
        assert len(code_snippet_wrng_msg) == 1
        close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
        close_dast_evd_pop_up.click()
        driver.refresh()
