from Applications.test_create_evd.create_evd import *
from Applications.test_create_applications.create_app import *
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_delete_application.delete_app import *
from pytest import mark

line_nos = [" ", "12345", "abc@!", " ", " ", "1"*6, "1"]
line_ranges = [" ", " ", "125-369", " ", " ", "6"*16, "1"]
code_snippets = ["/home/junaid/Pictures/we45.png", "/home/junaid/Downloads/results_supported_by_orchy/zap.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json", "/home/junaid/demo.pdf",
             "/home/junaid/demo.docx", "/home/junaid/Desktop/Response.txt", "/home/junaid/Desktop/response_empty_file.txt"]
paths = [" ", " ", "/bin/source/activate", " ", " ", "q"*121, "."]
files = [" ", " ", " ", "chandu.py", " ", "chandrashekar2.py", "a"]
params = [" ", " ", " ", " ", "arg1!=1", "q2"*7, "1"]


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

    def test_create_manual_evd_assert_wrng_msg(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        open_manual_vulnerability(driver, individual_vul_xpath="//tbody/tr/td[2]//div[@class='col']/p")

        for (line_num, line_Range, Code_snippet, Path, File, Param) in zip(line_nos, line_ranges, code_snippets, paths, files, params):
            if Code_snippet == "/home/junaid/Pictures/we45.png":
                sast_evd(driver, line_no=line_num, line_range=line_Range, code_snippet_location=Code_snippet, path=Path, file_name=File, param=Param)
                sast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(sast_wrng_msg) == 4
                line_no_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_for_empty_line_no)))
                assert len(line_no_wrng_msg) == 1
                code_snippet_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, code_snippet_wrng_msg_for_invalid_file)))
                assert len(code_snippet_wrng_msg) == 1
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif line_num == "12345":
                sast_evd(driver, line_no=line_num, line_range=line_Range, code_snippet_location=Code_snippet, path=Path, file_name=File, param=Param)
                sast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(sast_wrng_msg) == 4
                code_snippet_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, code_snippet_wrng_msg_for_invalid_file)))
                assert len(code_snippet_wrng_msg) == 1
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif line_Range == "125-369" or Path == "/bin/source/activate" or File == "chandu.py" or Param == "arg1!=1":
                sast_evd(driver, line_no=line_num, line_range=line_Range, code_snippet_location=Code_snippet, path=Path, file_name=File, param=Param)
                sast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(sast_wrng_msg) == 3
                line_no_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_for_empty_line_no)))
                assert len(line_no_wrng_msg) == 1
                code_snippet_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, code_snippet_wrng_msg_for_invalid_file)))
                assert code_snippet_wrng_msg.text == "* Please upload only text files"
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            elif line_num == "1"*6:
                sast_evd(driver, line_no=line_num, line_range=line_Range, code_snippet_location=Code_snippet, path=Path, file_name=File, param=Param)
                sast_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_fields_are_empty)))
                assert len(sast_wrng_msg) == 4
                line_no_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, wrng_msg_when_line_no_reaches_max_char)))
                assert line_no_wrng_msg.text == "* Line number cannot exceed more than 5 digits"
                close_dast_evd_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, close_evd_pop_up)))
                close_dast_evd_pop_up.click()

            else:
                sast_evd(driver, line_no=line_num, line_range=line_Range, code_snippet_location=Code_snippet, path=Path, file_name=File, param=Param)
                code_snippet_wrng_msg = wait.until(EC.presence_of_all_elements_located((By.XPATH, empty_file_wrng_msg)))
                assert len(code_snippet_wrng_msg) == 2
