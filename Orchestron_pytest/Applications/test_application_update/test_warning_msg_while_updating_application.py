from pytest import mark
from Applications.test_delete_application.delete_app import delete_app
from Applications.test_create_applications.create_app import *


@mark.update_feature_wrng_msgs
class UpdateFeatureWarningMessagesTests:
    def test_create_app(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        for i in ["update_warning_messages", '2']:
            create_apps(driver, application_name=i, url="http://demo.com")
            stop_till_spinner_is_invisible(driver)
            success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
            assert success_msg.text == "Application has been created successfully!"
            wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_warning_messaege_while_updating_application(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[ElementClickInterceptedException,
                                   TimeoutException, ElementNotVisibleException])

        # search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, search)))
        # search_tab.send_keys("DemoApplication")

        stop_till_spinner_is_invisible(driver)
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        stop_till_spinner_is_invisible(driver)
        select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='update_warning_messages']")))
        select_individual_app.click()

        stop_till_spinner_is_invisible(driver)
        time.sleep(2)
        action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        action.click()
        update_app = wait.until(EC.element_to_be_clickable((By.XPATH, update)))
        update_app.click()

        stop_till_spinner_is_invisible(driver)
        update_name = wait.until(EC.element_to_be_clickable((By.XPATH, update_app_name)))
        update_name.clear()
        update_name.send_keys("Demo " * 10)

        name_warning_msg = wait.until(EC.visibility_of_element_located((By.XPATH, update_name_warning_msg))).text
        assert name_warning_msg == "* Ensure this field has no more than 50 characters."

        update_name = wait.until(EC.element_to_be_clickable((By.XPATH, update_app_name)))
        update_name.clear()
        update_name.send_keys(2)

        update_URL = wait.until(EC.element_to_be_clickable((By.XPATH, update_url)))
        update_URL.clear()
        update_URL.send_keys("http://!1!!1.com")

        submit = wait.until(EC.element_to_be_clickable((By.XPATH, update_submit_btn)))
        submit.click()

        stop_till_spinner_is_invisible(driver)
        url_warning_msg = wait.until(EC.element_to_be_clickable((By.XPATH, update_url_warning_msg))).text
        assert "* Enter a valid URL." in url_warning_msg

        existing_app_name_wrng_msg = wait.until(EC.visibility_of_element_located((By.XPATH, existing_application_warning_msg)))
        assert existing_app_name_wrng_msg.text == '* Application with this name already exists.'

        stop_till_spinner_is_invisible(driver)
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close_popup.click()
        driver.refresh()

    def test_delete_app(self, driver):
        for i in ["//label[text()='update_warning_messages']", "//label[contains(text(),'2')]"]:
            delete_app(driver, application=i)
