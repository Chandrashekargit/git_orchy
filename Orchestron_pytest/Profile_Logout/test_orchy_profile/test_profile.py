import time
from pytest import mark
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from xpath.profile_module_xpath import *
from Profile_Logout.test_orchy_profile.profile_script import ProfileScript

first_names1 = [" ", "c", "c123!C", "1234567890", "!@#$%^&*()_+", " ", "chandra"]
last_names1 = [" ", "s", "s123!S", "1234567890", "!@#$%^&*()_+", "shekar", " "]


@mark.profile
class ProfileFeatureTests:
    def test_profile_feature1(self, driver):
        """
        These function lets us test if users with different naming sense can be registered.
        In these function we only handle first name, last name but not email field (just for lucidity)
        """
        for (fn, sn) in zip(first_names1, last_names1):
            ProfileScript(driver, firstName=fn, secondName=sn)    # calling the function 'profile script'.
            try:
                submit_btn = WebDriverWait(driver, 3, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, submit)))
                submit_btn.click()
                print("submit button clicked")
                time.sleep(6)
            except Exception as e:
                print("Submit button not visible")

    def test_profile_feature2(self, driver):
        """
        These function lets us check all the warning messages of first and second name fields.
        In these function we only handle first name, last name but not email field (just for lucidity)
        """
        first_names2 = ["c"*30, " ", "c"*30]
        last_names2 = [" ", "s"*30, "s"*30]
        for (fn, sn) in zip(first_names2, last_names2):
            ProfileScript(driver, firstName=fn, secondName=sn)   # calling the function 'profile script'.
            wait = WebDriverWait(driver, 3, poll_frequency=1, ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
            warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, warning_message1))).text

            assert "* Ensure this field has no more than 30 characters." in warning_msg

            try:
                submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, submit)))
                submit_btn.click()
                print("submit button clicked", fn, sn)
                time.sleep(6)
            except:
                print("Submit button not visible", fn, sn)

    def test_profile_feature3(self, driver):
        """
        These function lets us test if oneself's email can be updated and its warning message.
        These function lets us test the warning message if email field is empty.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, profile_dropdown)))
        dropdown.click()

        select_profile = wait.until(EC.element_to_be_clickable((By.XPATH, profile)))
        select_profile.click()

        email = wait.until(EC.element_to_be_clickable((By.XPATH, e_mail)))
        email.clear()

        warning_msg1 = wait.until(EC.element_to_be_clickable((By.XPATH, email_field_warning_message1))).text
        assert "* Please Provide Valid Email" in warning_msg1

        email.send_keys("chandrashekar@we45.co")
        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, submit)))
        submit_btn.click()

        warning_msg2 = wait.until(EC.element_to_be_clickable((By.XPATH, email_field_warning_message2))).text
        assert "* You cannot update the email! Please contact the administrator" in warning_msg2
