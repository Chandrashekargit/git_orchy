from pytest import mark
from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_delete_application.delete_app import *
from Applications.test_affected_instance.close_all_ai_of_vuls import *

# ba = Bulk actions


@mark.mark_vul_as_FP_via_ba
class BulkActionsTests:
    """
    This Testcase checks if we are able to mark vuls as FP via bulk actions.
    """
    # def test_create_app(self, driver):
    #     wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
    #         NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
    #
    #     create_apps(driver, application_name="bulk actions", url="http://demo.com")
    #
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    #     success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
    #     assert success_msg.text == "Application has been created successfully!"
    #     wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))
    #
    # def test_upload_scans(self, driver):
    #     upload_res(driver, application="//label[contains(text(),'bulk actions')]", tool_name="OWASP Dependency Checker",
    #                scan_name="owasp dependency checker", file_loc="/home/junaid/Downloads/Vishnu_orchestron_supported_tool_results/OWASP Dependency Checker.xml")
    #     WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
    #     # waits until the Loading symbol is invisible
    #     WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    def test_mark_vuls_as_FP(self, driver, app_name="//label[contains(text(),'bulk actions')]"):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])

        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        select_individual_app.click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        time.sleep(1)
        action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        action.click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        select_bulk_actions = wait.until(EC.element_to_be_clickable((By.XPATH, bulk_action)))
        select_bulk_actions.click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        per_page = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        per_page.click()
        select_All = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        select_All.click()
        time.sleep(2)

        num_of_TP_vuls = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tr[@class='el-table__row']//input[@type='checkbox']")))
        print(len(num_of_TP_vuls))

        for i in range(1, len(num_of_TP_vuls)+1):
            # selects all the checkboxes
            WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            driver.execute_script("window.scrollTo(0, 1000);")
            checkbox_all_TP_vul = driver.find_element_by_xpath("//tr[@class='el-table__row']["+str(i)+"]/td/div/div/label")
            checkbox_all_TP_vul.click()
            # checkbox_all_TP_vul = wait.until(EC.visibility_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(i)+"]//input[@type='checkbox']")))
            # driver.execute_script("arguments[0].click();", checkbox_all_TP_vul)

            click_submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))
            click_submit.click()

            confirm = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))
            confirm.click()

            WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, succes_msg_when_vuls_marked_as_FP_via_BA)))
            assert success_msg.text == "The vulnerabilities have been marked as False positive successfully!"

    # def test_delete_app(self, driver):
    #     delete_app(driver, application="//label[contains(text(),'bulk actions')]")
