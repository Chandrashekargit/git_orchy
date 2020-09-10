from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_manual_entry_scans.manual_entry import *
from xpath.reports_module_xpath import *
from pytest import mark
from spinner.spinner import *
from Applications.test_delete_application.delete_app import *

sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
             ]

sca_names = ["OWASP Dependency", "snyk", "whitesource", "Retire", "npm", "snyk"]


@mark.check_sev_filter
class reports_severity_count_Tests:
    """
    This Testcase checks the workflow of severity filter.
    """
    def test_create_app(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        create_apps(driver, application_name="check reports", url="http://demo.com")

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_upload_sca_results(self, driver):
        for (tool3, name3) in zip(sca_tools, sca_names):
            # calling the function 'upload_res' to upload all SCA scan's.
            upload_res(driver, application="//label[contains(text(), 'check reports')]", tool_name=name3, scan_name=name3, file_loc=tool3)

            # waits until the submit is invisible
            WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
            # waits until the Loading symbol is invisible
            WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    def test_goto_reports_section(self, driver, app_name="//label[contains(text(), 'check reports')]/../..//span[@class='el-checkbox__inner']"):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        go_to_reports_section = wait.until(EC.element_to_be_clickable((By.XPATH, reports_section)))
        go_to_reports_section.click()
        select_the_required_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        select_the_required_app.click()
        unselect_all_severities = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@style='min-height: 100%;']//div[@class='col-6']//span[@class='el-checkbox__inner']")))
        unselect_all_severities.click()

        for i in [high_sev, med_sev, low_sev, info_sev]:
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)
            select_severity = wait.until(EC.element_to_be_clickable((By.XPATH, i)))
            select_severity.click()

            # verify if all other severity count is zero apart from the selected one.
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)
            if i == high_sev:
                check_medium_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='medium-round']")))
                check_low_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='low-round']")))
                check_info_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info-round']")))
                assert check_medium_count.text == "0" and check_low_count.text == "0" and check_info_count.text == "0"
                unselect_high_sev = wait.until(EC.presence_of_element_located((By.XPATH, high_sev)))
                unselect_high_sev.click()
            elif i == med_sev:
                stop_till_spinner_is_invisible(driver)
                check_high_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='high-round']")))
                check_low_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='low-round']")))
                check_info_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info-round']")))
                assert check_high_count.text == "0" and check_low_count.text == "0" and check_info_count.text == "0"
                unselect_medium_sev = wait.until(EC.presence_of_element_located((By.XPATH, med_sev)))
                unselect_medium_sev.click()
            elif i == low_sev:
                stop_till_spinner_is_invisible(driver)
                check_high_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='high-round']")))
                check_medium_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='medium-round']")))
                check_info_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info-round']")))
                assert check_high_count.text == "0" and check_medium_count.text == "0" and check_info_count.text == "0"
                unselect_low_sev = wait.until(EC.presence_of_element_located((By.XPATH, low_sev)))
                unselect_low_sev.click()
            else:
                stop_till_spinner_is_invisible(driver)
                check_high_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='high-round']")))
                check_medium_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='medium-round']")))
                check_low_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='low-round']")))
                assert check_high_count.text == "0" and check_medium_count.text == "0" and check_low_count.text == "0"
                unselect_info_sev = wait.until(EC.presence_of_element_located((By.XPATH, info_sev)))
                unselect_info_sev.click()

    def test_affected_instance_sev(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        for (a, b) in zip([high_sev, med_sev, low_sev, info_sev], [1, 2, 3, 4]):
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)
            select_severity = wait.until(EC.element_to_be_clickable((By.XPATH, a)))
            select_severity.click()

            # verify if all other severity count is zero apart from the selected one.
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)

            try:
                stop_till_spinner_is_invisible(driver)
                move_to_last_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to last page']")))
                move_to_last_page.click()

                get_the_max_len_of_pagination = wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='page-item active']"))).text
                stop_till_spinner_is_invisible(driver)
                move_to_first_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to first page']")))
                move_to_first_page.click()

                for j in range(1, int(get_the_max_len_of_pagination)+1):
                    select_pagination = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to page "+str(j)+"']")))
                    select_pagination.click()
                    time.sleep(2)
                    severity_selected = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='group']/div[@class='row']//div[@class='col-sm-6']["+str(b)+"]/label//span[2]/label")))
                    get_the_count_of_number_of_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card mb-1']")))
                    for k in range(1, len(get_the_count_of_number_of_vul)+1):
                        severity_of_vul = wait.until(EC.presence_of_element_located((By.XPATH,
                                         "//div[@class='card mb-1']["+str(k)+"]"
                                         "//span[@class='badge high move_right orchy_font_family  orchy_font_sm badge-secondary' "
                                         "or @class='badge medium move_right orchy_font_family  orchy_font_sm badge-secondary' "
                                         "or @class='badge low move_right orchy_font_family  orchy_font_sm badge-secondary' "
                                         "or @class='badge info move_right orchy_font_family  orchy_font_sm badge-secondary']")))
                        print(severity_of_vul.text)
                        assert severity_of_vul.text == severity_selected.text
            except TimeoutException:
                stop_till_spinner_is_invisible(driver)
                severity_selected = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='group']/div[@class='row']//div[@class='col-sm-6']["+str(b)+"]/label//span[2]/label")))
                try:
                    get_the_count_of_number_of_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card mb-1']")))

                    for l in range(1, len(get_the_count_of_number_of_vul)+1):
                        stop_till_spinner_is_invisible(driver)
                        severity_of_vul = wait.until(EC.presence_of_element_located((By.XPATH,
                                         "//div[@class='card mb-1']["+str(l)+"]"
                                         "//span[@class='badge high move_right orchy_font_family  orchy_font_sm badge-secondary' "
                                         "or @class='badge medium move_right orchy_font_family  orchy_font_sm badge-secondary' "
                                         "or @class='badge low move_right orchy_font_family  orchy_font_sm badge-secondary' "
                                         "or @class='badge info move_right orchy_font_family  orchy_font_sm badge-secondary']")))
                        print(severity_of_vul.text)
                        assert severity_of_vul.text == severity_selected.text
                except TimeoutException:
                    print("No vulnerabilities present under: ", severity_selected.text)
                    
            stop_till_spinner_is_invisible(driver)
            unselect_severity = wait.until(EC.element_to_be_clickable((By.XPATH, a)))
            unselect_severity.click()

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'check reports')]")
