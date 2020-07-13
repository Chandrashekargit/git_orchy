from Applications.test_create_applications.create_app import create_apps
from Applications.test_upload_scans.test_upload_results import *
from Applications.test_delete_application.delete_app import *
from Applications.test_close_evidence.close_evd import *
from pytest import mark


class CloseEvdTests:
    def test_create_application(self, driver):
        create_apps(driver, application_name="App_to_check_evd", url="http://demo.com")

    def test_upload_scan(self, driver):
        # NOTE: To parse all results it takes some time. so, please upload small file.
        upload_res(driver, application="//label[contains(text(), 'App_to_check_evd')]", tool_name="npm",
                   file_loc="/home/junaid/Downloads/results_supported_by_orchy/NpmAudit.json")

    def test_close_evidence(self, driver):
        close_evd(driver, app_name="//label[contains(text(), 'App_to_check_evd')]")


