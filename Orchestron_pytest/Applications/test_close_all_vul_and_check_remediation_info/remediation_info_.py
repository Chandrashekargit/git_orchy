import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


def checks_visibility_of_remediation_info_of_closed_vuls(driver, app_name):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])
    wait1 = WebDriverWait(driver, 20, ignored_exceptions=[
        ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # Search the required Application
    # search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    # search_tab.click()
    # search_tab.send_keys("App_0")

    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
    select_individual_app.click()

    wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    go_to_closed_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
    go_to_closed_vul_section.click()

    wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    perpage = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    perpage.click()
    selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    selectAll.click()
    time.sleep(2)  # Sleep time is required to get the length of the closed vul's.

    number_of_closed_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='cell']/p")))
    print(len(number_of_closed_vul))

    i = len(number_of_closed_vul)
    while i > 0:
        print(i)

        wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        perpage = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage.click()
        selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        driver.execute_script("arguments[0].click();", selectAll)

        wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[" + str(i) + "]/td[2]//div[@class='cell']/p")))
        click_on_individual_vul.click()

        wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        move_to_remediation_info_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Remediation Info']")))
        driver.execute_script("arguments[0].click();", move_to_remediation_info_section)

        wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        remed_info = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@style='white-space: normal;']//div[@class='card-body']")))
        time.sleep(1)
        assert "vulnerable is fixed" == remed_info.text

        image = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@style='height: 120px; width: 120px; cursor: pointer;']")))
        image.click()

        close_image = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']")))
        close_image.click()

        wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Closed')]")))
        go_to_closed_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Closed')]")))
        go_to_closed_vul_section.click()
        i -= 1


    # ================= TEST CASE ENDS HERE ====================

    # # If we want to reopen the vulnerability please use below code
    # # time.sleep(1)
    # click_on_reopen_vul = wait.until(EC.element_to_be_clickable((By.XPATH, reopen_btn)))
    # click_on_reopen_vul.click()
    #
    # justification_popup = wait.until(EC.presence_of_element_located((By.XPATH, justification)))
    # justification_popup.send_keys('vulnerable is reopened')
    #
    # submit = wait.until(EC.element_to_be_clickable((By.XPATH, reopen_submit)))
    # submit.click()
    # i -= 1
    #
    # success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='The vulnerability has been Re-opened successfully!']")))
    # if success_msg.is_displayed():
    #     continue