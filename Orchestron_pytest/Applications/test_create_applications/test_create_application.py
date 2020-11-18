import time
from pytest import mark
from selenium.common.exceptions import *
from Applications.test_create_applications.create_app import create_apps
from xpath.Application_module_xpath import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# apps = ["DAST", "SAST", "SCA"]
apps = ["ZAP (json,xml)", "Burp (json,xml)", "arachni", "AppScan - DAST", "w3af", "acunetix", "appspider",
        "AppScan - SAST", "bandit", "brakeman", "checkmarx", "findsecbugs", "gosec",
        "hp", "nodejs", "veracode", "xanitizer", "OWASP dep", "snyk", "whitesource", "Retire", "npm", "Anchore(json)",
        "Aquasec (json)", "Nexus API (json)", "Detectify (json)", "Clair (json)", "Nexus CLI (json)", "Nessus (nessus)"]


@mark.smoke
@mark.create_apps
class ApplicationCreatingTests:
    def test_create_apps(self, driver):
        """
        These function lets us create new applications called sast, dast, sca with platform type as Python
        """
        for app in apps:
            create_apps(driver, application_name=app, url="http://demo.com")
            wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

            WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
            assert success_msg.text == "Application has been created successfully!"
            wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))


    # def test_if_applications_created(self, driver):
    #     """
    #     These function lets us check if the required applications are created.
    #     """
    #     application_Tab = WebDriverWait(driver, 10, poll_frequency=1).until(
    #         EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Applications')]")))
    #     application_Tab.click()
    #     time.sleep(2)
    #     applications = [driver.find_element_by_xpath("//label[contains(text(), 'SCA')]"),
    #                     driver.find_element_by_xpath("//label[contains(text(), 'DAST')]"),
    #                     driver.find_element_by_xpath("//label[contains(text(), 'SAST')]")]
    #     for application in applications:
    #         print(application.text)
    #         # print(application.tag_name)
    #         # print(application.parent)
    #         # print(application.location)
    #         # print(application.size)

