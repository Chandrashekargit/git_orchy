import time
from pytest import mark
from Applications.test_manual_entry_scans.manual_entry import *
from Applications.test_create_applications.create_app import *
from Applications.test_delete_application.delete_app import *


@mark.enter_manual_vul
class EnterManualVulnerableTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="Manual vul app", url="http://demo.com")

    def test_manual_entry(self, driver):
        create_manual_vul(driver, individual_app_xpath="//label[contains(text(), 'Manual vul app')]", scan_name="SQL manual", Severity="High", cwe_num="89:Sql")

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'Manual vul app')]")
