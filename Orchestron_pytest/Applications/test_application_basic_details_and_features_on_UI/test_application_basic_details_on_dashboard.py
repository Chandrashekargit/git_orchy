import time
from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Application_module_xpath import *
from spinner.spinner import *
from Applications.test_delete_application.delete_app import *

app_labels = [app_name_label, app_url_label, app_platform_label, app_team_label, app_hard_mark_false_postive_label, app_BT_label, app_BT_project_label, dashboard, open_vulnerability, closed_vulnerability, uncategorized_vulnerability, false_positive, action_dropdown]
its_texts = ["Application", "URL", "Platform", "Team", "Hard Mark False Positive", "Bug Tracker", "Bug Tracker Project", "Dashboard", "Opened", "Closed", "Uncategorized", "False Positive", "Actions"]
action_dropdown_texts = "Update\nUpload Results\nManual Entry\nView Scans\nBulk Actions\nCopy Webhook\nShow Webhook\nBug Tracker\nEnable Hard Mark False Positive\nView Report\nVulnerability Profile\nDelete"


@mark.app_ui_basic_details
class CheckBasicDetailsOfApplicationDashboardTests:
    """
        > checks for basic things on UI when application is created
        > checks if 'Action' dropdown has all options
        > checks if application has all section like "Dashboard", "opened", "closed", "Pagination" etc
    """
    def test_if_application_has_all_features_and_options(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        create_apps(driver, application_name="All options", url="https://demo.com")

        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'All options')]")))
        click_on_individual_app.click()

        # checks for pagination feature visibility on 'List of Application' section
        stop_till_spinner_is_invisible(driver)
        wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@aria-label='Pagination']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

        # check if Application has all the required details and options.
        stop_till_spinner_is_invisible(driver)
        for (app_label, its_text) in zip(app_labels, its_texts):
            application_details = wait.until(EC.presence_of_element_located((By.XPATH, app_label)))
            assert application_details.text == its_text

        click_on_action_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        click_on_action_dropdown.click()

        action_dropdown_option = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@x-placement]")))
        assert action_dropdown_option.text == action_dropdown_texts

    def test_if_all_section_are_visible_on_dashboard(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'All options')]")))
        click_on_individual_app.click()

        stop_till_spinner_is_invisible(driver)
        open_section = wait.until(EC.presence_of_element_located((By.XPATH, "//span[.='Open']")))
        assert open_section.text == "Open"

        close_section = wait.until(EC.presence_of_element_located((By.XPATH, "//span[.='Closed']")))
        assert close_section.text == "Closed"

        uncat_section = wait.until(EC.presence_of_element_located((By.XPATH, "//span[.='Uncategorized']")))
        assert uncat_section.text == "Uncategorized"

        avg_days = wait.until(EC.presence_of_element_located((By.XPATH, "//span[.='Average Days']")))
        assert avg_days.text == "Average Days"

        list_of_app_tag = wait.until(EC.presence_of_element_located((By.XPATH, "//p[.=' List of Applications ']")))
        assert list_of_app_tag.text == "List of Applications"

    def test_delete_above_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'All options')]")
