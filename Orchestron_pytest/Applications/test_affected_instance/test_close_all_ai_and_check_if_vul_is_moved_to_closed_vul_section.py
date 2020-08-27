from pytest import mark
from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_delete_application.delete_app import *
from Applications.test_affected_instance.close_all_ai_of_vuls import *


@mark.all_ai_closed
class Check_If_All_Evidences_Are_Closed_hen_Vul_Should_Move_To_Closed_vul_Section_Tests:
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

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'close all ai')]")
