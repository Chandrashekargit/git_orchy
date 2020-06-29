from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *
import time


def create_engagement(driver, engagement_name, which_application, which_scope_type):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException
    ])
    # clicks on Engagement section
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    # clicks on create button
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    time.sleep(2)
    create = wait.until(EC.element_to_be_clickable((By.XPATH, eng_create_btn)))
    create.click()

    # Enter the name of the engagement
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    name = wait.until(EC.presence_of_element_located((By.XPATH, eng_name)))
    name.send_keys(engagement_name)

    # Enter the description
    desc = wait.until(EC.presence_of_element_located((By.XPATH, eng_desc)))
    desc.send_keys("Demo Engagement")

    # Select the dates
    eng_date = wait.until(EC.element_to_be_clickable((By.XPATH, eng_date_btn)))
    eng_date.click()
    eng_date_popup1 = wait.until(EC.element_to_be_clickable((By.XPATH, eng_date1)))
    eng_date_popup1.click()
    eng_date_popup2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][2]//td[@title='30/06/2020']")))
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

    # Clicks on Submit button
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, eng_submit)))
    submit.click()

    # assert the success message
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, eng_success_msg)))
