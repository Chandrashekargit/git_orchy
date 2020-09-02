from pytest import mark
from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_delete_application.delete_app import *
from Applications.test_affected_instance.close_all_ai_of_vuls import *
from Applications.test_upload_scans.test_DAST_results_upload import *

dast_tools = [("/home/junaid/Downloads/results_supported_by_orchy/zap.xml", "ZAP (json,xml)"),
              ("/home/junaid/Downloads/results_supported_by_orchy/burp.xml", "Burp (json,xml)"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Arachni.json", "arachni"),
              ("/home/junaid/Downloads/results_supported_by_orchy/AppScan_DAST.xml", "AppScan - DAST"),
              ("/home/junaid/Downloads/results_supported_by_orchy/w3af.xml", "w3af"),
              ("/home/junaid/Downloads/results_supported_by_orchy/Acunetix.xml", "acunetix"),
              ("/home/junaid/Downloads/results_supported_by_orchy/appspider.xml", "appspider")]


@mark.perpage
class PerPageDropdownTests:
    """
    Checks if 'Number of vuls' matches per-page dropdown option selected.
    Make sure you have a application with more than 100 vulnerabilities.
    """
    def test_for_perpage_dropdown(self, driver, app_name):
        """
        :param app_name: give the xpath of the application
        """
        wait = WebDriverWait(driver, 30, poll_frequency=2, ignored_exceptions=[
            ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])

        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        select_individual_app.click()
        time.sleep(2)

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
        go_to_open_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        go_to_open_vul_section.click()

        for i, j in zip([five, ten, twenty_five, fifty, hundered], [5, 10, 25, 50, 100]):
            WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            per_page = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
            per_page.click()
            time.sleep(2)
            select_All = wait.until(EC.element_to_be_clickable((By.XPATH, i)))
            select_All.click()
            time.sleep(2)

            number_of_open_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
            assert len(number_of_open_vul) == j
