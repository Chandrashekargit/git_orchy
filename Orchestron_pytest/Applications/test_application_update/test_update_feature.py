from Applications.test_create_applications.create_app import *
from Applications.test_delete_application.delete_app import *

class UpdateFeatureTests:
    def test_create_app(self, driver):
        create_apps(driver, application_name="update feature", url="https://spotify.com/")

        # waits until the submit is invisible
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))
        # waits until the Loading symbol is invisible
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

    def test_application_update_feature(self, driver, app_name="//label[contains(text(),'update feature')]", updated_app_name="New updated name", updated_url="https://checkupdatefeature.com"):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

        stop_till_spinner_is_invisible(driver)
        applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
        applicationTab.click()

        stop_till_spinner_is_invisible(driver)
        click_on_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
        click_on_individual_app.click()

        action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
        action.click()

        select_update_option = wait.until(EC.element_to_be_clickable((By.XPATH, update)))
        select_update_option.click()

        update_name = wait.until(EC.element_to_be_clickable((By.XPATH, update_app_name)))
        update_name.clear()
        update_name.send_keys(updated_app_name)

        url_field = wait.until(EC.presence_of_element_located((By.XPATH, app_url)))
        url_field.clear()
        url_field.send_keys(updated_url)

        submit = wait.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
        submit.click()

        stop_till_spinner_is_invisible(driver)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//p[.='Application has been updated successfully!']")))
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//p[.='Application has been updated successfully!']")))

        # assert the updated info
        check_app_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='col-5'][1]//tr[1]/td[2]")))
        assert check_app_name.text == ":"+updated_app_name

        check_url = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='container-fluid']//div[@class='col-5'][1]//tr[2]/td[2]")))
        assert check_url.text == ":"+updated_url

    def test_delete_app(self, driver):
        delete_app(driver, application="//label[contains(text(),'update feature')]")
