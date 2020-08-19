from Engagements.test_create_eng.create_eng import *
from Applications.test_create_applications.create_app import *
from Applications.test_upload_scans.upload_results import *
from Applications.test_delete_application.delete_app import *
from Engagements.test_assign_and_unassign_scans.assign_scans import *
from Engagements.test_view_report.view_report import *
from pytest import mark

sca_tools = ["/home/junaid/Downloads/results_supported_by_orchy/OWASP Dependency Checker.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/snyk.json",
             "/home/junaid/Downloads/results_supported_by_orchy/WhiteSource.xml",
             "/home/junaid/Downloads/results_supported_by_orchy/RetireJS.json",
             "/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json"
             ]

sca_names = ["OWASP Dependency", "snyk", "whitesource", "Retire", "npm", "snyk"]


@mark.view_exec_report
class ViewExecReportsTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="View report", url="http://viewreport.com")

    def test_upload_scans(self, driver):
        for (tool3, name3) in zip(sca_tools, sca_names):
            upload_res(driver, application="//label[contains(text(), 'View report')]", tool_name=name3, file_loc=tool3)

    def test_create_eng(self, driver):
        create_engagement(driver, engagement_name="view report eng", eng_descrption="dmeo", which_application="View report",
                          which_scope_type="All")

    def test_assign_scans(self, driver):
        assign_scans(driver, individual_eng_xpath="//label[contains(text(),'view report eng')]")

    def test_view_report(self, driver):
        view_exec_report(driver, engagement_name_xpath="//label[contains(text(),'view report eng')]")

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'View report')]")
