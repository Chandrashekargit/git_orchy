from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *


def create_user(driver, fn=None, ln=None, email_id=None, un=None, privilage=None):
    """
    These function lets us create the users.
    """
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    # click on the create button where we get a pop up to create the normal user/admin
    create = WebDriverWait(driver, 10, poll_frequency=1.5).until(EC.presence_of_element_located((By.XPATH, create_btn)))
    create.click()
    firstName = wait.until(EC.presence_of_element_located((By.XPATH, first_name)))
    firstName.send_keys(fn)
    lastName = wait.until(EC.presence_of_element_located((By.XPATH, last_name)))
    lastName.send_keys(ln)
    email = wait.until(EC.presence_of_element_located((By.XPATH, e_mail)))
    email.send_keys(email_id)
    username = wait.until(EC.presence_of_element_located((By.XPATH, user_name)))
    username.send_keys(un)
    usertype = wait.until(EC.presence_of_element_located((By.XPATH, user_type)))
    usertype.send_keys(privilage)
    usertype.send_keys(Keys.ENTER)
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_submit)))
    submit.click()
