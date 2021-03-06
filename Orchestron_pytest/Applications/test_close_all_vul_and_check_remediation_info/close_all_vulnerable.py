import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


def close_all_vulnerable(driver, app_name):
    """
    > This function closes all the vulnerabilities of any given application by entering Justification and Evidence/image.
    :param app_name: Give the xpath of the required application to close all the vul's of that application
    """
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
    select_individual_app.click()

    WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    go_to_open_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    go_to_open_vul_section.click()

    WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    per_page = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    per_page.click()
    select_All = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    select_All.click()
    time.sleep(2)

    number_of_open_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
    print('Number of open vulnerability: ', len(number_of_open_vul))

    i = len(number_of_open_vul)
    while i > 0:
        # print(i)
        WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        go_to_open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        go_to_open_vul.click()

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        per_page_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        per_page_dropdown.click()
        selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        driver.execute_script("arguments[0].click();", selectAll)

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
        click_on_individual_vul.click()

        try:
            # Waiting for Time_intro presence on the screen
            WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH, "//u[text()='Time Intro']")))
        except TimeoutException:
            pass

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        click_close_vul_btn = wait.until(EC.element_to_be_clickable((By.XPATH, close_btn)))
        click_close_vul_btn.click()

        if i % 2 == 0:
            fix_btn = wait.until(EC.element_to_be_clickable((By.XPATH, fix)))
            fix_btn.click()
        else:
            wont_fix_btn = wait.until(EC.element_to_be_clickable((By.XPATH, wont_fix)))
            wont_fix_btn.click()

        justification_field = wait.until(EC.presence_of_element_located((By.XPATH, justification)))
        justification_field.send_keys('vulnerable is fixed')

        logo = wait.until(EC.presence_of_element_located((By.XPATH, evidence)))
        logo.send_keys("/home/junaid/Pictures/we45.png")

        submit = wait.until(EC.element_to_be_clickable((By.XPATH, fix_vul_submit)))
        submit.click()
        i -= 1
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[.='The Vulnerability closed successfully']")))
        assert success_msg.text == "The Vulnerability closed successfully"
