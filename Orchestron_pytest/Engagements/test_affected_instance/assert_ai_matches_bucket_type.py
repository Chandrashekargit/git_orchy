from spinner.spinner import *
import time
from xpath.Application_module_xpath import *
from xpath.Engagement_module_xpath import *


def test_assign_scans_and_check_ai(self, driver, engagement_name_xpath, tool_names):
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    # clicks on Engagement section
    stop_till_spinner_is_invisible(driver)
    eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    stop_till_spinner_is_invisible(driver)
    time.sleep(2)
    click_on_individual_eng = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_name_xpath)))
    click_on_individual_eng.click()

    stop_till_spinner_is_invisible(driver)
    assign_unassign_section = wait.until(EC.element_to_be_clickable((By.XPATH, assign_unassign_xpath)))
    assign_unassign_section.click()

    # scans = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@titles='Unassigned Scans,Assigned Scans'][1]//label[@class='el-checkbox el-transfer-panel__item']/span[1]")))
    # # print("The number of scans: ", len(scans))

    stop_till_spinner_is_invisible(driver)
    select_all_scans = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@titles='Unassigned Scans,Assigned Scans'][1]//label[@class='el-checkbox']")))
    select_all_scans.click()
    assign_scan = wait.until(EC.element_to_be_clickable((By.XPATH, assign_scan_submit)))
    assign_scan.click()

    stop_till_spinner_is_invisible(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, assign_success_msg)))
    wait.until(EC.invisibility_of_element((By.XPATH, assign_success_msg)))

    stop_till_spinner_is_invisible(driver)
    move_to_severity = wait.until(EC.element_to_be_clickable((By.XPATH, severity_section)))
    move_to_severity.click()

    for i in [high_severity, medium_severity, low_severity, info_severity]:
        try:
            click_on_sev = wait.until(EC.element_to_be_clickable((By.XPATH, i)))
            click_on_sev.click()
            stop_till_spinner_is_invisible(driver)
            per_page = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
            per_page.click()
            select_All = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
            select_All.click()
            time.sleep(2)
            stop_till_spinner_is_invisible(driver)
            total_num_of_vul = WebDriverWait(driver, 5, poll_frequency=1).until(EC.presence_of_all_elements_located((By.XPATH, "//tr[@class='el-table__row']//td[2]//p")))
        except TimeoutException:
            continue

        for j in range(1, len(total_num_of_vul) + 1):
            try:
                click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='el-table__row']["+str(j)+"]//td[2]//p")))
                click_on_individual_vul.click()
                stop_till_spinner_is_invisible(driver)
                time.sleep(1)
                move_to_ai_section = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
                move_to_ai_section.click()
                time.sleep(2)
                give_total_num_of_ai = WebDriverWait(driver, 5, poll_frequency=1).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='container-fluid' and @style]//div[@class='row']//div[@class='col-sm-10']")))
            except TimeoutException:
                go_back_to_vul_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Open')]")))
                go_back_to_vul_page.click()
                continue

            k = len(give_total_num_of_ai)
            while k >= 1:
                try:
                    stop_till_spinner_is_invisible(driver)
                    click_on_individual_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(k)+"]//header")))
                    click_on_individual_affected_instance.click()
                    time.sleep(1)

                    check_tool_name = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='vul-"+str(k-1)+"']//span[@class='badge badge-info']")))
                    assert check_tool_name.text in tool_names
                    k -= 1
                except:
                    stop_till_spinner_is_invisible(driver)
                    click_on_individual_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(k)+"]//header")))
                    click_on_individual_affected_instance.click()
                    time.sleep(1)

                    check_tool_name = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='vul-"+str(k-1)+"']//span[@class='badge badge-info']")))
                    assert check_tool_name.text in tool_names
                    k -= 1

            go_back_to_vul_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Open')]")))
            go_back_to_vul_page.click()
