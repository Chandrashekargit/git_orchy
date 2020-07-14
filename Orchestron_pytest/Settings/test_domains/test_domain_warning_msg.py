from Settings.test_domains.delete_domain import *
from Settings.test_domains.create_domain import *

class CheckDomainWarningMsgsTests:
    def test_create_exisiting_domain(self, driver):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
            ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

        # creates domain, asserts the success message.
        create_domain(driver, domain_name="abc.com")
        wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_domain_created)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_domain_created)))
        back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Back']")))
        back.click()

        # creates new domain with existing domain and asserts the warning message
        create_domain(driver, domain_name="abc.com")
        warning_msg = wait.until(EC.visibility_of_element_located((By.XPATH, wrng_msg_for_invalid_domain_name)))
        assert warning_msg.text == "* Please provide valid Domain."
