from xpath.settings_module_xpath import *
from Settings.test_teams.create_team import *
from Settings.test_teams.delete_team import *
from pytest import mark


@mark.test_team
class CheckTeamWarningMessagesTests:
    def test_warning_msg_when_same_team_is_created_with_existing_team_name(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])
        # create Team
        create_team(driver, name="Team A", desc="This is Team A")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_team_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_team_created)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        back.click()

        stop_till_spinner_is_invisible(driver)
        create_team(driver, name="Team A", desc="This is Team A")
        # Test for Warning message
        warning_msg_when_existing_team_is_created = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_when_we_create_existing_team)))
        assert warning_msg_when_existing_team_is_created.text == "* Team with this name already exists."

        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close']")))
        close_pop_up.click()
        back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        back.click()

    def test_warning_msg_while_updating_old_team_name_to_existing_team_name(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])
        # create Team
        create_team(driver, name="Team B", desc="This is Team B")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_team_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_team_created)))

        stop_till_spinner_is_invisible(driver)
        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
        action_dp.click()

        select_update = wait.until(EC.element_to_be_clickable((By.XPATH, update)))
        select_update.click()

        stop_till_spinner_is_invisible(driver)
        change_the_team_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-sm-10']//input[@type='text']")))
        change_the_team_name.clear()
        change_the_team_name.send_keys("Team A")

        submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, create_team_submit)))
        submit.click()

        stop_till_spinner_is_invisible(driver)
        warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'group with this name already exists.')]")))
        assert warning_msg.text == "* group with this name already exists."
        driver.refresh()

    def test_warning_msg_for_max_char_in_team_name_field(self, driver):
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
        name_field.send_keys("k" * 50)

        warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_max_char_in_name_field)))
        assert warning_msg.text == "* Ensure this field has no more than 50 characters."
        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close']")))
        close_pop_up.click()
        back = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        back.click()

    def test_warning_msg_for_max_char_while_updating(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        create_team(driver, name="Team C", desc="This is Team C")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_team_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_team_created)))

        stop_till_spinner_is_invisible(driver)
        search_team = wait.until(EC.element_to_be_clickable((By.XPATH, search_field)))
        search_team.clear()
        search_team.send_keys("Team C")
        search_team.send_keys(Keys.ENTER)

        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
        action_dp.click()

        select_update = wait.until(EC.element_to_be_clickable((By.XPATH, update)))
        select_update.click()

        stop_till_spinner_is_invisible(driver)
        change_the_team_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-sm-10']//input[@type='text']")))
        change_the_team_name.clear()
        change_the_team_name.send_keys("Team " * 50)

        warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_for_max_char_in_name_field)))
        assert warning_msg.text == "* Ensure this field has no more than 50 characters."
        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close']")))
        close_pop_up.click()
        stop_till_spinner_is_invisible(driver)
        back = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        back.click()

    def test_delete_team(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        for i in ["Team A", "Team B", "Team C"]:
            delete_team(driver, team_name=i)
            wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_delete_team)))
            wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_delete_team)))
            back = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
            back.click()
