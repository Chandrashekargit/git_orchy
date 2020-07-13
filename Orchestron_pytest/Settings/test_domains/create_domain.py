from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import *


def create_domain(driver, domain_name):
    """
    These function lets us create domain names.
    """
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
    domain.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    create = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create)))
    create.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    domain_names = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_field)))
    domain_names.send_keys(domain_name)

    domain_submit = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
    domain_submit.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_created)))
    wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_created)))
    driver.refresh()
