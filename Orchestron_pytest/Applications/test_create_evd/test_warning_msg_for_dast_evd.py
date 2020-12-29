from Applications.test_create_evd.create_evd import *
from Applications.test_create_applications.create_app import *
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_delete_application.delete_app import *
from pytest import mark
from spinner.spinner import *

urls = [" ", "http://deo.com", " ", " ", "http://demo!2.com", " ", " ", " "]
params = [" ", " ", "arg1", " ", "argument12345", "!@#$", "123456", " "]
payloads = [" ", " ", " ", "a!=1", "<name:chandu>", "!@#$", "123456", " "]

requests = ["/home/junaid/Pictures/we45.png", "/home/junaid/Downloads/results_supported_by_orchy/zap.xml",
            "/home/junaid/Downloads/results_supported_by_orchy/snyk.json", "/home/junaid/demo.pdf",
            "/home/junaid/demo.docx", "/home/junaid/Pictures/we45.png",
            "/home/junaid/Desktop/request.txt", "/home/junaid/Desktop/request_empty_file.txt"]

responses = ["/home/junaid/Pictures/we45.png", "/home/junaid/Downloads/results_supported_by_orchy/zap.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json", "/home/junaid/demo.pdf",
             "/home/junaid/demo.docx", "/home/junaid/demo.docx",
             "/home/junaid/Desktop/Response.txt", "/home/junaid/Desktop/response_empty_file.txt"]


@mark.warning_msgs_for_dast
class CreateEvidenceTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="test_to_create_manual_evd", url="http://QWERTY123.com")

    def test_create_manual_vul(self, driver):
        create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'test_to_create_manual_evd')]",
                          scan_name="Manual vul", Severity="Low", cwe_num="89:Sql", Descrption="This is manual vul")

    def test_create_manual_evd_and_assert_wrng_msgs_for_empty_fields(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p",
                                  application_name_xpath="//label[contains(text(), 'test_to_create_manual_evd')]")
        stop_till_spinner_is_invisible(driver)
        click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
        click_on_create_evd_btn.click()

        stop_till_spinner_is_invisible(driver)
        dast_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, dast_toggle_btn)))
        dast_evd_enable.click()

        stop_till_spinner_is_invisible(driver)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
        driver.execute_script("arguments[0].click();", submit)

        dast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
        assert len(dast_wrng_msg) == 3
        req_res_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, req_res_wrng_msg_for_empty_fields)))
        assert len(req_res_wrng_msg) == 2

        close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
        close_dast_evd_pop_up.click()
        driver.refresh()

    def test_create_manual_evd_assert_wrng_msg(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p",
                                  application_name_xpath="//label[contains(text(), 'test_to_create_manual_evd')]")

        for (url, param, payload, request, response) in zip(urls, params, payloads, requests, responses):
            if request and response == "/home/junaid/Pictures/we45.png":
                dast_evd(driver, enter_url=url, enter_param=param, enter_payload=payload, req_file_loc=request, response_file_loc=response)
                dast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(dast_wrng_msg) == 3
                req_res_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, req_res_wrng_msg_for_invalid_files)))
                assert len(req_res_wrng_msg) == 2
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif url == "http://deo.com" or param == "arg1" or payload == "a!=1":
                dast_evd(driver, enter_url=url, enter_param=param, enter_payload=payload, req_file_loc=request, response_file_loc=response)
                dast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(dast_wrng_msg) == 2
                req_res_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, req_res_wrng_msg_for_invalid_files)))
                assert len(req_res_wrng_msg) == 2
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif url == "http://demo!2.com":
                dast_evd(driver, enter_url=url, enter_param=param, enter_payload=payload, req_file_loc=request, response_file_loc=response)
                dast_url_wrng_msg = wait.until(EC.presence_of_element_located((By.XPATH, invalid_url_wrng_msg)))
                assert dast_url_wrng_msg.text == "* Enter a valid URL."
                param_payload_max_char = wait.until(EC.presence_of_all_elements_located((By.XPATH, param_payload_reaching_max_char)))
                assert len(param_payload_max_char) == 2
                req_res_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, req_res_wrng_msg_for_invalid_files)))
                assert len(req_res_wrng_msg) == 2
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif param and payload == "!@#$":
                dast_evd(driver, enter_url=url, enter_param=param, enter_payload=payload, req_file_loc=request, response_file_loc=response)
                dast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(dast_wrng_msg) == 1
                req_res_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, req_res_wrng_msg_for_invalid_files)))
                assert len(req_res_wrng_msg) == 2
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif request == "/home/junaid/Desktop/request_empty_file.txt":
                dast_evd(driver, enter_url=url, enter_param=param, enter_payload=payload, req_file_loc=request, response_file_loc=response)
                dast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(dast_wrng_msg) == 3
                req_res_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, empty_file_wrng_msg)))
                assert len(req_res_wrng_msg) == 2
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            else:
                dast_evd(driver, enter_url=url, enter_param=param, enter_payload=payload, req_file_loc=request, response_file_loc=response)
                dast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(dast_wrng_msg) == 1
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'test_to_create_manual_evd')]")
