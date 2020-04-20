import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from Settings.test_manageUsersAndTeams.create_users_script import *
from Applications.test_create_applications.create_app import *
from Settings.test_manageUsersAndTeams.domain_script import *
from Settings.test_manageUsersAndTeams.delete_user_script import *


firstnames = ['Jose', 'pep', 'James', 'Niki']
lastnames = ['mourinho', 'guardiola', 'hunt', 'lauda']

"""
Before running these file please make sure there is domain called 'gmail.com'
"""


@mark.create_users
class UsersWarningMessagesAndCreateAndDeleteUsersTests:
    # def test_domain_not_exist_warning_msg(self, driver):
    #     """
    #     These function lets us check if we are able to create the users outside org and asserts its warning message.
    #     """
    #     wait = WebDriverWait(driver, 6, poll_frequency=2)
    #     # calling the function 'create_user'
    #     create_user(driver, fn="Jose", ln="mourinho", email_id="Josemourinho@xyz.com", un="Jose", privilage="admin")
    #     time.sleep(2)
    #     # asserts the warning message
    #     warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_if_we_create_users_outside_org))).text
    #     assert "* You are trying to create users outside organization. Please register the domain" in warning_msg
    #     time.sleep(2)
    #     close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='×']")))
    #     close_pop_up.click()

    # def test_create_user_with_existing_mail_and_username_check_warning_msg(self, driver):
    #     """
    #     These function lets us check the warning message if admin tries to create the new user with
    #     existing username and email
    #     """
    #     wait = WebDriverWait(driver, 10, poll_frequency=2)
    #     # calling the function 'create_user'
    #     create_user(driver, fn="c", ln="s", email_id="chandrashekar@we45.com", un="cs", privilage="admin")
    #
    #     email_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, existing_email_warning_msg))).text
    #     un_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, existing_username_warning_msg))).text
    #     assert email_warning_message1 == "* user with this email address already exists."
    #     assert username_warning_message2 == "* This user name has already been added."
    #     time.sleep(2)
    #
    #     close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='×']")))
    #     close_pop_up.click()

    def test_create_users(self, driver):
        """
        These function lets us create new users (both admin users and normal users)
        """
        # calling the function 'create_domain_script'
        create_domain_script(driver, domain_names="gmail.com")

        # calling the function 'create_user'
        create_user(driver, fn="Jose", ln="mourinho", email_id="Josemourinho@gmail.com", un="Jose", privilage="admin")
        create_user(driver, fn="pep", ln="guardiola", email_id="pepguardiola@gmail.com", un="pep", privilage="admin")
        create_user(driver, fn="James", ln="hunt", email_id="Jameshunt@gmail.com", un="James", privilage="normal")
        create_user(driver, fn="Niki", ln="lauda", email_id="Nikilauda@gmail.com", un="Niki", privilage="normal")
        driver.refresh()

    # def test_assign_normal_users_to_team(self, driver, create_team):
    #     """
    #     These function lets us assign the normal users to required team
    #     :param create_team: It creates new team where normal users can be assigned to that team
    #     """
    #     wait = WebDriverWait(driver, 10, poll_frequency=1)
    #     settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    #     driver.execute_script("arguments[0].click();", settingstab)
    #
    #     teams = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
    #     teams.click()
    #
    #     search = wait.until(EC.element_to_be_clickable((By.XPATH, search_field)))
    #     search.send_keys('Testing team')
    #
    #     action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
    #     action_dp.click()
    #     addusers = wait.until(EC.element_to_be_clickable((By.XPATH, add_users)))
    #     addusers.click()
    #
    #     # select users pop up
    #     select_users_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, select_users_dp)))
    #     select_users_dropdown.click()
    #     select_users_dropdown.send_keys('james')  # Add 1st Normal user
    #     select_users_dropdown.send_keys(Keys.ENTER)
    #     select_users_dropdown.click()
    #     select_users_dropdown.send_keys('jose')  # Add 2nd Normal user
    #     select_users_dropdown.send_keys(Keys.ENTER)
    #
    #     select_user_submit = wait.until(EC.element_to_be_clickable((By.XPATH, select_users_submit)))
    #     select_user_submit.click()
    #     time.sleep(2)
    #
    #     count_of_users = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '2')]"))).text
    #     assert count_of_users == '2'

    # def test_warning_message_for_creating_existing_team(self, driver, create_team):
    #     """
    #     These function lets us check the warning message if we try to create team same as existing team
    #     :param create_team: It creates new team.
    #     """
    #     wait = WebDriverWait(driver, 10, poll_frequency=1)
    #     warning_msg = wait.until(EC.element_to_be_clickable(
    #             (By.XPATH, "//p[contains(text(), ' * Team with this name already exists.')]"))).text
    #     print("\n", warning_msg)
    #     assert warning_msg == "* Team with this name already exists."
    #     close_popup = wait.until(EC.element_to_be_clickable((By.XPATH,
    #                                              "/html/body/div/div/div[2]/section/div/div[1]/div/div/div[2]"
    #                                               "/div/div/div[9]/div/div[1]/div/div/header/button")))
    #     close_popup.click()
    #
    # def test_warning_message_for_max_char(self, driver):
    #     """
    #     These function lets us check the warning message if the team 'name' field reaches the max characters
    #     """
    #     wait = WebDriverWait(driver, 10, poll_frequency=1)
    #     settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    #     driver.execute_script("arguments[0].click();", settingstab)
    #
    #     teams = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
    #     teams.click()
    #     create = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_btn)))
    #     create.click()
    #     name = wait.until(EC.element_to_be_clickable((By.XPATH, team_name)))
    #     name.send_keys('Tests' * 10)
    #     warning_msg = wait.until(EC.element_to_be_clickable(
    #             (By.XPATH, "//p[contains(text(), ' * Ensure this field has no more than 50 characters.')]"))).text
    #     print('\n', warning_msg)
    #     assert warning_msg == "* Ensure this field has no more than 50 characters."
    #     desc = wait.until(EC.element_to_be_clickable((By.XPATH, team_desc)))
    #     desc.send_keys('These is testing team where only testers are assigned to these team')
    #     submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_team_submit)))
    #     submit.click()
    #     time.sleep(2)
    #
    #     # Delete the above team
    #     action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
    #     action_dp.click()
    #     dele = wait.until(EC.element_to_be_clickable((By.XPATH, delete)))
    #     dele.click()
    #     click_yes = wait.until(EC.element_to_be_clickable((By.XPATH,
    #                                                "/html/body/div/div/div[2]/section/div/div[1]/div/div/div[2]/div"
    #                                               "/div/div[10]/div/div[1]/div/div/footer/div/div/button[2]")))
    #     click_yes.click()
    #     driver.refresh()

    def test_delete_users(self, driver):
        """
        These function lets us delete the users.
        """
        for i in ["Josemourinho@gmail.com", "pepguardiola@gmail.com", "Jameshunt@gmail.com", "Nikilauda@gmail.com"]:
            delete_users(driver, user_email=i)

    # def test_forWarningMessageWhenNoNormalUserPresentAndClickOnAddusers(self, driver):
    #     wait = WebDriverWait(driver, 10, poll_frequency=1)
    #     settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    #     driver.execute_script("arguments[0].click();", settingstab)
    #
    #     teams = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
    #     teams.click()
    #     driver.execute_script("window.scrollTo(0, 900);")
    #     action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
    #     action_dp.click()
    #     addusers = wait.until(EC.element_to_be_clickable((By.XPATH, add_users)))
    #     addusers.click()
    #     warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH,
    #                     "//p[contains(text(), ' * Note: Please create normal user to assign them to a team .')]"))).text
    #     assert warning_msg == "* Note: Please create normal user to assign them to a team ."
