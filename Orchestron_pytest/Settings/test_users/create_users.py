import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *


def create_user(driver, fn, ln, email_id, un, privilage):
    """
    These function lets us create the users.
    """
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    # click on users section
    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    user_section = wait.until(EC.element_to_be_clickable((By.XPATH, users)))
    user_section.click()

    # click on the create button where we get a pop up to create the normal user and admin user
    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    create = wait.until(EC.presence_of_element_located((By.XPATH, create_btn)))
    create.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
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

    if privilage == "Normal".lower():
        click_on_create_team = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Create Team']")))
        click_on_create_team.click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@maxlength='50']")))
        name.send_keys("Demo X team")

        desc = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id]")))
        desc.send_keys("Demo team")

        submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='Submit']")))
        submit.click()
        time.sleep(3)

        click_on_select_team_dp = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select']")))
        click_on_select_team_dp.send_keys("Demo X team")
        click_on_select_team_dp.send_keys(Keys.ARROW_DOWN)
        click_on_select_team_dp.send_keys(Keys.ENTER)

    try:
        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_submit)))
        submit.click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_created)))
        # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_created)))
        # back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        # back.click()
    except TimeoutException:
        print("Submit button not visible")
