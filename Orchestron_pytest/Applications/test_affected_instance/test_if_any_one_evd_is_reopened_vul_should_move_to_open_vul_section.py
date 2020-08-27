from pytest import mark
from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_delete_application.delete_app import *
from Applications.test_affected_instance.close_all_ai_of_vuls import *


@mark.reopen_evd
class Check_If_Any_One_Evid_Is_Reopened_Then_Vul_Should_Move_To_Opened_Vul_Section_Tests:
    """
    This Testcase checks when all the affected instances are closed then vul should move to closed vulnerable section.
    """
    def test_create_app(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        create_apps(driver, application_name="close all ai", url="http://demo.com")

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_upload_scans(self, driver):
        upload_res(driver, application="//label[contains(text(),'close all ai')]", tool_name="OWASP Dependency Checker",
                   scan_name="owasp dependency checker", file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/OWASP Dependency Checker.xml")
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
        # waits until the Loading symbol is invisible
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    def test_close_all_ai(self, driver):
        close_all_ai(driver, app_name="//label[contains(text(),'close all ai')]")

    def test_reopen_any_one_evd_and_check_if_vul_is_moved_opened_status(self, driver, app_name="//label[contains(text(),'close all ai')]"):
        wait = WebDriverWait(driver, 30, poll_frequency=2, ignored_exceptions=[
            ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])

        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        select_individual_app.click()
        time.sleep(2)

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
        go_to_closed_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
        go_to_closed_vul_section.click()

        WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        per_page = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        per_page.click()
        select_All = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        select_All.click()
        time.sleep(2)

        number_of_closed_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='cell']/p")))
        print('Number of closed vulnerabilities: ', len(number_of_closed_vul))

        i = len(number_of_closed_vul)
        while i >= 1:
            wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
            go_to_closed_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
            go_to_closed_vul_section.click()

            wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            per_page_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
            per_page_dropdown.click()
            selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
            driver.execute_script("arguments[0].click();", selectAll)

            wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            time.sleep(1)
            click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='cell']/p")))
            click_on_individual_vul.click()

            WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            time.sleep(1)
            move_to_ai_section = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
            move_to_ai_section.click()
            time.sleep(2)  # This time.sleep helps to calculate the num of affected instance under individual vul

            for j in range(1, 2):
                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_individual_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH,
                   "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//header")))
                click_on_individual_affected_instance.click()
                time.sleep(1)

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_ai_action_dp = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='row']["+str(j)+"]//div[@class='col-sm-2']//div[@id='right']")))
                click_on_ai_action_dp.click()

                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                Reopen_evd = wait.until(EC.element_to_be_clickable((By.XPATH, reopen_evd)))
                Reopen_evd.click()

                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
                click_submit.click()

                success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_when_evd_reopened)))
                assert success_msg.text == "Evidence successfully reopened!"

                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
                go_to_closed_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
                go_to_closed_vul_section.click()
            i -= 1

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
        go_to_open_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        go_to_open_vul_section.click()

        number_of_opened_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        assert len(number_of_opened_vul) == len(number_of_closed_vul)

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'close all ai')]")
