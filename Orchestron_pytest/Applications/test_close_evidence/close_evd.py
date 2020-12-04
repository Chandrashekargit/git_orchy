import time
from xpath.Application_module_xpath import *
from spinner.spinner import *


def close_evd(driver, app_name=None):
    """
    * This function lets us close all the affected evidences.
    :param driver: launch the browser and login.
    :param app_name: give the xpath of the application.
    """
    wait = WebDriverWait(driver, 20, poll_frequency=3)
    wait1 = WebDriverWait(driver, 10)

    # Click on Application section
    stop_till_spinner_is_invisible(driver)
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # select the required application
    stop_till_spinner_is_invisible(driver)
    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
    select_individual_app.click()

    # Clicks on Open vulnerability of individual application
    stop_till_spinner_is_invisible(driver)
    open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    # Clicks Per-page drop-down and selects 'All'.
    stop_till_spinner_is_invisible(driver)
    time.sleep(1)
    perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    perpage_dp.click()
    sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    sel_all_option.click()
    time.sleep(2)

    try:
        vuls = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print('\nTotal number of vul: ', len(vuls))

        for i in range(1, len(vuls) + 1):
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)
            open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
            open_vul.click()

            # clicks on individual vul
            stop_till_spinner_is_invisible(driver)
            click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
            # print('vulnerability name: ', click_on_individual_vul.text)
            click_on_individual_vul.click()

            # wait till affected instance section is visible
            stop_till_spinner_is_invisible(driver)
            wait.until(EC.visibility_of_element_located((By.XPATH, affected_instance)))

            # wait till Vulnerability info section is visible
            stop_till_spinner_is_invisible(driver)
            wait.until(EC.visibility_of_element_located((By.XPATH, vul_info)))

            # moves to affected instance Section
            stop_till_spinner_is_invisible(driver)
            time.sleep(2)
            move_to_ai = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
            move_to_ai.click()
            time.sleep(2)

            stop_till_spinner_is_invisible(driver)
            affected_inst = wait1.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']//div[contains(text(),'Actions')]")))
            print('Total number of affected_instance: ', len(affected_inst))

            for j in range(1, len(affected_inst) + 1):
                stop_till_spinner_is_invisible(driver)
                click_on_individual_action_dp = wait1.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//div[contains(text(),'Actions')]")))
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
                stop_till_spinner_is_invisible(driver)

                # if j == len(affected_inst):
                #     break

    except TimeoutException:
        # checks if vulnerabilities are present, if not, it prints out the msg.
        # else, it goes to affected instance section.
        WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print("\nNo vulnerabilities are present for this application")
