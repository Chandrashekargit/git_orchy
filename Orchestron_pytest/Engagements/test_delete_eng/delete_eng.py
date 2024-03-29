from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *
from xpath.Application_module_xpath import *
from spinner.spinner import *


def delete_eng(driver, engagement_name_xpath):
    wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException
    ])
    # clicks on Engagement section
    stop_till_spinner_is_invisible(driver)
    eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    stop_till_spinner_is_invisible(driver)
    click_on_individual_eng = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_name_xpath)))
    click_on_individual_eng.click()

    stop_till_spinner_is_invisible(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, action_dropdown)))
    action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action.click()
    select_delete = wait.until(EC.element_to_be_clickable((By.XPATH, eng_delete)))
    select_delete.click()
    stop_till_spinner_is_invisible(driver)
    click_delete = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_delete)))
    click_delete.click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    stop_till_spinner_is_invisible(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, delete_success_msg)))
