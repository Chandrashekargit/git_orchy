import time
from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Application_module_xpath import *
from spinner.spinner import *
from Applications.test_delete_application.delete_app import *

perpage_dp_options = "5\n10\n25\n50\n100\nAll"


@mark.app_ui_uncat_sec
class CheckBasicDetailsAndFeaturesOfApplicationUncategorizedVulSectionTests:
    def basic_func(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'All options')]")))
        click_on_individual_app.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        go_to_uncat_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, uncategorized_vulnerability)))
        go_to_uncat_vul_section.click()

        assert wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Uncategorized')]"))).text == "Uncategorized"

    def test_for_all_options_under_closed_vul_section(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        # creates application
        create_apps(driver, application_name="All options", url="http://demo.com")

        # goes to 'closed vulnerability' section of desired application
        self.basic_func(driver)

        # checks per-page dropdown and all its option
        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        perpage = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage.click()

        check_perpage_dropdown_all_options = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@x-placement]//ul")))
        time.sleep(1)
        assert check_perpage_dropdown_all_options.text == perpage_dp_options

        # checks for pagination, search, Name, CWE, Categorize sections on 'Open vulnerability section'
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col']//ul[@aria-label='Pagination']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='orchy_font_family orchy_font_color orchy_font_md el-input']//input[@placeholder='Search']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//th[2]//div[.='Name']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[.='CWE']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[.='Categorize']")))

    def test_delete_above_app(self, driver):
        delete_app(driver, application_xpath="//label[contains(text(), 'All options')]")
