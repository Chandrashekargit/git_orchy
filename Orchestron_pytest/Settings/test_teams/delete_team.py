import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *


def delete_team(driver, team_name):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    team = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
    team.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    search_team = wait.until(EC.element_to_be_clickable((By.XPATH, search_field)))
    search_team.clear()
    search_team.send_keys(team_name)
    search_team.send_keys(Keys.ENTER)

    action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
    action_dp.click()

    select_delete = wait.until(EC.element_to_be_clickable((By.XPATH, delete)))
    select_delete.click()
    click_yes = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_delete)))
    click_yes.click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_delete_team)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_delete_team)))
    time.sleep(2)
