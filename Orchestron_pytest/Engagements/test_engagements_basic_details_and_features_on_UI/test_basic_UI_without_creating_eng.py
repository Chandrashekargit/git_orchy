from pytest import mark
from xpath.Engagement_module_xpath import *
from spinner.spinner import *
from Engagements.test_create_eng.create_eng import *


bucket_type_options_xpath = [dast_bucket_type, sast_bucket_type, sca_bucket_type, manual_bucket_type, script_bucket_type,
                             orchy_json_bucket_type, infra_bucket_type, container_bucket_type, cloud_bucket_type, all_bucket_type]

bucket_type_options_text = ["DAST", "SAST", "SCA", "Manual", "Script", "Orchestron JSON", "INFRA", "Container", "Cloud", "All"]

"""
Note: Before running this testcase make sure we have ZERO Engagements
"""


@mark.basic_elements_before_eng
class CheckBasicUIOnEngTests:
    def test_basic_ui(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
        eng_tab.click()

        # checks 'List Of Engagements' tag available on UI
        stop_till_spinner_is_invisible(driver)
        list_of_eng = wait.until(EC.presence_of_element_located((By.XPATH, "//p[.=' List of Engagements ']")))
        assert list_of_eng.text == "List of Engagements", "List of Engagement tag is not visible on UI"

        # checks create btn
        create_btn1 = wait.until(EC.presence_of_element_located((By.XPATH, eng_create_btn)))
        assert create_btn1.text == "Create", "Create button is not visible on UI"

        create_btn2 = wait.until(EC.presence_of_element_located((By.XPATH, eng_create_btn2)))
        assert create_btn2.text == "Click here to create an Engagement or click on Create button."

        # checks Search field
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

        # checks 'eng_list_is_empty' tag
        eng_list_is_empty = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Currently, the Engagement list is empty.')]")))
        assert eng_list_is_empty.text == "Currently, the Engagement list is empty."

    def test_create_btn(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        for i in [eng_create_btn, eng_create_btn2]:
            # clicks on Engagement section
            stop_till_spinner_is_invisible(driver)
            eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
            eng_tab.click()

            # clicks on create button
            stop_till_spinner_is_invisible(driver)
            # time.sleep(3)
            create = wait.until(EC.element_to_be_clickable((By.XPATH, i)))
            create.click()

            # checks for all fields visibility/presence after clicking on create button.
            stop_till_spinner_is_invisible(driver)
            name = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Name: *']")))
            assert name.text == "Name: *"
            desc = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Description: *']")))
            assert desc.text == "Description: *"
            app_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Application: *']")))
            assert app_dropdown.text == "Application: *"
            scope = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Scope (by result type): *']")))
            assert scope.text == "Scope (by result type): *"
            bucket_type = wait.until(EC.presence_of_element_located((By.XPATH, eng_bucket_type)))
            bucket_type.click()
            time.sleep(2)
            # checks for visibility of all options under bucket type dropdown
            for (j, k) in zip(bucket_type_options_xpath, bucket_type_options_text):
                options = wait.until(EC.presence_of_element_located((By.XPATH, j)))
                assert options.text == k

            date = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Date: *']")))
            assert date.text == "Date: *"
            close_btn = wait.until(EC.presence_of_element_located((By.XPATH, create_eng_popup_close2)))
            assert close_btn.text == "Close"
            close_btn.click()
