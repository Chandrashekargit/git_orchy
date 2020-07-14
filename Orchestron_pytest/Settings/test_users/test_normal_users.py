from Settings.test_users.create_users import *
from Settings.test_domains.create_domain import *
from Settings.test_domains.delete_domain import *
from Settings.test_users.delete_user import *
from Settings.test_teams.delete_team import *
from pytest import mark

firstnames = ['Jose', 'pep']
lastnames = ['mourinho', 'guardiola']


@mark.normal_user
class CreateNormalUserAndAssertWarningMsgTests:
    def test_for_normal_users(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        create_domain(driver, domain_name="xyz.com")

        for (firstname, lastname) in zip(firstnames, lastnames):
            if firstname == "Jose":
                create_user(driver, fn=firstname, ln=lastname, email_id=firstname+lastname+"@xyz.com", un=firstname, privilage="normal")
                wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_created)))
                wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_created)))
                back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
                back.click()
            else:
                create_user(driver, fn=firstname, ln=lastname, email_id=firstname+lastname+"@xyz.com", un=firstname, privilage="normal")
                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, wrng_msg_for_creating_existing_team))).text
                print("\n", warning_msg)
                assert warning_msg == "* Team with this name already exists."
                close_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.='×']")))
                close_pop_up.click()
                back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
                back.click()

    def test_delete_users(self, driver):
        delete_users(driver, user_email="Josemourinho@xyz.com")
        driver.refresh()

    def test_delete_domain(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        delete_domain(driver, domain_name="xyz.com")
        back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        back.click()

    def test_delete_team(self, driver):
        delete_team(driver, team_name="Demo X team")
