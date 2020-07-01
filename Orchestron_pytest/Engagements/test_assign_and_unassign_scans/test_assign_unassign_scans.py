from Engagements.test_create_eng.create_eng import *
from Engagements.test_delete_eng.delete_eng import *
from Applications.test_delete_application.delete_app import *
from Applications.test_upload_scans.test_upload_results import *
from Engagements.test_assign_and_unassign_scans.assign_scans import *
from Engagements.test_assign_and_unassign_scans.unassign_scans import *
from Applications.test_create_applications.create_app import *
from pytest import mark


sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
             ]

sca_names = ["OWASP", "snyk", "whitesource", "Retire", "npm", "snyk"]


@mark.assign_unassign_scans
class CreateEngagementTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="Demo X", url="http://demo.com")

    def test_upload_scans(self, driver):
        for (tool3, name3) in zip(sca_tools, sca_names):
            upload_res(driver, application="//label[contxains(text(), 'Demo X')]", tool_name=name3, file_loc=tool3)

    def test_create_eng(self, driver):
        create_engagement(driver, engagement_name="Demo engagement", which_application="Demo X", which_scope_type="All")

    def test_assign_scans(self, driver):
        assign_scans(driver, individual_eng_xpath="//label[contains(text(), 'Demo engagement')]")

    def test_unassign_scans(self, driver):
        unassign_scans(driver, individual_eng_xpath="//label[contains(text(), 'Demo engagement')]")

    def test_delete_eng(self, driver):
        delete_eng(driver, engagement_name_xpath="//label[contains(text(), 'Demo engagement')]")

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'Demo X')]")
