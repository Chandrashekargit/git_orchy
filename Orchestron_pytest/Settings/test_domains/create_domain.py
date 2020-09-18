from xpath.settings_module_xpath import *
from selenium.common.exceptions import *
from spinner.spinner import *


def create_domain(driver, domain_name):
    """
    These function lets us create domain names.
    """
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    stop_till_spinner_is_invisible(driver)
    domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
    domain.click()

    stop_till_spinner_is_invisible(driver)
    create = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create)))
    create.click()

    stop_till_spinner_is_invisible(driver)
    domain_names = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_field)))
    domain_names.clear()
    domain_names.send_keys(domain_name)

    try:
        domain_submit = WebDriverWait(driver, 5, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
        domain_submit.click()
    except TimeoutException:
        print("Submit button not visible")

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_created)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_created)))
    # driver.refresh()
