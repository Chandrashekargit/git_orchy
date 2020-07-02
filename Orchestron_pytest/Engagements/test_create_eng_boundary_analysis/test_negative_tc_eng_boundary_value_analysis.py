from pytest import mark
from Engagements.test_create_eng.create_eng import *
from Applications.test_create_applications.create_app import *
from Applications.test_delete_application.delete_app import *

eng_names = [" ", "Demo eng", "Demo eng"]
eng_descs = ["@1q,2/3==0" * 20, "z", "1"]


@mark.engagement_boundary_value_analysis_negative
class EngagementNegativeBVATests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="Application y", url="http://demo.com")

    def test_negative_tc_empty_space_in_name_field(self, driver):
        for (engagement_name, engagement_desc) in zip(eng_names, eng_descs):
            create_engagement(driver, engagement_name=engagement_name, eng_descrption=engagement_desc,
                              which_application="Application y", which_scope_type="SAST")

            if engagement_desc == "1":
                warning_msg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, wrng_msg_for_same_eng_name)))
                print(warning_msg.text)
                assert warning_msg.text == "* engagement with this name already exists."
                close_pop_up = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, create_eng_popup_close)))
                close_pop_up.click()

            elif engagement_name == " ":
                close_pop_up = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, create_eng_popup_close)))
                close_pop_up.click()
    
    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'Application y')]")
