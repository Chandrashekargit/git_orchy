from pytest import mark
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_create_applications.create_app import *
from Applications.test_delete_application.delete_app import *

names = [" ", "Manual vulnerability", " ", " ", " "]
severities = [" ", " ", "info", " ", " "]
cwes = ["=", "=", "=", "79", "="]
descriptions = [" ", " ", " ", " ", "Manual vul"]


@mark.wrng_msg_for_manual_vul
class EnterManualVulnerableTests:
    """
    This Testcase lets us check all the warning message for 'Manual entry' feature
    """
    def test_create_app(self, driver):
        create_apps(driver, application_name="Manual vul app", url="http://demo.com")

    def test_manual_entry(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        for (name, severity, cwe, desc) in zip(names, severities, cwes, descriptions):
            if name == " " and severity == " " and desc == " " and cwe == "=":
                create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'Manual vul app')]",
                                  scan_name=name, Severity=severity, cwe_num=cwe, Descrption=desc)
                empty_field_wrng_message = wait.until(EC.presence_of_all_elements_located((By.XPATH, empty_field_wrng_msg)))
                assert len(empty_field_wrng_message) == 2
                severity_empty_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_severity_field_empty)))
                assert severity_empty_warning_msg.text == "* Please select the severity"
                cwe_empty_field = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_cwe_field_empty)))
                assert cwe_empty_field.text == "* A valid integer is required."
                create_manual_vul_pop_up_close = wait.until(EC.element_to_be_clickable((By.XPATH, close_create_manual_vul_pop_up)))
                create_manual_vul_pop_up_close.click()
            elif name == "Manual vulnerability":
                create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'Manual vul app')]",
                                  scan_name=name, Severity=severity, cwe_num=cwe, Descrption=desc)
                empty_field_wrng_message = wait.until(EC.presence_of_all_elements_located((By.XPATH, empty_field_wrng_msg)))
                assert len(empty_field_wrng_message) == 1
                severity_empty_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_severity_field_empty)))
                assert severity_empty_warning_msg.text == "* Please select the severity"
                cwe_empty_field = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_cwe_field_empty)))
                assert cwe_empty_field.text == "* A valid integer is required."
                create_manual_vul_pop_up_close = wait.until(EC.element_to_be_clickable((By.XPATH, close_create_manual_vul_pop_up)))
                create_manual_vul_pop_up_close.click()
            elif severity == "info":
                create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'Manual vul app')]",
                                  scan_name=name, Severity=severity, cwe_num=cwe, Descrption=desc)
                empty_field_wrng_message = wait.until(EC.presence_of_all_elements_located((By.XPATH, empty_field_wrng_msg)))
                assert len(empty_field_wrng_message) == 2
                cwe_empty_field = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_cwe_field_empty)))
                assert cwe_empty_field.text == "* A valid integer is required."
                create_manual_vul_pop_up_close = wait.until(EC.element_to_be_clickable((By.XPATH, close_create_manual_vul_pop_up)))
                create_manual_vul_pop_up_close.click()
            elif cwe == 79:
                create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'Manual vul app')]",
                                  scan_name=name, Severity=severity, cwe_num=cwe, Descrption=desc)
                empty_field_wrng_message = wait.until(EC.presence_of_all_elements_located((By.XPATH, empty_field_wrng_msg)))
                assert len(empty_field_wrng_message) == 2
                severity_empty_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_severity_field_empty)))
                assert severity_empty_warning_msg.text == "* Please select the severity"
                create_manual_vul_pop_up_close = wait.until(EC.element_to_be_clickable((By.XPATH, close_create_manual_vul_pop_up)))
                create_manual_vul_pop_up_close.click()
            elif desc == "Manual vul":
                create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'Manual vul app')]",
                                  scan_name=name, Severity=severity, cwe_num=cwe, Descrption=desc)
                empty_field_wrng_message = wait.until(EC.presence_of_all_elements_located((By.XPATH, empty_field_wrng_msg)))
                assert len(empty_field_wrng_message) == 1
                severity_empty_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_severity_field_empty)))
                assert severity_empty_warning_msg.text == "* Please select the severity"
                cwe_empty_field = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_cwe_field_empty)))
                assert cwe_empty_field.text == "* A valid integer is required."
                create_manual_vul_pop_up_close = wait.until(EC.element_to_be_clickable((By.XPATH, close_create_manual_vul_pop_up)))
                create_manual_vul_pop_up_close.click()

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'Manual vul app')]")
