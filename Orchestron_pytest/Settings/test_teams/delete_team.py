import time
from selenium.webdriver.common.keys import Keys
from xpath.settings_module_xpath import *
from spinner.spinner import *


def delete_team(driver, team_name):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    stop_till_spinner_is_invisible(driver)
    team = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
    team.click()

    stop_till_spinner_is_invisible(driver)
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

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_delete_team)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_delete_team)))
    time.sleep(2)
