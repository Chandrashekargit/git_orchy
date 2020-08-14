from pytest import mark
from Applications.test_delete_application.delete_app import delete_app
from Applications.test_create_applications.create_app import *


@mark.create_app_negative_tc
class ApplicationNegativeBoundaryValueAnalysisTcTests:
    def test_negative_tc_invalid_url(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        create_apps(driver, application_name="!", url="http://!.com")

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        url_wrng_msg = wait.until(EC.visibility_of_element_located((By.XPATH, invalid_url_wrng_msg)))
        assert url_wrng_msg.text == "* Enter a valid URL."

        close = wait.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        driver.refresh()

    def test_negative_tc_no_value_in_name_field(self, driver):
        wait1 = WebDriverWait(driver, 5, poll_frequency=1)
        create_apps(driver, application_name=" ", url="http://!.com")

        close = wait1.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        driver.refresh()

    def test_negative_tc_no_value_in_url_field(self, driver):
        wait1 = WebDriverWait(driver, 5, poll_frequency=1)
        create_apps(driver, application_name="Demo", url=" ")

        close = wait1.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        driver.refresh()

    def test_all_valid_inputs(self, driver):
        wait1 = WebDriverWait(driver, 5, poll_frequency=1)
        create_apps(driver, application_name="demo application", url="http://demo.com")

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        success_msg = wait1.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait1.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_negative_tc_existing_app_name(self, driver):
        wait = WebDriverWait(driver, 10, poll_frequency=2)
        create_apps(driver, application_name="demo application", url="http://demo.com")

        wrng_msg_for_existing_app = wait.until(EC.visibility_of_element_located((By.XPATH, warning_msg_for_existing_app)))
        assert wrng_msg_for_existing_app.text == "* Application with this name already exists."

        close = wait.until(EC.element_to_be_clickable((By.XPATH, app_pop_up_close_btn)))
        close.click()
        driver.refresh()

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(), 'demo application')]")
