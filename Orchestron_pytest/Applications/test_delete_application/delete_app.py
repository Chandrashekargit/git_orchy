import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from xpath.Application_module_xpath import *


def delete_app(driver, application=None):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, application)))
    # individual_app.click()
    time.sleep(2)
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()

    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, delete_option)))
    delete_btn.click()

    delete_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, yes)))
    time.sleep(1)
    delete_pop_up.click()

    enter_del = wait.until(EC.element_to_be_clickable((By.XPATH, enter_delete)))
    enter_del.send_keys("DELETE")

    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, delete)))
    delete_button.click()
    time.sleep(2)

# these function is used in 'test_delete_application', 'test_warning_msg_while_updating_application'.
