from Applications.test_create_applications.create_app import create_apps
from Applications.test_upload_scans.test_upload_results import *
from Applications.test_delete_application.delete_app import *
from pytest import mark


@mark.close_evd
class CloseEvdTests:
    def test_create_application(self, driver):
        create_apps(driver, application_name="App_to_check_evd", url="http://demo.com")

    def test_upload_scan(self, driver):
        # NOTE: To parse all results it takes some time.
        upload_res(driver, application="//label[contains(text(), 'App_to_check_evd')]", tool_name="npm",
                   file_loc="/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json")

    def test_close_and_reopen_evd(self, driver, app_name="//label[contains(text(), 'App_to_check_evd')]"):
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        wait1 = WebDriverWait(driver, 10)

        # Click on Application section
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        select_individual_app.click()

        # Clicks on Open vulnerability of individual application
        open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        open_vul.click()

        # Clicks Per-page drop-down and selects 'All'.
        perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage_dp.click()
        sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        sel_all_option.click()
        time.sleep(2)

        # gives the total count of vulnerabilities present under open vulnerability for individual application
        vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print('\nTotal number of vul: ', len(vul))

        for i in range(1, len(vul)+1):
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
            open_vul.click()

            # clicks on individual vul
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            click_on_individual_vul = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
            print('vulnerability name: ', click_on_individual_vul.text)
            click_on_individual_vul.click()

            # moves to affected instance Section
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            move_to_ai = wait.until(EC.presence_of_element_located((By.XPATH, affected_instance)))
            move_to_ai.click()

            # Gives the count of total number of affected instances under individual vulnerability.
            affected_inst = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']//div[contains(text(),'Actions')]")))
            print('Total number of affected_instance: ', len(affected_inst))

            for j in range(1, len(affected_inst)+1):
                click_on_individual_action_dp = wait1.until(EC.element_to_be_clickable((By.XPATH,
                    "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//div[contains(text(),'Actions')]")))
                click_on_individual_action_dp.click()

                select_close_evd = wait1.until(EC.element_to_be_clickable((By.XPATH, close_evdience)))
                select_close_evd.click()

                justi = wait1.until(EC.element_to_be_clickable((By.XPATH, justification)))
                justi.send_keys("qwerty")

                submit = wait1.until(EC.presence_of_element_located((By.XPATH, app_submit)))
                submit.click()
                wait1.until(EC.invisibility_of_element((By.XPATH, app_submit)))
                wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

                if j == len(affected_inst):
                    break

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'App_to_check_evd')]")
