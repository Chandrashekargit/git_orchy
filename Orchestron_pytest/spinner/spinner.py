from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def stop_till_spinner_is_invisible(driver):
    WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='loading-background' or @class='loading-icon']")))
