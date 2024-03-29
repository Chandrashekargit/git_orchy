import time
from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from xpath.Application_module_xpath import *
from Applications.test_delete_application.delete_app import delete_app

apps = ["//label[contains(text(), 'DAST')]",
        "//label[contains(text(), 'SAST')]",
        "//label[contains(text(), 'SCA')]"
        ]


@mark.delete_apps
def test_delete_apps(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    for app in apps:
        delete_app(driver, application_xpath=app)
