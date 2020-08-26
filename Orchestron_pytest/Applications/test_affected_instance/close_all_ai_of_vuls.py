import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from xpath.Application_module_xpath import *


def close_all_ai(driver, app_name):
    """
    This function closes all the Affected instances of all Vulnerabilities
    under any required application and asserts the success messages,
    asserts number of open vulnerabilities == number of closed vulnerabilities.
    :param app_name: Xpath of the Application.
    """
    wait = WebDriverWait(driver, 30, poll_frequency=2, ignored_exceptions=[
        ElementNotInteractableException, ElementClickInterceptedException, ElementNotVisibleException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
    select_individual_app.click()
    time.sleep(2)

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
    go_to_open_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    go_to_open_vul_section.click()

    WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    per_page = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    per_page.click()
    select_All = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    select_All.click()
    time.sleep(2)

    number_of_open_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
    print('Number of open vulnerabilities: ', len(number_of_open_vul))

    i = len(number_of_open_vul)
    while i >= 1:
        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
        go_to_open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        go_to_open_vul.click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        per_page_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        per_page_dropdown.click()
        selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        driver.execute_script("arguments[0].click();", selectAll)

        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        time.sleep(1)
        click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
        click_on_individual_vul.click()

        WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        time.sleep(1)
        move_to_ai_section = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
        move_to_ai_section.click()
        time.sleep(2)  # This time.sleep helps to calculate the num of affected instance under individual vul

        give_total_num_of_ai = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='container-fluid' and @style]//div[@class='row']//div[@class='col-sm-10']")))
        # print("Number of Affected instances: ", len(give_total_num_of_ai))

        j = len(give_total_num_of_ai)
        while j >= 1:
            if j == 1:
                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_individual_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH,
                   "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//header")))
                click_on_individual_affected_instance.click()
                time.sleep(1)

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_ai_action_dp = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='row'][" + str(j) + "]//div[@class='col-sm-2']//div[@id='right']")))
                click_on_ai_action_dp.click()

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                close_evd = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[.='Close evidence']")))
                close_evd.click()

                click_submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
                click_submit.click()

                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[.='Vulnerability successfully closed!']")))
                assert success_msg.text == "Vulnerability successfully closed!"
                break
            else:
                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_individual_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH,
                   "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//header")))
                click_on_individual_affected_instance.click()
                time.sleep(1)

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_on_ai_action_dp = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='row']["+str(j)+"]//div[@class='col-sm-2']//div[@id='right']")))
                click_on_ai_action_dp.click()

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                close_evd = wait.until(EC.presence_of_element_located((By.XPATH, close_evdience)))
                close_evd.click()

                # upload_img = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='custom-file-input']")))
                # upload_img.send_keys("/home/junaid/Pictures/we45.png")

                # enter_evd_justification = wait.until(EC.presence_of_element_located((By.XPATH, evd_justification)))
                # enter_evd_justification.send_keys("Closing the Evidence")

                WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                click_submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
                click_submit.click()

                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
                success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[.='Evidence successfully closed!']")))
                assert success_msg.text == "Evidence successfully closed!"
                wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            j -= 1
        wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
        go_to_open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
        go_to_open_vul.click()
        i -= 1

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
    go_to_open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    go_to_open_vul.click()

    check_if_any_vul_is_present = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[.='No Data']")))
    assert check_if_any_vul_is_present.text == "No Data"

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-icon' or @class='loading-background']")))
    go_to_closed_vul_section = wait.until(EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
    go_to_closed_vul_section.click()

    WebDriverWait(driver, 20, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    per_page = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    per_page.click()
    select_All = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    select_All.click()
    time.sleep(2)

    number_of_closed_vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='cell']/p")))
    print("Number of closed vulnerabilities: ", len(number_of_closed_vul))

    assert len(number_of_open_vul) == len(number_of_closed_vul)
