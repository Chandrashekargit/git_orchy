import time
from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Application_module_xpath import *
from spinner.spinner import *
from Applications.test_delete_application.delete_app import *

perpage_dp_options = "5\n10\n25\n50\n100\nAll"
filter_section = ["CWE", "Severity", "Ageing", "Tool"]
filter_severity_options = [filter_severity_high, filter_severity_medium, filter_severity_low, filter_severity_info]
filter_severity_texts = ["High", "Medium", "Low", "Info"]
filter_ageing_options = [filter_ageing1, filter_ageing2, filter_ageing3, filter_ageing4, filter_ageing5, filter_ageing6, filter_ageing7]
filter_ageing_texts = ['0-5 days', '6-10 days', '11-20 days', '21-40 days', '41-80 days', '81-100 days', 'More than 100 days']


@mark.app_ui_open_vul
class CheckBasicDetailsAndFeaturesOfApplicationOpenVulSectionTests:
    def basic_func(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'All options')]")))
        click_on_individual_app.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        go_to_open_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        go_to_open_vul_section.click()

    def test_for_all_options_and_features_under_open_vul_section(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        create_apps(driver, application_name="All options", url="http://demo.com")

        self.basic_func(driver)

        # checks per-page dropdown and all its option
        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        perpage = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage.click()

        check_perpage_dropdown_all_options = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']")))
        time.sleep(1)
        assert check_perpage_dropdown_all_options.text == perpage_dp_options

        # checks for 'Search' feature
        wait.until(EC.presence_of_element_located((By.XPATH, search)))

    def test_for_filters_feature(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        self.basic_func(driver)
        # checks for pagination, search, Name, CWE sections on 'Open vulnerability section'
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col']//ul[@aria-label='Pagination']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='orchy_font_family orchy_font_color orchy_font_md el-input']//input[@placeholder='Search']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//th[2]//div[.='Name']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[.='CWE']")))

        stop_till_spinner_is_invisible(driver)
        time.sleep(1)
        click_filter_btn = wait.until(EC.element_to_be_clickable((By.XPATH, filter_option_btn)))
        click_filter_btn.click()

        # checks for visibility of CWE, Severity, Ageing, Tool Section
        stop_till_spinner_is_invisible(driver)
        for (header, header_text) in zip([cwe_tag, severity_tag, ageing_tag, tool_tag], filter_section):
            checks_for_all_filter_sections = wait.until(EC.presence_of_element_located((By.XPATH, header)))
            assert checks_for_all_filter_sections.text == header_text

        # checks for 'Filter Severity options'
        for (filter_severity_option, filter_severity_text) in zip(filter_severity_options, filter_severity_texts):
            checks_for_severity_filter_option = wait.until(EC.presence_of_element_located((By.XPATH, filter_severity_option)))
            assert checks_for_severity_filter_option.text == filter_severity_text

        # checks if all filter severity options can be selected and unselected via checkbox
        for (filter_ageing_option, filter_ageing_text) in zip(filter_ageing_options, filter_ageing_texts):
            checks_for_severity_ageing_option = wait.until(EC.presence_of_element_located((By.XPATH, filter_ageing_option)))
            assert checks_for_severity_ageing_option.text == filter_ageing_text

    def test_if_filter_severity_options_can_be_checked_and_unchecked(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        self.basic_func(driver)

        stop_till_spinner_is_invisible(driver)
        time.sleep(1)
        click_filter_btn = wait.until(EC.element_to_be_clickable((By.XPATH, filter_option_btn)))
        click_filter_btn.click()

        # checks filter severity options
        for i in range(1, 5):
            check_sev_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='group'][1]//div[@class='col-sm-12']["+str(i)+"]//span[@class='el-checkbox__input']")))
            check_sev_filter.click()
        assert wait.until(EC.invisibility_of_element((By.XPATH, "//div[@role='group'][1]//div[@class='col-sm-12']//span[@class='el-checkbox__input']")))

        # unchecks filter severity options
        for i in range(1, 5):
            uncheck_sev_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='group'][1]//div[@class='col-sm-12']["+str(i)+"]//span[@class='el-checkbox__input is-checked']")))
            uncheck_sev_filter.click()
        assert wait.until(EC.invisibility_of_element((By.XPATH, "//div[@role='group'][1]//div[@class='col-sm-12']//span[@class='el-checkbox__input is-checked']")))

    def test_if_filter_ageing_options_can_be_checked_and_unchecked(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        self.basic_func(driver)

        stop_till_spinner_is_invisible(driver)
        time.sleep(1)
        click_filter_btn = wait.until(EC.element_to_be_clickable((By.XPATH, filter_option_btn)))
        click_filter_btn.click()

        # checks filter ageing options
        for i in range(1, 8):
            check_sev_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='group'][2]//div[@class='col-sm-12']["+str(i)+"]//span[@class='el-checkbox__input']")))
            check_sev_filter.click()
        assert wait.until(EC.invisibility_of_element((By.XPATH, "//div[@role='group'][2]//div[@class='col-sm-12']//span[@class='el-checkbox__input']")))

        # unchecks filter severity options
        for i in range(1, 8):
            uncheck_sev_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='group'][2]//div[@class='col-sm-12']["+str(i)+"]//span[@class='el-checkbox__input is-checked']")))
            uncheck_sev_filter.click()
        assert wait.until(EC.invisibility_of_element((By.XPATH, "//div[@role='group'][2]//div[@class='col-sm-12']//span[@class='el-checkbox__input is-checked']")))

    def test_delete_above_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'All options')]")
