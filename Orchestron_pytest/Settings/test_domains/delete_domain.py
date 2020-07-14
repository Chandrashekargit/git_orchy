from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import *


def delete_domain(driver, domain_name):
    wait = WebDriverWait(driver, 10, poll_frequency=3, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
    domain.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    search = wait.until(EC.presence_of_element_located((By.XPATH, domain_search_field)))
    search.clear()
    search.send_keys(domain_name)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, doamin_action_dropdown)))
    action_dp.click()

    delete = wait.until(EC.element_to_be_clickable((By.XPATH, domain_delete)))
    delete.click()
    delete_domain_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, domain_delete_yes)))
    delete_domain_pop_up.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
    # back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
    # back.click()