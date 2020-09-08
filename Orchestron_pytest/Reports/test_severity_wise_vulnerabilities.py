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


@mark.a
class reports_severity_wise_Tests:
    """
    This Testcase checks when all the affected instances are closed then vul should move to closed vulnerable section.
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

    def test_goto_reports_section(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        go_to_reports_section = wait.until(EC.element_to_be_clickable((By.XPATH, reports_section)))
        go_to_reports_section.click()

        unselect_all_severities = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@style='min-height: 100%;']//div[@class='col-6']//span[@class='el-checkbox__inner']")))
        unselect_all_severities.click()

        for i in [high_sev, med_sev, low_sev, info_sev]:
            select_high = wait.until(EC.element_to_be_clickable((By.XPATH, i)))
            select_high.click()

            # verify if all other severity count is zero
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)
            if i == high_sev:
                medium_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='medium-round']")))
                low_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='low-round']")))
                info_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info-round']")))
                assert medium_count.text == "0" and low_count.text == "0" and info_count.text == "0"
                high_count = wait.until(EC.presence_of_element_located((By.XPATH, high_sev)))
                high_count.click()
            elif i == med_sev:
                stop_till_spinner_is_invisible(driver)
                high_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='high-round']")))
                low_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='low-round']")))
                info_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info-round']")))
                assert high_count.text == "0" and low_count.text == "0" and info_count.text == "0"
                medium_count = wait.until(EC.presence_of_element_located((By.XPATH, med_sev)))
                medium_count.click()
            elif i == low_sev:
                stop_till_spinner_is_invisible(driver)
                high_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='high-round']")))
                medium_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='medium-round']")))
                info_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info-round']")))
                assert high_count.text == "0" and medium_count.text == "0" and info_count.text == "0"
                low_count = wait.until(EC.presence_of_element_located((By.XPATH, low_sev)))
                low_count.click()
            else:
                stop_till_spinner_is_invisible(driver)
                high_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='high-round']")))
                medium_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='medium-round']")))
                low_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='low-round']")))
                assert high_count.text == "0" and medium_count.text == "0" and low_count.text == "0"

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'check reports')]")
