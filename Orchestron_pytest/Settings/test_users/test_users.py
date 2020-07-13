from Settings.test_domains.create_domain import create_domain
from Settings.test_users.create_users import *
from Settings.test_domains.delete_domain import *
from Settings.test_users.delete_user_script import *
from Settings.test_teams.create_team import *


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
    #
    #     # asserts the warning message
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    #     warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, warning_msg_if_we_create_users_outside_org)))
    #     assert "* You are trying to create users outside organization. Please register the domain" in warning_msg.text
    #
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
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    #     email_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, existing_email_warning_msg))).text
    #     un_warning_msg = wait.until(EC.presence_of_element_located((By.XPATH, existing_username_warning_msg))).text
    #     assert email_warning_msg == "* user with this email address already exists."
    #     assert un_warning_msg == "* This user name has already been added."
    #
    #     close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='×']")))
    #     close_pop_up.click()

    # def test_create_users(self, driver):
    #     """
    #     This function lets us create new users (both admin users and normal users)
    #     """
    #     wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
    #         ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])
    #
    #     # calling the function 'create_domain_script'
    #     create_domain(driver, domain_name="xyz.com")
    #
    #     for (firstname, lastname) in zip(firstnames, lastnames):
    #         if firstname == "Jose" or firstname == "pep":
    #             create_user(driver, fn=firstname, ln=lastname, email_id=firstname+lastname+"@xyz.com", un=firstname, privilage="admin")
    #             wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_created)))
    #             wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_created)))
    #         else:
    #             create_user(driver, fn=firstname, ln=lastname, email_id=firstname+lastname+"@xyz.com", un=firstname, privilage="normal")
    #             wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_created)))
    #             wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_created)))

    # def test_assign_normal_users_to_team(self, driver):
    #     """
    #     These function lets us assign the normal users to required team
    #     """
    #     wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
    #         ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])
        # create_team(driver, name="Demo team", desc="demo")
        # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_team_created)))
        # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_team_created)))
        # back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        # back.click()
        # time.sleep(2)
        # wait = WebDriverWait(driver, 20, poll_frequency=2)
        # settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        # driver.execute_script("arguments[0].click();", settingstab)
        #
        # teams = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
        # teams.click()
        #
        # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        # search = wait.until(EC.element_to_be_clickable((By.XPATH, search_field)))
        # search.send_keys("Demo team")

        # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        # action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
        # action_dp.click()
        # addusers = wait.until(EC.element_to_be_clickable((By.XPATH, add_users)))
        # addusers.click()
        #
        # # select users pop up
        # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        # select_users_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, select_users_dp)))
        # select_users_dropdown.click()
        # select_users_dropdown.send_keys('james')  # Add 1st Normal user
        # select_users_dropdown.send_keys(Keys.ENTER)
        # select_users_dropdown.click()
        # select_users_dropdown.send_keys('Niki')  # Add 2nd Normal user
        # select_users_dropdown.send_keys(Keys.ENTER)
        #
        # select_user_submit = wait.until(EC.element_to_be_clickable((By.XPATH, select_users_submit)))
        # select_user_submit.click()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        # count_of_users = wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='el-table__row'][1]/td[3]//p"))).text
        # assert count_of_users == '2'

    # def test_warning_message_for_creating_existing_team(self, driver):
    #     """
    #     These function lets us check the warning message if we try to create team same as existing team.
    #     """
    #     wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
    #                 ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])
    #     create_team(driver, name="Demo team", desc="demo")
    #     time.sleep(2)
    #     wait = WebDriverWait(driver, 10, poll_frequency=1)
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    #     warning_msg = wait.until(EC.element_to_be_clickable(
    #             (By.XPATH, "//p[contains(text(), ' * Team with this name already exists.')]"))).text
    #     print("\n", warning_msg)
    #     assert warning_msg == "* Team with this name already exists."
    #     close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='×']")))
    #     close_popup.click()

    def test_warning_message_for_max_char(self, driver):
        """
        These function lets us check the warning message if the team 'name' field reaches the max characters.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        teams = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
        teams.click()
        create = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_btn)))
        create.click()
        name = wait.until(EC.element_to_be_clickable((By.XPATH, team_name)))
        name.send_keys('Tests' * 10)
        warning_msg = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//p[contains(text(), ' * Ensure this field has no more than 50 characters.')]"))).text
        print('\n', warning_msg)
        assert warning_msg == "* Ensure this field has no more than 50 characters."
        desc = wait.until(EC.element_to_be_clickable((By.XPATH, team_desc)))
        desc.send_keys('These is testing team where only testers are assigned to these team')
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_team_submit)))
        submit.click()
        time.sleep(2)

        # Delete the above team
        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
        action_dp.click()
        dele = wait.until(EC.element_to_be_clickable((By.XPATH, delete)))
        dele.click()
        click_yes = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "/html/body/div/div/div[2]/section/div/div[1]/div/div/div[2]/div"
                                                  "/div/div[10]/div/div[1]/div/div/footer/div/div/button[2]")))
        click_yes.click()
        driver.refresh()

    # def test_delete_users_and_respective_domain(self, driver):
    #     """
    #     These function lets us delete the users.
    #     """
    #     for i in ["Josemourinho@gmail.com", "pepguardiola@gmail.com", "Jameshunt@gmail.com", "Nikilauda@gmail.com"]:
    #         delete_users(driver, user_email=i)
    #
    # def test_delete_domain(self, driver):
    #     delete_domain(driver, domain_name="gmail.com")

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
