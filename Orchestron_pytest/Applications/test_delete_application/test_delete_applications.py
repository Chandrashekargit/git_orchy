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
    for i in range(1,10):
        delete_app(driver, application=i)  # calling the function 'delete_app'
        time.sleep(1)
        driver.refresh()
        # assert app not in driver.page_source

