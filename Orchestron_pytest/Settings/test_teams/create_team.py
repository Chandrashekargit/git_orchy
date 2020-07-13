import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import *


def create_team(driver, name, desc):
    """
    These function lets us create team.
    """
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    team = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
    team.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    create = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_btn)))
    create.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    name_field = wait.until(EC.presence_of_element_located((By.XPATH, team_name)))
    name_field.send_keys(name)

    desc_field = wait.until(EC.presence_of_element_located((By.XPATH, team_desc)))
    desc_field.send_keys(desc)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_team_submit)))
    submit.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_team_created)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_team_created)))
    # back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
    # back.click()
