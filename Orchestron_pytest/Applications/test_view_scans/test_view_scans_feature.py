from pytest import mark
from Applications.test_delete_application.delete_app import delete_app
from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *

sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
             ]

sca_names = ["OWASP Dependency", "snyk", "whitesource", "Retire", "npm", "snyk"]


@mark.a
class ViewScansFeatureTests:
    # def test_create_app(self, driver):
    #     wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
    #         NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
    #
    #     create_apps(driver, application_name="close all ai", url="http://demo.com")
    #
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    #     success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
    #     assert success_msg.text == "Application has been created successfully!"
    #     wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))
    #
    # def test_upload_scans(self, driver):
    #     for (tool3, name3) in zip(sca_tools, sca_names):
    #         upload_res(driver, application="//label[contains(text(), 'Demo X')]", tool_name=name3, scan_name=name3,
    #                    file_loc=tool3)
    #
    #     WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
    #     # waits until the Loading symbol is invisible
    #     WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    def test_view_scans(self, driver, application="//label[contains(text(),'Demo C')]"):
        wait = WebDriverWait(driver, 15, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        stop_till_spinner_is_invisible(driver)
        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, application)))
        click_on_individual_app.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        action.click()

        select_view_scans = wait.until(EC.element_to_be_clickable((By.XPATH, view_scans)))
        select_view_scans.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(1)
        perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage_dp.click()
        sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        sel_all_option.click()
        stop_till_spinner_is_invisible(driver)

        try:
            scan_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='scans_list']//tr[@class='el-table__row']")))

            for i in range(1, len(scan_list)+1):
                click_on_individual_scan = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='scans_list']//tr[@class='el-table__row']["+str(i)+"]//p/label")))
                click_on_individual_scan.click()

                stop_till_spinner_is_invisible(driver)
                time.sleep(2)
                perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
                perpage_dp.click()
                sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
                sel_all_option.click()
                stop_till_spinner_is_invisible(driver)
                time.sleep(3)   # to load all the vulnerabilities

                for j in ["high", "medium", "low", "info"]:
                    try:
                        number_of_vul_via_severity_wise = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='"+j+"-vul-severity-circle']")))
                        count_of_severity = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='"+j+"-round orchy_font_family orchy_font_md']/span")))
                        assert str(len(number_of_vul_via_severity_wise)) == count_of_severity.text
                    except TimeoutException:
                        print("No vulnerabilities under **"+j+"** severity")
        except TimeoutException:
            print("Oops.. No scans available!")

