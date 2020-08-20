from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


def create_apps(driver, application_name=None, url=None):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    create_btn = wait.until(EC.presence_of_element_located((By.XPATH, app_create_button)))
    create_btn.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, app_name)))
    name = wait.until(EC.presence_of_element_located((By.XPATH, app_name)))
    name.send_keys(application_name)

    url_field = wait.until(EC.presence_of_element_located((By.XPATH, app_url)))
    url_field.send_keys(url)

    platform_type = wait.until(EC.presence_of_element_located((By.XPATH, app_platform_type)))
    platform_type.send_keys("Python")
    platform_type.send_keys(Keys.ARROW_DOWN)
    platform_type.send_keys(Keys.ENTER)

    team = wait.until(EC.presence_of_element_located((By.XPATH, app_team)))
    team.click()
    # team.send_keys('Testing')
    # team.send_keys(Keys.ENTER)

    try:
        submit_1 = WebDriverWait(driver, 5, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, app_submit)))
        submit_1.click()
    except TimeoutException:
        print("Submit button not visible")

    # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    # success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_app_created)))
    # assert success_msg.text == "Application has been created successfully!"
    # wait.until(EC.invisibility_of_element((By.XPATH, success_msg_for_app_created)))
