from Applications.test_create_applications.create_app import *
from Applications.test_delete_application.delete_app import *
from pytest import mark


@mark.test_update_feature
class UpdateFeatureTests:
    def test_create_app(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        create_apps(driver, application_name="update feature", url="https://spotify.com/")

        stop_till_spinner_is_invisible(driver)
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
        assert success_msg.text == "Application has been created successfully!"
        wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))

    def test_application_update_feature(self, driver, app_name="//label[contains(text(),'update feature')]",
                updated_app_name="New updated name", updated_url="https://checkupdatefeature.com", platform="Ruby"):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
             NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        stop_till_spinner_is_invisible(driver)
        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        click_on_individual_app.click()

        stop_till_spinner_is_invisible(driver)
        stop_till_spinner_is_invisible(driver)
        action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        action.click()

        select_update_option = wait.until(EC.element_to_be_clickable((By.XPATH, update)))
        select_update_option.click()

        stop_till_spinner_is_invisible(driver)
        update_name = wait.until(EC.element_to_be_clickable((By.XPATH, update_app_name)))
        update_name.clear()
        update_name.send_keys(updated_app_name)

        stop_till_spinner_is_invisible(driver)
        change_platformtype = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row my-1'][2]//i[@class='el-tag__close el-icon-close']")))
        change_platformtype.click()
        platform_type = wait.until(EC.presence_of_element_located((By.XPATH, app_platform_type)))
        platform_type.send_keys(platform)
        platform_type.send_keys(Keys.ARROW_DOWN)
        platform_type.send_keys(Keys.ENTER)

        url_field = wait.until(EC.presence_of_element_located((By.XPATH, app_url)))
        url_field.clear()
        url_field.send_keys(updated_url)

        team = wait.until(EC.presence_of_element_located((By.XPATH, app_team)))
        team.click()

        submit = wait.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
        submit.click()

        stop_till_spinner_is_invisible(driver)
        wait.until(EC.visibility_of_element_located((By.XPATH, update_success_msg)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, update_success_msg)))

        # assert the updated info
        check_app_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='col-5'][1]//tr[1]/td[2]")))
        assert check_app_name.text == ": "+updated_app_name

        check_url = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='col-5'][1]//tr[2]/td[2]")))
        assert check_url.text == ": "+updated_url

        check_platform = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='col-5'][1]//tr[3]/td[2]")))
        assert check_platform.text == ": "+platform

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'New updated name')]")
