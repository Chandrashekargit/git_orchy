import time
import pytest
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.settings_module_xpath import *
from selenium.common.exceptions import TimeoutException

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
    def create_domain(self, driver, domain_name1):
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
        domain.click()
        driver.execute_script("window.scrollTo(0, 900);")
        create = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create)))
        create.click()
        domain_name = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_field)))
        domain_name.send_keys(domain_name1)
        domain_submit = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
        domain_submit.click()

    @mark.parametrize('domain_names', [
        'demo123.com',
        pytest.param('@gmail.com', marks=pytest.mark.xfail),
        pytest.param('demo!@.com', marks=pytest.mark.xfail),
        pytest.param('demo.com ', marks=pytest.mark.xfail),
        pytest.param(' demo.com', marks=pytest.mark.xfail)
    ])
    def test_valid_and_invalid_domain_names(self, driver, domain_names):
        """
        These function lets us test the positive and negative domain names
        """
        wait = WebDriverWait(driver, 5, poll_frequency=1)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
        domain.click()
        driver.execute_script("window.scrollTo(0, 900);")
        create = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create)))
        create.click()
        domain_name = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_field)))
        domain_name.send_keys(domain_names)
        try:
            domain_submit = WebDriverWait(driver, 3, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
            domain_submit.click()
        except TimeoutException:
            print("\n***Domain can't be registered. please check the format***")
            close_pop_up = WebDriverWait(driver, 3, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, domain_create_popup_close)))
            close_pop_up.click()
            driver.refresh()
        assert wait.until(EC.element_to_be_clickable((By.XPATH,
                                                      "//tr[@aria-rowindex='1']//td[@data-label='Name']/div[text("
                                                      ")='demo123.com']"))).text == "demo123.com "

    def test_warning_message_if_we_create_existing_domain_name(self, driver):
        """
        These function lets us test the warning message if we try to create existing domain name(s).
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        # create existing domain and check the warning message.
        """ calling the function 'create_domain'."""
        self.create_domain(driver, "we45.com")
        time.sleep(2)
        warning_msg = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//p[contains(text(),' * organization email domain configuration with this "
                                        "domain name already exists.')]"))).text
        assert warning_msg == "* organization email domain configuration with this domain name already exists."
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             "/html/body/div/div/div[2]/section/div/div["
                                                             "1]/div/div/div[2]/div/div/div[11]/div[2]/div["
                                                             "1]/div/div/div[2]/div[3]/div[2]/div/div["
                                                             "1]/div/div/header/button")))
        close_popup.click()
        driver.refresh()

    def test_if_we_can_delete_domain_while_users_with_that_domain_exist(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        # create new domain.
        """ calling the function 'create_domain'."""
        self.create_domain(driver, "demo.com")
        time.sleep(1.5)

        # go to Users section and create a new user with above domain
        users_section = wait.until(EC.element_to_be_clickable((By.XPATH, users)))
        users_section.click()
        create = WebDriverWait(driver, 10, poll_frequency=1.5).until(EC.presence_of_element_located((By.XPATH, create_btn)))
        create.click()
        firstName = wait.until(EC.presence_of_element_located((By.XPATH, first_name)))
        firstName.send_keys("Jose")
        lastName = wait.until(EC.presence_of_element_located((By.XPATH, last_name)))
        lastName.send_keys("mourinho")
        email = wait.until(EC.presence_of_element_located((By.XPATH, e_mail)))
        email.send_keys("Josemourinho@demo.com")
        username = wait.until(EC.presence_of_element_located((By.XPATH, user_name)))
        username.send_keys("Jose")
        usertype = wait.until(EC.presence_of_element_located((By.XPATH, user_type)))
        usertype.send_keys("admin")
        usertype.send_keys(Keys.ENTER)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, create_user_submit)))
        submit.click()
        time.sleep(2)

        # go back to domain section and try to delete the domain, we should see the warning message and not be able to
        # delete the domain.
        def delete_domain():
            wait = WebDriverWait(driver, 10, poll_frequency=1)
            domain = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, domain_section)))
            domain.click()
            action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, doamin_action_dropdown)))
            action_dp.click()
            time.sleep(1)
            delete = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, domain_actiondp_delete)))
            delete.click()
            delete_domain_pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, domain_delete_confirm_popup)))
            delete_domain_pop_up.click()

        delete_domain()

        warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             "/html/body/div/div/div[2]/section/div/div[1]/div/div/"
                                                             "div[2]/div/div/div[11]/div[2]/div[1]/div/div/div[2]/"
                                                             "div[3]/div[3]/div/div[1]/div/div/div/div/p"))).text
        assert warning_msg == "* User with this domain configuration alredy exists please delete users if want to " \
                              "delete this domain configuration"
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             "/html/body/div/div/div[2]/section/div/div[1]/div/div/"
                                                             "div[2]/div/div/div[11]/div[2]/div[1]/div/div/div[2]/"
                                                             "div[3]/div[3]/div/div[1]/div/div/footer/div/button")))
        close_popup.click()

        # clear the data
        # go back to user section and delete the user
        users_section = wait.until(EC.element_to_be_clickable((By.XPATH, users)))
        users_section.click()
        users_action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, users_section_action_dropdown)))
        users_action_dp.click()
        del_user = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable((By.XPATH, action_dp_delete)))
        del_user.click()
        del_user_yes = wait.until(EC.element_to_be_clickable((By.XPATH, delete_confirmation_yes)))
        del_user_yes.click()
        time.sleep(2)

        # go back to domain section and delete the Domain, recalling the function 'delete_domain'.
        delete_domain()
        delete_domain()
        driver.refresh()

    def test_if_we_can_update_domain_name_while_users_exists_with_that_domain_name(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        domain = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable((By.XPATH, domain_section)))
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

        update_domain_name = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Domain' and @value='we45.com']")))
        update_domain_name.clear()
        update_domain_name.send_keys('we45.co')

        domain_update_name_submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-content']//button[contains(text(),'Create')]")))
        domain_update_name_submit.click()

        warning_msg = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/section/div/div[1]/div/div/div[2]/div/"
                                                  "div/div[11]/div[2]/div[1]/div/div/div[2]/div[3]/div[4]/div/div[1]/"
                                                  "div/div/div/div/p"))).text
        assert warning_msg == "* User with this domain configuration alredy exists please delete users " \
                              "if want to edit this domain configuration"
