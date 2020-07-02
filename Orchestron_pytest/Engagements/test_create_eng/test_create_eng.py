from Engagements.test_create_eng.create_eng import *
from Engagements.test_delete_eng.delete_eng import *
from Applications.test_delete_application.delete_app import *
from Applications.test_create_applications.create_app import *
from pytest import mark


@mark.create_eng
class CreateEngagementTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="Demo X", url="http://demo.com")

    def test_create_eng(self, driver):
        create_engagement(driver, engagement_name="Demo engagement", eng_descrption="demo", which_application="Demo X", which_scope_type="All")

    def test_delete_eng(self, driver):
        delete_eng(driver, engagement_name_xpath="//label[contains(text(), 'Demo engagement')]")

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'Demo X')]")
