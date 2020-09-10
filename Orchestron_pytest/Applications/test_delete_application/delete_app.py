import time
from xpath.Application_module_xpath import *
from spinner.spinner import *


def delete_app(driver, application):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    stop_till_spinner_is_invisible(driver)
    individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, application)))
    individual_app.click()

    stop_till_spinner_is_invisible(driver)
    stop_till_spinner_is_invisible(driver)
    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action_dp.click()

    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, delete_option)))
    delete_btn.click()

    stop_till_spinner_is_invisible(driver)
    delete_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, yes)))
    time.sleep(1)
    driver.execute_script("arguments[0].click();", delete_pop_up)

    enter_del = wait.until(EC.element_to_be_clickable((By.XPATH, enter_delete)))
    enter_del.send_keys("DELETE")

    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, delete)))
    driver.execute_script("arguments[0].click();", delete_button)

    stop_till_spinner_is_invisible(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_delete)))
    wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_for_app_delete)))
