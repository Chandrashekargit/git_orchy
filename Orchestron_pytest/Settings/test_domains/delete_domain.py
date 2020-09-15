from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import *
from spinner.spinner import *


def delete_domain(driver, domain_name):
    wait = WebDriverWait(driver, 10, poll_frequency=3, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    stop_till_spinner_is_invisible(driver)
    domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
    domain.click()

    stop_till_spinner_is_invisible(driver)
    stop_till_spinner_is_invisible(driver)
    search = wait.until(EC.presence_of_element_located((By.XPATH, domain_search_field)))
    search.clear()
    search.send_keys(domain_name)

    stop_till_spinner_is_invisible(driver)
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, doamin_action_dropdown)))
    action_dp.click()

    delete = wait.until(EC.element_to_be_clickable((By.XPATH, domain_delete)))
    delete.click()
    delete_domain_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, domain_delete_yes)))
    delete_domain_pop_up.click()

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
    # back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
    # back.click()