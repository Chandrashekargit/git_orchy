import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *


def delete_users(driver, user_email=None):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    search = wait.until(EC.presence_of_element_located((By.XPATH, users_search_field)))
    search.clear()
    search.send_keys(user_email)
    driver.execute_script("window.scrollTo(0, 900);")
    time.sleep(2)
    action = wait.until(EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown)))
    action.click()
    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown_delete)))
    delete_btn.click()
    time.sleep(2)
    delete_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, delete_confirmation_yes)))
    driver.execute_script("arguments[0].click();", delete_pop_up)
    time.sleep(2)
