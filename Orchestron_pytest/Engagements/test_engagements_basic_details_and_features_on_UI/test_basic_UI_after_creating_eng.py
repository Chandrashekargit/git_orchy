import time
from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Engagement_module_xpath import *
from spinner.spinner import *
from Engagements.test_create_eng.create_eng import *
from Applications.test_delete_application.delete_app import *


@mark.basic_elements_after_eng
class CheckBasicUIOnEngTests:
    def test_create_eng(self, driver):
        create_apps(driver, application_name="demo1", url="http://demo.com")  # creates app
        create_engagement(driver, engagement_name="test basic UI", eng_descrption="demo", which_application="demo1", which_scope_type="All")    # creates eng

    def test_basic_UI_elements(self, driver, engagement_name_xpath="//label[contains(text(),'test basic UI')]"):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        stop_till_spinner_is_invisible(driver)
        click_on_individual_eng = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_name_xpath)))
        click_on_individual_eng.click()

        # checks for name, app, desc, stat/stop date, bucket_type fields after creating eng
        name = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.='Name']")))
        assert name.text == "Name"
        app = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.='Application']")))
        assert app.text == "Application"
        desc = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.='Description']")))
        assert desc.text == "Description"
        start = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.='Start ']")))
        assert start.text == "Start"
        stop = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.='Stop ']")))
        assert stop.text == "Stop"
        action_dp = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Actions')]")))
        assert action_dp.text == "Actions"

        # checks for presence of pagination tab
        wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@aria-label='Pagination']")))

        # checks for presence of Dashboard, Scans, Vulnerabilities, Assign/Unassign scans sections
        dashboard = wait.until(EC.presence_of_element_located((By.XPATH, dashboard_section)))
        assert dashboard.text == "Dashboard"
        dashboard = wait.until(EC.presence_of_element_located((By.XPATH, scans_section)))
        assert dashboard.text == "Scans"
        dashboard = wait.until(EC.presence_of_element_located((By.XPATH, vulnerabilities_section)))
        assert dashboard.text == "Vulnerabilities"
        dashboard = wait.until(EC.presence_of_element_located((By.XPATH, assign_unassign_section)))
        assert dashboard.text == "Assign / Unassign Scans"

    def test_delete_app(self, driver):
        delete_app(driver, application_xpath="//label[contains(text(),'demo1')]")
