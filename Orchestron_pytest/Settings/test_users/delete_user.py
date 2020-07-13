import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *


def delete_users(driver, user_email):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    # click on users section
    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    user_section = wait.until(EC.element_to_be_clickable((By.XPATH, users)))
    user_section.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    search = wait.until(EC.presence_of_element_located((By.XPATH, users_search_field)))
    search.clear()
    search.send_keys(user_email)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    action = wait.until(EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown)))
    action.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown_delete)))
    delete_btn.click()

    delete_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, delete_confirmation_yes)))
    delete_pop_up.click()
    # driver.execute_script("arguments[0].click();", delete_pop_up)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_deleted)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_deleted)))
    time.sleep(2)
