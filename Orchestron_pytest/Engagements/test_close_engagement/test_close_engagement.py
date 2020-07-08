from Applications.test_create_applications.create_app import *
from Engagements.test_create_eng.create_eng import *
from Applications.test_delete_application.delete_app import *
from Engagements.test_close_engagement.close_eng import *
from pytest import mark


@mark.close_eng
class CloseEngagementTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="Demo X", url="http://demo.com")

    def test_create_eng(self, driver):
        create_engagement(driver, engagement_name="Demo eng", eng_descrption="dmeo", which_application="Demo X", which_scope_type="DAST")

    def test_close_eng(self, driver):
        close_eng(driver, engagement_name_xpath="//label[contains(text(),'Demo eng')]")

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'Demo X')]")
