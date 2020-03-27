import time
from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from xpath.Application_module_xpath import *

apps = ["//label[contains(text(), 'DAST')]",
        "//label[contains(text(), 'SAST')]",
        "//label[contains(text(), 'SCA')]"
        ]


@mark.delete_apps
def test_delete_apps(driver):
    for app in apps:
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        individual_app = WebDriverWait(driver, 10, poll_frequency=3).until(EC.element_to_be_clickable((By.XPATH, app)))
        individual_app.click()

        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        action_dp.click()

        delete_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@class='el-dropdown-menu el-popper']//li[11]")))
        delete_btn.click()

        delete_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Yes')]")))
        time.sleep(1)
        delete_pop_up.click()

        enter_del = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type DELETE']")))
        enter_del.send_keys("DELETE")

        delete = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//footer[@class='modal-footer']//button[contains(text(),'Delete')]")))
        delete.click()
        time.sleep(1)
        driver.refresh()

