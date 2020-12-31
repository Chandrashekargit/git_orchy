import time
from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Application_module_xpath import *
from spinner.spinner import *

apps = ["DAST", "SAST", "SCA"]
# apps = ["ZAP (json,xml)", "Burp (json,xml)", "arachni", "AppScan - DAST", "w3af", "acunetix", "appspider",
#         "AppScan - SAST", "bandit", "brakeman", "checkmarx", "findsecbugs", "gosec",
#         "hp", "nodejs", "veracode", "xanitizer", "OWASP dep", "snyk", "whitesource", "Retire", "npm", "Anchore(json)",
#         "Aquasec (json)", "Nexus API (json)", "Detectify (json)", "Clair (json)", "Nexus CLI (json)", "Nessus (nessus)"]


@mark.create_apps
def test_create_apps(driver):
    """
    These function lets us create new applications with platform type as Python
    """
    for app in apps:
        create_apps(driver, application_name=app, url="http://demo.com")
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))
