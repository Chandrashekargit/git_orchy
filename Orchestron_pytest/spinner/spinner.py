from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def stop_till_spinner_is_invisible(driver):
    WebDriverWait(driver, 100, poll_frequency=3).until(EC.invisibility_of_element((By.XPATH, "//div[@class='vld-background']")))
