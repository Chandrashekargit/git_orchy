from Applications.test_create_applications.create_app import *
from Engagements.test_create_eng.create_eng import *
from Applications.test_delete_application.delete_app import *
from Engagements.test_close_engagement.close_eng import *
from pytest import mark

apps = ["Demo A", "Demo B", "Demo C", "Demo D", "Demo E"]
engs = ["Demo A eng", "Demo B eng", "Demo C eng", "Demo D eng", "Demo E eng"]
scopes = ["DAST", "SAST", "SCA", "Manual", "All"]


@mark.close_eng
class CloseEngagementTests:
    """
    This TC lets us check if we are able to close the Engagement for all scope types.
    """
    def test_create_app(self, driver):
        for app in apps:
            create_apps(driver, application_name=app, url="http://demo.com")

    def test_create_eng(self, driver):
        for (eng, app, scope) in zip(engs, apps, scopes):
            create_engagement(driver, engagement_name=eng, eng_descrption="demo "*20, which_application=app,
                              which_scope_type=scope)

    def test_close_eng(self, driver):
        for eng in engs:
            close_eng(driver, engagement_name_xpath="//label[contains(text(),'"+eng+"')]")

    def test_delete_app(self, driver):
        for app in apps:
            delete_app(driver, application="//label[contains(text(), '"+app+"')]")
