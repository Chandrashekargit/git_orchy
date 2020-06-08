import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark
from xpath.Application_module_xpath import *

# Note: we have redirection error in orchy, when we select the ALL option from perpage dropdown and click on some vul
#       and get back, "ALL" option is replaced with 10. This script works for 1st 10 vul's. if the redirection is fixed
#       it works like charm for N number of vul's. [same issue with pagination]


@mark.check_for_detailed_evd
def test_if_evidences_have_detailed_evd(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=2)

    # Click on Application section
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # Search the required Application
    # search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    # search_tab.click()
    # search_tab.send_keys("Enter the app name")
    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Nexus API (json)')]")))
    select_individual_app.click()

    # Clicks on Open vulnerability of individual application
    open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    # Clicks Per-page drop-down and selects 'All'.
    perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Per Page']")))
    perpage_dp.click()
    sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    sel_all_option.click()
    time.sleep(2)

    # gives the total count of vulnerabilities present under open vulnerability for individual application
    vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
    print('\nTotal number of vul: ', len(vul))

    for i in range(1, len(vul)+1):
        # Clicks Per-page drop-down and selects 'All'
        perpage = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Per Page']")))
        perpage.click()
        time.sleep(1)
        selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        selectAll.click()

        # clicks on individual vul
        click_on_vul = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
        print('vulnerability name: ', click_on_vul.text)
        click_on_vul.click()
        time.sleep(2)

        # moves to affected instance Section
        move_to_ai = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Affected Instances']")))
        move_to_ai.click()

        # Gives the count of total number of affected instances under individual vulnerability.
        affected_instance = wait.until(EC.presence_of_all_elements_located((By.XPATH,
            "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']//header")))
        print('Total number of ai: ', len(affected_instance))

        for j in range(1, len(affected_instance)+1):
            click_on_individual_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH,
               "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//header")))
            # time.sleep(1)
            click_on_individual_affected_instance.click()

            check_the_value_of_affected_instance = wait.until(EC.presence_of_element_located((By.XPATH,
                "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//div[@class='collapse show']//div[@class='list-group-item']")))
            # print(check_the_value_of_affected_instance)

            if "Detailed Evidence" in check_the_value_of_affected_instance.text:
                print('Evidence: ', click_on_individual_affected_instance.text)

        go_back_to_open_vul = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Opened')]")))
        go_back_to_open_vul.click()
        print('*' * 50)
        time.sleep(1)
