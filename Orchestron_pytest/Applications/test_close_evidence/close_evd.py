import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


def close_evd(driver, app_name=None):
    """
    * This function lets us close all the affected evidences.
    :param driver: launch the browser and login.
    :param app_name: give the xpath of the application.
    """
    wait = WebDriverWait(driver, 20, poll_frequency=3)
    wait1 = WebDriverWait(driver, 10)

    # Click on Application section
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # select the required application
    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
    select_individual_app.click()

    # Clicks on Open vulnerability of individual application
    wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    # Clicks Per-page drop-down and selects 'All'.
    wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    time.sleep(1)
    perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    perpage_dp.click()
    sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    sel_all_option.click()
    time.sleep(2)

    try:
        # checks if vulnerabilities are present, if not, it prints out the msg.
        # else, it goes to affected instance section.
        WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print("\nNo vulnerabilities are present for this application")
    except TimeoutException:
        vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print('\nTotal number of vul: ', len(vul))

        for i in range(1, len(vul) + 1):
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
            open_vul.click()

            # clicks on individual vul
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
            print('vulnerability name: ', click_on_individual_vul.text)
            click_on_individual_vul.click()

            # wait till affected instance section is visible
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, affected_instance)))

            # moves to affected instance Section
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            move_to_ai = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
            move_to_ai.click()
            time.sleep(2)

            # try:
            # Gives the count of total number of affected instances under individual vulnerability.
            wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            affected_inst = wait1.until(EC.presence_of_all_elements_located((By.XPATH,
                "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']//div[contains(text(),'Actions')]")))
            print('Total number of affected_instance: ', len(affected_inst))

            for j in range(1, len(affected_inst) + 1):
                click_on_individual_action_dp = wait1.until(EC.element_to_be_clickable((By.XPATH,
                    "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row'][" +str(j)+"]//div[contains(text(),'Actions')]")))
                click_on_individual_action_dp.click()

                select_close_evd = wait1.until(EC.presence_of_element_located((By.XPATH, close_evdience)))
                select_close_evd.click()
                time.sleep(1)
                justi = wait1.until(EC.presence_of_element_located((By.XPATH, justification)))
                justi.send_keys("qwerty")
                time.sleep(1)
                submit = wait1.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
                submit.click()
                wait1.until(EC.invisibility_of_element((By.XPATH, app_submit)))
                wait1.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))

                if j == len(affected_inst):
                    break
            # except TimeoutException:
            #     break
            # finally:
            #     wait1.until(EC.invisibility_of_element((By.XPATH,
            #                                             "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']//div[contains(text(),'Actions')]")))
            #     print("No affected instances present under this vulnerability")
