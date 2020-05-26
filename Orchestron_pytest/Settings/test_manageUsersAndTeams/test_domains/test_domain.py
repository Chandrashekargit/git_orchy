import time
import pytest
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import *
from Settings.test_manageUsersAndTeams.test_domains.domain_script import *
from Settings.test_manageUsersAndTeams.test_users.create_users_script import *
from Settings.test_manageUsersAndTeams.test_domains.delete_domain import *

"""
> Tests if we can create new domain
> Tests to create domains with positive and negative domain name formats.
> Tests the warning message if we try to create existing domain names.
> Tests to delete domain while users with that domain exist and asserts the warning message(if any).
> Tests if we can delete the domain.
> Tests if we can update the domain name while users with that domain name exist and assert the warning message(if any).
"""


@mark.test_domain
class CheckForAllTheWarningMessagesUnderDomainSectionTests:
    @mark.parametrize('domain_names', [
        "demo123.com", '@gmail.com', 'demo!@.com', 'demo.com ', ' demo.com']
                      )
    def test_valid_and_invalid_domain_names(self, driver, domain_names):
        """
        These function lets us test positive and negative domain names.
        """
        wait = WebDriverWait(driver, 6, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)
        time.sleep(1)
        domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
        domain.click()
        # driver.execute_script("window.scrollTo(0, 900);")
        time.sleep(1)
        create = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create)))
        create.click()
        domain_name = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_field)))
        domain_name.send_keys(domain_names)
        try:
            domain_submit = WebDriverWait(driver, 3, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
            domain_submit.click()
        except TimeoutException:
            print("\n***Domain can't be registered, please check the format***")
            close_pop_up = WebDriverWait(driver, 3, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, domain_create_popup_close)))
            close_pop_up.click()
            # driver.refresh()

    def test_warning_message_if_we_create_existing_domain_name(self, driver):
        """
        These function lets us test the warning message if we try to create existing domain name(s).
        """
        wait = WebDriverWait(driver, 6, poll_frequency=2)
        # calling the function 'create_domain_script'
        create_domain_script(driver, domain_names="we45.com")
        time.sleep(2)
        warning_msg = wait.until(
            EC.element_to_be_clickable((By.XPATH, warning_msg_for_same_domain_name))).text
        assert warning_msg == "* organization email domain configuration with this domain name already exists."
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create_popup_close)))
        close_popup.click()
        driver.refresh()

    def test_if_we_can_delete_domain_while_users_with_that_domain_exist(self, driver):
        """
        These function lets us test if we can delete domain while users with that domain name exist.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        # calling the function 'create_domain_script'
        create_domain_script(driver, domain_names="demo.com")
        time.sleep(1.5)

        # go to Users section and create a new user with above domain
        users_section = wait.until(EC.element_to_be_clickable((By.XPATH, users)))
        users_section.click()
        # calling the function 'create_user'
        create_user(driver, fn="Jose", ln="mourinho", email_id="Josemourinho@demo.com", un="Jose", privilage="admin")
        time.sleep(2)

        # go back to domain section and try to delete the domain, we should see the warning message and not be able to
        # delete the domain.
        delete_domain(driver, domain_name="demo.com")

        warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, warning_msg_for_delete_domain_while_user_exist))).text
        assert warning_msg == "* User with this domain configuration alredy exists please delete users if want to " \
                              "delete this domain configuration"
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']")))
        close_popup.click()
        driver.refresh()

        # clear the above data entered
        # go back to user section and delete the user
        users_section = wait.until(EC.element_to_be_clickable((By.XPATH, users)))
        users_section.click()
        users_action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown)))
        users_action_dp.click()
        del_user = wait.until(EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown_delete)))
        del_user.click()
        time.sleep(1)
        del_user_yes = wait.until(EC.element_to_be_clickable((By.XPATH, delete_confirmation_yes)))
        del_user_yes.click()
        time.sleep(2)

        # go back to domain section and delete the Domain, recalling the function 'delete_domain'.
        delete_domain(driver, domain_name="demo.com")
        time.sleep(1)
        delete_domain(driver, domain_name="demo123.com")
        time.sleep(1)
        driver.refresh()

    def test_if_we_can_update_domain_name_while_users_exists_with_that_domain_name(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)
        # click on domain
        domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
        domain.click()

        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, doamin_action_dropdown)))
        action_dp.click()

        search = wait.until(EC.element_to_be_clickable((By.XPATH, domain_search_field)))
        search.clear()
        search.send_keys('we45')

        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, doamin_action_dropdown)))
        action_dp.click()
        update = wait.until(EC.element_to_be_clickable((By.XPATH, domain_actiondp_update)))
        update.click()

        update_domain_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Domain']")))
        update_domain_name.clear()
        update_domain_name.send_keys('we45.co')

        domain_update_name_submit = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
        domain_update_name_submit.click()

        warning_msg = wait.until(
            EC.element_to_be_clickable((By.XPATH, warning_msg_if_we_update_domain_name_while_user_exist))).text
        assert warning_msg == "* User with this domain configuration alredy exists please delete users " \
                              "if want to edit this domain configuration"
