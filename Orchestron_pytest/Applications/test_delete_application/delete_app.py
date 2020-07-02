import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from xpath.Application_module_xpath import *


def delete_app(driver, application=None):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, application)))
    individual_app.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()

    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, delete_option)))
    delete_btn.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    delete_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, yes)))
    time.sleep(1)
    delete_pop_up.click()

    enter_del = wait.until(EC.element_to_be_clickable((By.XPATH, enter_delete)))
    enter_del.send_keys("DELETE")

    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, delete)))
    delete_button.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    # success_msg = wait.until(EC.presence_of_element_located((By.XPATH, "Application has been deleted successfully!")))
    time.sleep(2)

