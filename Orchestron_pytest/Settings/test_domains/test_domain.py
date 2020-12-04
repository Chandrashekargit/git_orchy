from pytest import mark
from Settings.test_users.create_users import *
from Settings.test_domains.delete_domain import *
from Settings.test_domains.create_domain import *
from Settings.test_users.delete_user import *
from spinner.spinner import *

"""
> Tests if we can create new domain
> Tests to create domains with positive and negative domain name formats.
> Tests the warning message if we try to create existing domain names.
> Tests to delete domain while users with that domain exist and asserts the warning message(if any).
> Tests if we can delete the domain.
> Tests if we can update the domain name while users with that domain name exist and assert the warning message(if any).
"""

domain_names = ['@gmail.com', 'demo!@.com', 'demo.com ', ' demo.com']


@mark.test_domain
class CheckForAllTheWarningMessagesUnderDomainSectionTests:
    def test_invalid_domain_names(self, driver):
        """
        These function lets us test positive and negative domain names.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        for domain in domain_names:
            create_domain(driver, domain_name=domain)
            warning_msg = wait.until(EC.visibility_of_element_located((By.XPATH, wrng_msg_for_invalid_domain_name)))
            assert warning_msg.text == "* Please provide valid Domain."
            close_pop_up = WebDriverWait(driver, 3, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, domain_create_popup_close)))
            close_pop_up.click()

            back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
            back.click()

    def test_warning_message_if_we_create_new_domain_with_existing_domain_name(self, driver):
        """
        These function lets us test the warning message if we try to create existing domain name(s).
        """
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        # calling the function 'create_domain_script'
        create_domain(driver, domain_name="we45.com")

        stop_till_spinner_is_invisible(driver)
        warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, warning_msg_for_same_domain_name))).text
        assert warning_msg == "* organization email domain configuration with this domain name already exists."

        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, domain_create_popup_close)))
        close_popup.click()
        driver.refresh()

    def test_if_we_can_delete_domain_while_users_with_that_domain_exist(self, driver):
        """
        These function lets us test if we can delete domain while users with that domain name exist.
        """
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        # creates a domain
        create_domain(driver, domain_name="abc.com")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_created)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        back.click()

        # creates a user
        create_user(driver, fn="Jose", ln="mourinho", email_id="Josemourinho@abc.com", un="Jose", privilage="Admin")
        stop_till_spinner_is_invisible(driver)
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_created)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        back.click()

        # go to domain section and try to delete the domain and assert the warning message
        delete_domain(driver, domain_name="abc.com")
        warning_msg = wait.until(EC.visibility_of_element_located((By.XPATH, warning_msg_for_delete_domain_while_user_exist))).text
        assert warning_msg == "* User(s) with this domain configuration already exists. Please delete users to delete this domain configuration."
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='×']")))
        close_popup.click()
        back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        back.click()

        # delete above user
        delete_users(driver, user_email="Josemourinho@abc.com")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_deleted)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_deleted)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        back.click()

        # delete above domain
        delete_domain(driver, domain_name="abc.com")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        back.click()

    def test_if_we_can_update_domain_name_while_users_exists_with_that_domain_name(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
                ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        # creates a domain
        create_domain(driver, domain_name="abc.com")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_created)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        back.click()

        # creates a user
        create_user(driver, fn="Jose", ln="mourinho", email_id="Josemourinho@abc.com", un="Jose", privilage="Admin")
        stop_till_spinner_is_invisible(driver)
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_created)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        back.click()

        # go to domain section and try to update the domain name and assert the warning message
        settingstab = wait.until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
        driver.execute_script("arguments[0].click();", settingstab)

        stop_till_spinner_is_invisible(driver)
        domain = wait.until(EC.element_to_be_clickable((By.XPATH, domain_section)))
        domain.click()

        stop_till_spinner_is_invisible(driver)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, domain_search_field)))
        search.clear()
        search.send_keys('abc.com')

        stop_till_spinner_is_invisible(driver)
        action_dp = wait.until(EC.element_to_be_clickable((By.XPATH, doamin_action_dropdown)))
        action_dp.click()
        update = wait.until(EC.element_to_be_clickable((By.XPATH, domain_actiondp_update)))
        update.click()

        stop_till_spinner_is_invisible(driver)
        update_domain_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Domain']")))
        update_domain_name.clear()
        update_domain_name.send_keys('abcd.com')

        domain_update_name_submit = wait.until(EC.element_to_be_clickable((By.XPATH, domain_name_submit)))
        domain_update_name_submit.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(5)
        # warning_msg = wait.until(EC.visibility_of_element_located((By.XPATH, warning_msg_if_we_update_domain_name_while_user_exist)))
        warning_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/p/text()")))
        print(warning_msg.text)
        assert warning_msg == "* User(s) with this domain configuration already exists, to edit domain name please delete the users."

        # # delete above user
        # delete_users(driver, user_email="Josemourinho@abc.com")
        # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_user_deleted)))
        # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_user_deleted)))
        # back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        # back.click()
        #
        # # delete above domain
        # delete_domain(driver, domain_name="abc.com")
        # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
        # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_deleted)))
        # back = wait.until(EC.element_to_be_clickable((By.XPATH, back_btn)))
        # back.click()