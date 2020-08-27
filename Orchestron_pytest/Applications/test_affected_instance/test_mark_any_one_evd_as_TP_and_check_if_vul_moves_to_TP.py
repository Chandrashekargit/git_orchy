from pytest import mark
from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_delete_application.delete_app import *
from Applications.test_affected_instance.mark_all_ai_as_fp import *


@mark.TP
class Check_If_Any_One_Evidences_Marked_As_TP_then_Vul_Should_Move_To_TP_Section_Tests:
    """
    This Testcase checks when all the affected instances are marked as FP then vul should move to FP section.
    """
    def test_create_app(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        create_apps(driver, application_name="Manual vul app", url="http://demo.com")

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_upload_scans(self, driver):
        upload_res(driver, application="//label[contains(text(),'Manual vul app')]", tool_name="OWASP Dependency Checker",
           scan_name="owasp dependency checker", file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/OWASP Dependency Checker.xml")
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
        # waits until the Loading symbol is invisible
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    def test_mark_all_evidences_as_FP(self, driver):
        mark_all_evidences_as_FP(driver, app_name="//label[contains(text(),'Manual vul app')]")

    def test_mark_any_one_evd_as_TP_and_check_if_vul_moves_to_TP(self, driver, app_xpath="//label[contains(text(),'Manual vul app')]"):
        wait = WebDriverWait(driver, 30, poll_frequency=2, ignored_exceptions=[
            ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])

        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_xpath)))
        select_individual_app.click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        go_to_fp_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.='False Positive']")))
        go_to_fp_section.click()
        time.sleep(2)

        number_of_fp_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print("Number of False positive vulnerabilities: ", len(number_of_fp_vul))

        i = len(number_of_fp_vul)
        while i >= 1:
            wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
            go_to_fp_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.='False Positive']")))
            go_to_fp_section.click()

            wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            time.sleep(1)
            per_page_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
            per_page_dropdown.click()
            selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
            driver.execute_script("arguments[0].click();", selectAll)

            vul_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
            a = vul_name.text

            wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
            click_on_individual_vul.click()

            WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            time.sleep(1)
            move_to_ai_section = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
            move_to_ai_section.click()
            time.sleep(2)

            for j in range(1, 2):
                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_individual_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH,
                   "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//header")))
                click_on_individual_affected_instance.click()
                time.sleep(1)

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_ai_action_dp = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='row']["+str(j)+"]//div[@class='col-sm-2']//div[@id='right']")))
                click_on_ai_action_dp.click()

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                mark_ai_as_TP = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@x-placement]//li[@tabindex='-1'][1]")))
                mark_ai_as_TP.click()

                success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_when_evd_marked_as_TP)))
                assert success_msg.text == "Evidence successfully marked as True Positive!"
                wait.until(EC.invisibility_of_element((By.XPATH, success_msg_when_evd_marked_as_TP)))
            i -= 1

        number_of_TP_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        assert len(number_of_fp_vul) == len(number_of_TP_vul)

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'Manual vul app')]")
