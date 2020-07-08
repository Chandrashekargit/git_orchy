from pytest import mark
from Engagements.test_create_eng.create_eng import *
from Applications.test_create_applications.create_app import *
from Applications.test_delete_application.delete_app import *

eng_names = ["!@#$%^&*() 1234567890! createapp with alphanum,spl", "1234567890", "D", "0", "@", "ABC", "abc"]
eng_descs = ["@1q,2/3==0" * 20, "z", "http://DEMO.com", "qwerty"*200, "!@#$%^&*()_+=-", "abc", "abc"]


@mark.engagement_boundary_value_analysis_positive
class EngagementBVATests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="Demo y", url="http://demo.com")

    def test_create_eng(self, driver):
        for (eng_name, eng_desc) in zip(eng_names, eng_descs):
            create_engagement(driver, engagement_name=eng_name, eng_descrption=eng_desc, which_application="Demo y",
                              which_scope_type="All")

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'Demo y')]")
