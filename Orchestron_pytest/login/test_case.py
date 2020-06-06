from pytest import mark
import time
from login.Page_object import PageObjectForLoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.login_xpath import *
from xpath.Application_module_xpath import *
from selenium import webdriver


emails = ['chandrashekar@we45.com', 'chandrashekar@we45.com', 'chandrashekr@we45.com', 'Chandrashekar@we45.com',
             'chandra@we45.com', ' ', 'chandrashekar@we45.com', ' ', 'chandrashekar@we45.com']

passwords = ['Test@134', 'test@134', 'Test@1234', 'Test@1234', 'welcome@1234', 'Test@1234', ' ', ' ', 'Test@1234']


@mark.login
def test_login_feature():
    for (e, p) in zip(emails, passwords):
        browser = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
        lg = PageObjectForLoginPage(driver=browser)
        lg.go()
        time.sleep(2)
        lg.enter_email_or_username(email_id=e)
        lg.enter_password(password=p)
        lg.click_login_btn()
        if e == 'chandrashekar@we45.com' and p == 'Test@134' or \
           e == 'chandrashekar@we45.com' and p == 'test@134' or \
           e == 'chandrashekr@we45.com' and p == 'Test@1234' or \
           e == 'Chandrashekar@we45.com' and p == 'Test@1234' or \
           e == 'chandra@we45.com' and p == 'welcome@1234':
            # Checks if the warning is displayed.
            warning_msg = lg.wait.until(EC.presence_of_element_located((By.XPATH, warning_message1))).is_displayed()
            print(warning_msg)
            print("\nInvalid cred's")
            # prints out the text of warning message.
            warning_msg1 = lg.wait.until(EC.presence_of_element_located((By.XPATH, warning_message1))).text
            print(warning_msg1)
            close_warning_msg = lg.wait.until(EC.presence_of_element_located((By.XPATH, close_warning_message1)))
            close_warning_msg.click()

            assert "Unable to log in with provided credentials." in warning_msg1
            browser.quit()
        # check for blank username field, check for blank password field, both fields blank,
        elif e == ' ' and p == 'Test@1234' or e == 'chandrashekar@we45.com' and \
                p == ' ' or e == ' ' and p == ' ':
            WebDriverWait(browser, 10, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, warning_message2))).is_displayed()
            print("\nemail or PW field can't be empty")
            warning_msg2 = WebDriverWait(browser, 10, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, warning_message2))).text
            assert warning_msg2 == "* This field may not be blank."
            browser.quit()
        # valid cred's
        elif e == 'chandrashekar@we45.com' and p == 'Test@1234':
            time.sleep(2)
            assert browser.current_url == url + 'org/dashboard'
            browser.quit()
