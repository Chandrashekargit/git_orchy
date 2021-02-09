import time
from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Engagement_module_xpath import *
from spinner.spinner import *
from Engagements.test_create_eng.create_eng import *
from Applications.test_delete_application.delete_app import *

perpage_dp_options = "5\n10\n25\n50\n100\nAll"


@mark.basic_elements_for_scans
class CheckBasicUIOnEngTests:
    def test_create_eng(self, driver):
        create_apps(driver, application_name="demo1", url="http://demo.com")  # creates app
        create_engagement(driver, engagement_name="test basic UI", eng_descrption="demo", which_application="demo1", which_scope_type="All")    # creates eng

    def test_scans_section(self, driver, engagement_name_xpath="//label[contains(text(),'test basic UI')]"):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        stop_till_spinner_is_invisible(driver)
        click_on_individual_eng = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_name_xpath)))
        click_on_individual_eng.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        click_on_scans_section = wait.until(EC.element_to_be_clickable((By.XPATH, scans_section)))
        click_on_scans_section.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        perpage = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage.click()

        check_perpage_dropdown_all_options = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']")))
        time.sleep(1)
        assert check_perpage_dropdown_all_options.text == perpage_dp_options

        # checks for 'Search', 'Pagination', 'Name' options
        stop_till_spinner_is_invisible(driver)
        wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@aria-label='Pagination']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='scans_list']//th//div[.='Name']")))

    def test_delete_app(self, driver):
        delete_app(driver, application_xpath="//label[contains(text(),'demo1')]")
