from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *
import time
from spinner.spinner import *


def create_engagement(driver, engagement_name, eng_descrption, which_application, which_scope_type):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    # clicks on Engagement section
    stop_till_spinner_is_invisible(driver)
    eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    # clicks on create button
    stop_till_spinner_is_invisible(driver)
    time.sleep(3)
    create = wait.until(EC.element_to_be_clickable((By.XPATH, eng_create_btn)))
    create.click()

    # Enter the name of the engagement
    stop_till_spinner_is_invisible(driver)
    time.sleep(2)
    name = wait.until(EC.element_to_be_clickable((By.XPATH, eng_name)))
    name.send_keys(engagement_name)

    # Enter the description
    desc = wait.until(EC.presence_of_element_located((By.XPATH, eng_desc)))
    desc.send_keys(eng_descrption)

    # Select the dates
    eng_date = wait.until(EC.element_to_be_clickable((By.XPATH, eng_date_btn)))
    eng_date.click()
    eng_date_popup1 = wait.until(EC.element_to_be_clickable((By.XPATH, eng_date1)))
    eng_date_popup1.click()
    eng_date_popup2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][2]//td[@title='30/01/2021']")))
    eng_date_popup2.click()

    # selects the scope/bucket type
    bucket_type = wait.until(EC.presence_of_element_located((By.XPATH, eng_bucket_type)))
    bucket_type.send_keys(which_scope_type)
    bucket_type.send_keys(Keys.ARROW_DOWN)
    bucket_type.send_keys(Keys.ENTER)

    # selects the required application from the dropdwon
    app_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, eng_app_dropdown)))
    app_dropdown.click()
    app_dropdown.send_keys(which_application)
    app_dropdown.send_keys(Keys.ARROW_DOWN)
    app_dropdown.send_keys(Keys.ENTER)

    try:
        # Clicks on Submit button
        submit = WebDriverWait(driver, 5, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, eng_submit)))
        submit.click()
        # assert the success message
        # stop_till_spinner_is_invisible(driver)
        # wait.until(EC.visibility_of_element_located((By.XPATH, eng_success_msg)))
        # wait.until(EC.invisibility_of_element((By.XPATH, eng_success_msg)))
    except (ElementClickInterceptedException, TimeoutException):
        print('submit button not visible')

    # success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[.='Engagement has been created successfully!']")))
    # assert success_msg.text == "Engagement has been created successfully!"
    # wait.until(EC.invisibility_of_element_located((By.XPATH, "//p[.='Engagement has been created successfully!']")))
