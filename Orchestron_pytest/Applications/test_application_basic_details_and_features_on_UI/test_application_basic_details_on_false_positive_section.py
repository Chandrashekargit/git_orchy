from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Application_module_xpath import *
from spinner.spinner import *
from Applications.test_delete_application.delete_app import *

perpage_dp_options = "5\n10\n25\n50\n100\nAll"


@mark.app_ui_false_positive_sec
class CheckBasicDetailsAndFeaturesOfApplicationOpenVulSectionTests:
    def basic_func(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'All options')]")))
        click_on_individual_app.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        go_to_false_positive_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, false_positive)))
        go_to_false_positive_vul_section.click()

        assert wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'False Positive')]"))).text == "False Positive"

    def test_for_filters_feature(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        create_apps(driver, application_name="All options", url="http://demo.com")

        self.basic_func(driver)
        # checks for pagination, search, Name, CWE sections on 'Open vulnerability section'
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col']//ul[@aria-label='Pagination']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='orchy_font_family orchy_font_color orchy_font_md el-input']//input[@placeholder='Search']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//th[2]//div[.='Name']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[.='CWE']")))

    def test_delete_above_app(self, driver):
        delete_app(driver, application_xpath="//label[contains(text(), 'All options')]")
