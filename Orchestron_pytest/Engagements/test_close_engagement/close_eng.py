from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *


def close_eng(driver, engagement_name_xpath):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    # clicks on engagement tab
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    # clicks on individual engagement
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    click_on_individual_eng = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_name_xpath)))
    click_on_individual_eng.click()

    # awaits for action dropdown btn to be visible on DOM and clicks on it
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, action_dropdown)))
    action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action.click()

    # selects the close_engagement option from action dropdown
    select_close_eng = wait.until(EC.element_to_be_clickable((By.XPATH, eng_close)))
    select_close_eng.click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    click_close = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_close_eng)))
    click_close.click()

    # awaits for success msg to be visible
    success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, close_success_msg)))
    assert success_msg.text == "Engagement has been closed Successfully!"

    # awaits for success msg to be invisible
    wait.until(EC.invisibility_of_element((By.XPATH, close_success_msg)))
