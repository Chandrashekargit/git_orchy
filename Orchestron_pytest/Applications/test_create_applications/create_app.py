import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from wait.Explicit_wait import ExplicitWait


def create_apps(driver, application_name=None, url=None):
    applicationTab = ExplicitWait(value=application_tab).click(driver)
    create_btn = ExplicitWait(value=app_create_button).click(driver)

    name = ExplicitWait(value=app_name).presence1(driver)
    name.send_keys(application_name)

    url_field = ExplicitWait(value=app_url).presence1(driver)
    url_field.send_keys(url)

    platform_type = ExplicitWait(value=app_platform_type).presence1(driver)
    platform_type.send_keys("Python")
    platform_type.send_keys(Keys.ARROW_DOWN)
    platform_type.send_keys(Keys.ENTER)

    team = ExplicitWait(value=app_team).presence1(driver)
    team.click()
    # team.send_keys('Testing')
    # team.send_keys(Keys.ENTER)

    submit_1 = ExplicitWait(value=app_submit).click(driver)
    time.sleep(2)

# def create_apps(driver, application_name=None, url=None):
#     wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
#         NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])
#
#     applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
#     applicationTab.click()
#
#     create_btn = wait.until(EC.presence_of_element_located((By.XPATH, app_create_button)))
#     create_btn.click()
#
#     name = wait.until(EC.presence_of_element_located((By.XPATH, app_name)))
#     name.send_keys(application_name)
#
#     url_field = wait.until(EC.presence_of_element_located((By.XPATH, app_url)))
#     url_field.send_keys(url)
#
#     platform_type = wait.until(EC.presence_of_element_located((By.XPATH, app_platform_type)))
#     platform_type.send_keys("Python")
#     platform_type.send_keys(Keys.ARROW_DOWN)
#     platform_type.send_keys(Keys.ENTER)
#
#     team = wait.until(EC.presence_of_element_located((By.XPATH, app_team)))
#     team.click()
#     # team.send_keys('Testing')
#     # team.send_keys(Keys.ENTER)
#
#     submit_1 = wait.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
#     submit_1.click()
#     time.sleep(2)