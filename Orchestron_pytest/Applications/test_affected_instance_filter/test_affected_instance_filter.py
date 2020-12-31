from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from xpath.Application_module_xpath import *
from Applications.test_delete_application.delete_app import *
from spinner.spinner import *
import time
from pytest import mark

tool_names = ["npm", "ZAP (json,xml)", "hp", "Openvas (xml)", "Aquasec (json)"]
file_locs = ["/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json",
             "/home/junaid/Downloads/results_supported_by_orchy/zap.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/HP.xml",
             "/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/Openvas_63.94.64.36.xml",
             "/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/aquasec_api.json"]

sast_tools = ["Tool: Checkmarx", "Tool: FindSecBugs", "Tool: GoSec", "Tool: Brakeman", "Tool: Bandit", "Tool: NodeJsScan",
              "Tool: Xanitizer", "Tool: FindSecBugs", "Tool: HP Fortify", "Tool: Veracode", "Tool: GoSec"]
dast_tools = ["Tool: Burp", "Tool: ZAP", "Tool: Arachani", "Tool: Appspider", "Tool: w3af", "Tool: Acunetix"]
sca_tools = ["Tool: RetireJS", "Tool: OWASP Dependency Checker", "Tool: Snyk", "Tool: Whitesource", "Tool: RetireJS", "Tool: NpmAudit"]
container_tools = ["Container (Aquasec)"]
infra_tools = ["Infra (Openvas)"]
cloud_tools = []


@mark.ai_filter
class CheckAffectedInstanceFiltersTests:
    """
    This testcase lets us check the Affected Instance filter.
    For eg: If user selects 'SCA' Filter option and if it has
    any affected instance(s) it checks the tool name and asserts if the tool name == SCA section tool name.
    """
    def test_create_application(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=1)
        create_apps(driver, application_name="check_ai_filter", url="http://demo.com")

        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_upload_scan(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2)

        # NOTE: To parse all results it takes some time. so, please upload small files.
        for (i, k) in zip(tool_names, file_locs):
            upload_res(driver, application="//label[contains(text(), 'check_ai_filter')]", tool_name=i, scan_name=i,
                       file_loc=k)

            stop_till_spinner_is_invisible(driver)
            wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
            wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))

        time.sleep(100)     # to let all the results parse
        driver.refresh()

    def test_check_ai_filter(self, driver, application_name="//label[contains(text(), 'check_ai_filter')]"):
        wait = WebDriverWait(driver, 20, poll_frequency=2)

        # Click on Application section
        stop_till_spinner_is_invisible(driver)
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        # select the required application
        stop_till_spinner_is_invisible(driver)
        select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, application_name)))
        select_individual_app.click()

        # Clicks on Open vulnerability of individual application
        stop_till_spinner_is_invisible(driver)
        open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        open_vul.click()

        for i in range(1, 11):
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)
            open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
            open_vul.click()

            # clicks on individual vul
            stop_till_spinner_is_invisible(driver)
            click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
            # print('vulnerability name: ', click_on_individual_vul.text)
            click_on_individual_vul.click()

            # # wait till Vulnerability info section is visible
            # stop_till_spinner_is_invisible(driver)
            # wait.until(EC.visibility_of_element_located((By.XPATH, vul_info)))
            #
            # # wait till affected instance section is visible
            # stop_till_spinner_is_invisible(driver)
            # wait.until(EC.visibility_of_element_located((By.XPATH, affected_instance)))

            # moves to affected instance Section
            stop_till_spinner_is_invisible(driver)
            time.sleep(4)
            move_to_ai = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
            move_to_ai.click()

            for j in [select_all_filter, sca_filter, sast_filter, dast_filter, container_filter, infra_filter, cloud_filter]:
                stop_till_spinner_is_invisible(driver)
                time.sleep(1)
                select_filter_option = wait.until(EC.visibility_of_element_located((By.XPATH, j)))
                select_filter_option.click()
                stop_till_spinner_is_invisible(driver)
                try:
                    stop_till_spinner_is_invisible(driver)
                    no_data_visibility = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'No data')]")))
                    assert no_data_visibility.text == "No data"
                except TimeoutException:
                    stop_till_spinner_is_invisible(driver)
                    total_no_of_ai = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@id='instance_button']")))
                    for k in range(1, len(total_no_of_ai)+1):
                        click_on_individual_ai = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(k)+"]//a[@id]")))
                        click_on_individual_ai.click()
                        if j == sca_filter:
                            stop_till_spinner_is_invisible(driver)
                            grab_tool_name1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='row']["+str(k)+"]//div[@class='list-group']//span[@style='float: right;']")))
                            print(grab_tool_name1.text)
                            time.sleep(1)
                            assert grab_tool_name1.text in sca_tools
                        elif j == sast_filter:
                            stop_till_spinner_is_invisible(driver)
                            grab_tool_name2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='row']["+str(k)+"]//div[@class='list-group']//span[@style='float: right;']")))
                            print(grab_tool_name2.text)
                            time.sleep(1)
                            assert grab_tool_name2.text in sast_tools
                        elif j == dast_filter:
                            stop_till_spinner_is_invisible(driver)
                            grab_tool_name3 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='row']["+str(k)+"]//div[@class='list-group']//span[@style='float: right;']")))
                            print(grab_tool_name3.text)
                            time.sleep(1)
                            assert grab_tool_name3.text in dast_tools
                        elif j == infra_filter:
                            stop_till_spinner_is_invisible(driver)
                            grab_tool_name4 = wait.until(EC.presence_of_element_located((By.XPATH, "//b[.='Infra (Openvas)']")))
                            print(grab_tool_name4.text)
                            time.sleep(1)
                            assert grab_tool_name4.text in infra_tools
                        elif j == container_filter:
                            stop_till_spinner_is_invisible(driver)
                            grab_tool_name4 = wait.until(EC.presence_of_element_located((By.XPATH, "//b[.='Container (Aquasec)']")))
                            print(grab_tool_name4.text)
                            time.sleep(1)
                            assert grab_tool_name4.text in infra_tools
                if j != select_all_filter:
                    stop_till_spinner_is_invisible(driver)
                    select_filter_option = wait.until(EC.visibility_of_element_located((By.XPATH, j)))
                    select_filter_option.click()

            stop_till_spinner_is_invisible(driver)
            open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Opened')]")))
            open_vul.click()
            driver.refresh()

    def test_delete_app(self, driver):
        delete_app(driver, application_xpath="//label[contains(text(), 'check_ai_filter')]")
