# import time
# import pytest
# from pytest import mark
# from selenium.common.exceptions import *
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from xpath.profile_module_xpath import *
# from Profile_Logout.test_orchy_profile.change_pw_script import change_pw
#
#
# def test_change_pw_rules_visibility(driver):
#     wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
#         NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
#
#     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, profile_dropdown)))
#     dropdown.click()
#
#     select_profile = wait.until(EC.element_to_be_clickable((By.XPATH, profile)))
#     select_profile.click()
#
#     move_to_change_pw_section = wait.until(EC.element_to_be_clickable((By.XPATH, change_pw_section)))
#     move_to_change_pw_section.click()
#
#     # assert if all the rules to change the password are visible
#     rules_to_set_pw = wait.until(EC.element_to_be_clickable((By.XPATH, pw_rules))).text
#     assert "Longer than 7 characters\nHas a capital letter\nHas a lowercase letter\nHas a number\nHas a special character" in rules_to_set_pw
#
#     # assert if still rules are visible after entering the current password
#     current_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, current_pw)))
#     current_password_field.send_keys("Test@1234")
#     assert "Longer than 7 characters\nHas a capital letter\nHas a lowercase letter\nHas a number\nHas a special character" in rules_to_set_pw
#
#     rules = {"T": "Has a capital letter",
#              "e": "Has a lowercase letter",
#              "1": "Has a number",
#              "!@#": "Has a special character",
#              "abcdefghi": "Longer than 7 characters\nHas a lowercase letter",
#              "Test@1234": "Longer than 7 characters\nHas a capital letter\nHas a lowercase letter\nHas a number\nHas a special character"
#              }
#
#     def check_which_rules_present():
#         """
#         These function asserts if correct message/rule is disabled from UI when user/admin enters the one syllable of PW.
#         """
#         for (k, r) in rules.items():
#             new_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, new_pw)))
#             new_password_field.clear()
#             new_password_field.send_keys(k)
#             time.sleep(1)
#             assert r not in "//div[@class='tab-pane active']//div[@class='col-3']/div"
#     check_which_rules_present()
#
#
# def test_warning_msgs_of_change_pw(driver):
#     """
#     > These function:
#         - lets us assert the warning message when user/admin tries to change the pw, which is same as old pw.
#         - lets us assert the warning message when user/admin tries to change the pw, by entering invalid 'current password'.
#     """
#     current_passwords = ["Test@1234", "Test@234"]
#     new_passwords = ["Test@1234", "Test@1234"]
#     confirm_new_passwords = ["Test@1234", "Test@1234"]
#
#     for (current_password, new_password, confirm_new_password) in zip(current_passwords, new_passwords, confirm_new_passwords):
#         wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[
#             NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
#         # calling the function 'change_pw()'
#         change_pw(driver, Current_password=current_password, New_password=new_password,Confirm_new_password=confirm_new_password)
#         # lets us assert the warning message when user/admin tries to change the pw, which is same as old pw.
#         if current_password == "Test@1234" and new_password == "Test@1234":
#             warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, change_pw_warning_msg1))).text
#             assert "* Old password cannot be reused!" in warning_msg
#         # lets us assert the warning message when user/admin tries to change the pw, by entering invalid 'current password'.
#         elif current_password == "Test@234":
#             warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, change_pw_warning_msg2))).text
#             assert "* Invalid credenetials!" in warning_msg
#
#
# @mark.change_pw
# @mark.parametrize('current_password, new_password, confirm_new_password', [
#     pytest.param(" ", "Test@1234", " ", marks=pytest.mark.xfail(reason="current_pw field is empty and confirm_new_pw != new_pw")),
#     pytest.param("Test@1234", " ", " ", marks=pytest.mark.xfail(reason="new_pw and confirm_new_pw fields are empty")),
#     pytest.param("Test@1234", "Test@1234", "test@1234", marks=pytest.mark.xfail(reason="confirm_new_pw != new_pw"))
# ])
# def test_if_submit_btn_visible_or_not(driver, current_password, new_password, confirm_new_password):
#     """
#     These function lets us test if 'Submit' button is visible oor not when one of the fields doesn't match the
#     required guidelines.
#     """
#     # calling the function 'change_pw()'
#     change_pw(driver, Current_password=current_password, New_password=new_password, Confirm_new_password=confirm_new_password)
