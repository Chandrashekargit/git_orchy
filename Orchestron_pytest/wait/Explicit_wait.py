from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWait:

    def __init__(self, value):
        # self.driver = driver
        # self.by = by
        self.value = value

    # property makes the function as variable. so we no need to call the function instead we could just use the func
    # name like variable where needed. #Brandon blair.
    # @property
    def presence1(self, driver):
        element = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions = [
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException]).until(EC.presence_of_element_located((By.XPATH, self.value)))
        return element

    # @property
    def click(self, driver):
        element = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException]).until(EC.element_to_be_clickable((By.XPATH, self.value)))
        return element.click()

# Haven't used this file anywhere yet
