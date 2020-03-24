import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *

apps = ["DAST", "SAST", "SCA"]


@mark.smoke
@mark.create_apps
class ApplicationCreatingTests:
    def test_create_apps(self, driver):
        """
        These function lets us create new applications called sast, dast, sca with platform type as Python
        """
        for app in apps:
            applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, application_tab)))
            applicationTab.click()

            create_btn = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.presence_of_element_located((By.XPATH, app_create_button)))
            create_btn.click()

            name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, app_name)))
            name.send_keys(app)

            url = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, app_url)))
            url.send_keys("http://" + app + ".com")

            platform_type = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, app_platform_type)))
            platform_type.send_keys("Python")
            platform_type.send_keys(Keys.ARROW_DOWN)
            platform_type.send_keys(Keys.ENTER)

            team = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, app_team)))
            team.click()
            # team.send_keys('Testing')
            # team.send_keys(Keys.ENTER)

            submit_1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, app_submit)))
            submit_1.click()
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


