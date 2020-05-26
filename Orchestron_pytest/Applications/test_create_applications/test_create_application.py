import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from Applications.test_create_applications.create_app import create_apps

apps = ["DAST", "SAST", "SCA"]
# apps = ["ZAP (json,xml)", "Burp (json,xml)", "arachni", "AppScan - DAST", "w3af", "acunetix", "appspider",
#         "AppScan - SAST", "bandit", "brakeman", "checkmarx", "findsecbugs", "gosec",
#         "hp", "nodejs", "veracode", "xanitizer", "OWASP dep", "snyk", "whitesource", "Retire", "npm", "Anchore(json)",
#         "Aquasec (json)", "Nexus API (json)", "Detectify (json)", "Clair (json)", "Nexus CLI (json)", "Nessus (nessus)"]


@mark.smoke
@mark.create_apps
class ApplicationCreatingTests:
    def test_create_apps(self, driver):
        """
        These function lets us create new applications called sast, dast, sca with platform type as Python
        """
        for app in apps:
            # calling the function 'create_apps'
            create_apps(driver, application_name=app, url="http://demo.com")
            time.sleep(2)

    def test_if_applications_created(self, driver):
        """
        These function lets us check if the required applications are created.
        """
        application_Tab = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Applications')]")))
        application_Tab.click()
        time.sleep(2)
        applications = [driver.find_element_by_xpath("//label[contains(text(), 'SCA')]"),
                        driver.find_element_by_xpath("//label[contains(text(), 'DAST')]"),
                        driver.find_element_by_xpath("//label[contains(text(), 'SAST')]")]
        for application in applications:
            print(application.text)
            # print(application.tag_name)
            # print(application.parent)
            # print(application.location)
            # print(application.size)


