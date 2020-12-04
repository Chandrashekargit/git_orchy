from xpath.settings_module_xpath import *
from spinner.spinner import *


def create_team(driver, name, desc):
    """
    These function lets us create team.
    """
    wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    stop_till_spinner_is_invisible(driver)
    team = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
    team.click()

    stop_till_spinner_is_invisible(driver)
    create = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_btn)))
    create.click()

    stop_till_spinner_is_invisible(driver)
    name_field = wait.until(EC.presence_of_element_located((By.XPATH, team_name)))
    name_field.send_keys(name)

    desc_field = wait.until(EC.presence_of_element_located((By.XPATH, team_desc)))
    desc_field.send_keys(desc)

    try:
        stop_till_spinner_is_invisible(driver)
        submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, create_team_submit)))
        submit.click()

    except TimeoutException:
        print("Submit button not visible")

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_team_created)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_team_created)))
    # back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
    # back.click()
