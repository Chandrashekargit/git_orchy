import time

from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


def create_apps(driver, application_name=None, url=None):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    create_btn = wait.until(EC.presence_of_element_located((By.XPATH, app_create_button)))
    create_btn.click()

    name = wait.until(EC.presence_of_element_located((By.XPATH, app_name)))
    name.send_keys(application_name)

    url_field = wait.until(EC.presence_of_element_located((By.XPATH, app_url)))
    url_field.send_keys(url)

    platform_type = wait.until(EC.presence_of_element_located((By.XPATH, app_platform_type)))
    platform_type.send_keys("Python")
    platform_type.send_keys(Keys.ARROW_DOWN)
    platform_type.send_keys(Keys.ENTER)

    team = wait.until(EC.presence_of_element_located((By.XPATH, app_team)))
    team.click()
    # team.send_keys('Testing')
    # team.send_keys(Keys.ENTER)

    submit_1 = wait.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
    submit_1.click()
    time.sleep(2)
