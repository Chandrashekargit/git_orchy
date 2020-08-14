from pytest import mark
from Applications.test_create_applications.create_app import create_apps
from xpath.Application_module_xpath import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app_names = ['!@#$%^&*() 1234567890! createapp with alphanum,spl', '1234567890', 'D']
urls = ['http://demo.com', 'http://demo.com', 'http://D.com']


@mark.create_app_positive_tc
def test_positive_tc_application_boundary_value_analysis(driver):
    for (app_name, urL) in zip(app_names, urls):
        create_apps(driver, application_name=app_name, url=urL)

        wait = WebDriverWait(driver, 10, poll_frequency=2)
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))
