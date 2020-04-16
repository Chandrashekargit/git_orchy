import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from Settings.test_manageUsersAndTeams.create_users_script import *


firstnames = ['Jose', 'pep', 'James', 'Niki']
lastnames = ['mourinho', 'guardiola', 'hunt', 'lauda']

"""
Before running these file please make sure there is domain called 'gmail.com'
"""


@mark.settings_smoke
class UsersWarningMessagesAndCreateAndDeleteUsersTests:
    def test_domain_not_exist_warning_msg(self, driver):
        """
        These function lets us check the warning message when we try to create the users
        outside the registered domains.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        create_user(driver, fn="Jose", ln="mourinho", email_id="Josemourinho@xyz.com", un="Jose", privilage="admin")
        time.sleep(2)

        warning_message = "//p[contains(text(),'Your trying to create users outside organization please add the respective domains in configuration')]"
        e = wait.until(EC.presence_of_element_located((By.XPATH, warning_message))).text
        print('\n', e)

        if e:
            print('\nplease register the domain.')
            assert e == "* Your trying to create users outside organization please add the respective domains in configuration"
        else:
            print('\nUser successfully created')
        time.sleep(2)
        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "/html/body/div/div/div[2]/section/div/div["
                                                              "1]/div/div/div[2]/div/div/div[7]/div/div["
                                                              "1]/div/div/header/button")))
        close_pop_up.click()

    def test_create_user_with_existing_mail_and_username_check_warning_msg(self, driver):
        """
        These function lets us check the warning message if admin tries to create the new user with
        existing username and email
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        settingstab = wait.until(
            EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        # click on the create button where we get a pop up to create the normal user/admin
        create = WebDriverWait(driver, 10, poll_frequency=1.5).until(
            EC.presence_of_element_located((By.XPATH, create_btn)))
        create.click()
        firstName = wait.until(EC.presence_of_element_located((By.XPATH, first_name)))
        firstName.send_keys("c")
        lastName = wait.until(EC.presence_of_element_located((By.XPATH, last_name)))
        lastName.send_keys("s")
        email = wait.until(EC.presence_of_element_located((By.XPATH, e_mail)))
        email.send_keys("chandrashekar@we45.com")
        username = wait.until(EC.presence_of_element_located((By.XPATH, user_name)))
        username.send_keys("c")
        usertype = wait.until(EC.presence_of_element_located((By.XPATH, user_type)))
        usertype.send_keys("admin")
        usertype.send_keys(Keys.ENTER)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_submit)))
        submit.click()
        time.sleep(2)

        email_warning_message1 = wait.until(EC.presence_of_element_located((By.XPATH,
                                    "//p[contains(text(), ' * user with this email address already exists.')]"))).text
        username_warning_message2 = wait.until(EC.presence_of_element_located((By.XPATH,
                                   "//p[contains(text(), ' * This user name has already been added.')]"))).text
        assert email_warning_message1 == "* user with this email address already exists."
        assert username_warning_message2 == "* This user name has already been added."
        time.sleep(2)

        close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "/html/body/div/div/div[2]/section/div/div["
                                                              "1]/div/div/div[2]/div/div/div[7]/div/div["
                                                              "1]/div/div/header/button")))
        close_pop_up.click()

    @mark.create_users
    def test_create_users(self, driver):
        """
        These function lets us create new users
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        for firstname, lastname in zip(firstnames, lastnames):
            """click on settings tab"""
            settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
            driver.execute_script("arguments[0].click();", settingstab)

            """click on the create button where we get a pop up to create the normal user/admin"""
            create = WebDriverWait(driver, 10, poll_frequency=1.5).until(EC.presence_of_element_located((By.XPATH, create_btn)))
            create.click()
            firstName = wait.until(EC.presence_of_element_located((By.XPATH, first_name)))
            firstName.send_keys(firstname)
            lastName = wait.until(EC.presence_of_element_located((By.XPATH, last_name)))
            lastName.send_keys(lastname)
            email = wait.until(EC.presence_of_element_located((By.XPATH, e_mail)))
            email.send_keys(firstname + lastname + "@gmail.com")
            username = wait.until(EC.presence_of_element_located((By.XPATH, user_name)))
            username.send_keys(firstname)

            if firstname == 'Jose' or firstname == 'James':
                usertype = wait.until(EC.presence_of_element_located((By.XPATH, user_type)))
                usertype.send_keys("normal")
                usertype.send_keys(Keys.ENTER)
            else:
                usertype = wait.until(EC.presence_of_element_located((By.XPATH, user_type)))
                usertype.send_keys("admin")
                usertype.send_keys(Keys.ENTER)

            submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_submit)))
            submit.click()
            time.sleep(1)
            driver.refresh()

    def test_assign_normal_users_to_team(self, driver, create_team):
        """
        These function lets us assign the normal users to required team
        :param create_team: It creates new team where normal users can be assigned to that team
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        teams = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
        teams.click()

        search = wait.until(EC.element_to_be_clickable((By.XPATH, search_field)))
        search.send_keys('Testing team')

        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
        action_dp.click()
        addusers = wait.until(EC.element_to_be_clickable((By.XPATH, add_users)))
        addusers.click()

        # select users pop up
        select_users_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, select_users_dp)))
        select_users_dropdown.click()
        select_users_dropdown.send_keys('james')  # Add 1st Normal user
        select_users_dropdown.send_keys(Keys.ENTER)
        select_users_dropdown.click()
        select_users_dropdown.send_keys('jose')  # Add 2nd Normal user
        select_users_dropdown.send_keys(Keys.ENTER)

        select_user_submit = wait.until(EC.element_to_be_clickable((By.XPATH, select_users_submit)))
        select_user_submit.click()
        time.sleep(2)

        count_of_users = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '2')]"))).text
        assert count_of_users == '2'

    def test_warning_message_for_creating_existing_team(self, driver, create_team):
        """
        These function lets us check the warning message if we try to create team same as existing team
        :param create_team: It creates new team.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        warning_msg = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//p[contains(text(), ' * Team with this name already exists.')]"))).text
        print("\n", warning_msg)
        assert warning_msg == "* Team with this name already exists."
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                 "/html/body/div/div/div[2]/section/div/div[1]/div/div/div[2]"
                                                  "/div/div/div[9]/div/div[1]/div/div/header/button")))
        close_popup.click()

    def test_warning_message_for_max_char(self, driver):
        """
        These function lets us check the warning message if the team 'name' field reaches the max characters
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

    @mark.delete_user
    def test_delete_users(self, driver):
        """
        These function lets us delete the users.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        for i in range(4):
            driver.execute_script("window.scrollTo(0, 900);")
            settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
            driver.execute_script("arguments[0].click();", settingstab)
            driver.execute_script("window.scrollTo(0, 900);")

            action = WebDriverWait(driver, 10, poll_frequency=1.5).until(
                EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown)))
            action.click()
            delete_btn = WebDriverWait(driver, 10, poll_frequency=1.5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/ul/li[3]/a/li")))
            delete_btn.click()
            delete_pop_up = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Yes')]")))
            delete_pop_up.click()
            driver.refresh()

    def test_forWarningMessageWhenNoNormalUserPresentAndClickOnAddusers(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        teams = wait.until(EC.element_to_be_clickable((By.XPATH, team_section)))
        teams.click()
        driver.execute_script("window.scrollTo(0, 900);")
        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, teams_section_action_dropdown)))
        action_dp.click()
        addusers = wait.until(EC.element_to_be_clickable((By.XPATH, add_users)))
        addusers.click()
        warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH,
                        "//p[contains(text(), ' * Note: Please create normal user to assign them to a team .')]"))).text
        assert warning_msg == "* Note: Please create normal user to assign them to a team ."
