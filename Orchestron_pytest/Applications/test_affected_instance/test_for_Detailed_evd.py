import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark
from xpath.Application_module_xpath import *


@mark.check_for_detailed_evd
def test_if_evidences_have_detailed_evd(driver, app_name="//label[contains(text(),'DAST')]"):
    wait = WebDriverWait(driver, 10, poll_frequency=2)
    wait1 = WebDriverWait(driver, 10)

    # Click on Application section
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # Search the required Application
    # search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    # search_tab.click()
    # search_tab.send_keys("Enter the app name")
    select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, app_name)))
    select_individual_app.click()

    # Clicks on Open vulnerability of individual application
    open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    # Clicks Per-page drop-down and selects 'All'.
    perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    perpage_dp.click()
    sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    sel_all_option.click()
    time.sleep(2)

    # gives the total count of vulnerabilities present under open vulnerability for individual application
    vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
    print('\nTotal number of vul: ', len(vul))

    for i in range(1, len(vul)+1):
        # Clicks Per-page drop-down and selects 'All'
        perpage = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
        perpage.click()
        selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
        driver.execute_script("arguments[0].click();", selectAll)

        # clicks on individual vul
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        click_on_individual_vul = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
        print('vulnerability name: ', click_on_individual_vul.text)
        click_on_individual_vul.click()

        # moves to affected instance Section
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        move_to_ai = wait.until(EC.presence_of_element_located((By.XPATH, affected_instance)))
        move_to_ai.click()

        # Gives the count of total number of affected instances under individual vulnerability.
        affected_inst = wait.until(EC.presence_of_all_elements_located((By.XPATH,
            "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']//header")))
        print('Total number of affected_instance: ', len(affected_inst))

        for j in range(1, len(affected_inst)+1):
            click_on_individual_affected_instance = wait1.until(EC.presence_of_element_located((By.XPATH,
               "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//header")))
            # time.sleep(1)
            click_on_individual_affected_instance.click()

            check_the_value_of_affected_instance = wait1.until(EC.presence_of_element_located((By.XPATH,
                "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//div[@class='collapse show']//div[@class='list-group-item']")))
            # print(check_the_value_of_affected_instance)

            if "Detailed Evidence" in check_the_value_of_affected_instance.text:
                print('Evidence: ', click_on_individual_affected_instance.text)

        go_back_to_open_vul = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Opened')]")))
        go_back_to_open_vul.click()
        print('*' * 50)
        time.sleep(1)


# import time
# import os
# from selenium.common.exceptions import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# # Initialise the Browser
# driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
# driver.get("https://demo.orchestron.dev/")
# driver.maximize_window()
# time.sleep(2)
# wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[ElementClickInterceptedException,
#                                                                        ElementNotVisibleException,
#                                                                        ElementClickInterceptedException])
#
# # Credentials to Login
# email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email or Username']")))
# email.send_keys('chandrashekar@we45.com')
# pw = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
# pw.send_keys('Test@1234')
# login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
# login.click()
#
# wait = WebDriverWait(driver, 10, poll_frequency=2)
# wait1 = WebDriverWait(driver, 10)
#
# # Click on Application section
# applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Applications')]")))
# applicationTab.click()
#
# # Search the required Application
# # search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
# # search_tab.click()
# # search_tab.send_keys("Enter the app name")
# select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'burp pro JSON')]")))
# select_individual_app.click()
#
# # Clicks on Open vulnerability of individual application
# open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Opened')]")))
# open_vul.click()
#
# # Clicks Per-page drop-down and selects 'All'.
# # time.sleep(1)
# # perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Per Page']")))
# # perpage_dp.click()
# # sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[6]//span[text()='All']")))
# # sel_all_option.click()
# time.sleep(2)
#
# # gives the total count of vulnerabilities present under open vulnerability for individual application
# vul = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
# print('\nTotal number of vul: ', len(vul))
# # vul_len = len(vul)
# with open("demo.txt1", "w") as f:
#     for i in range(1, len(vul)+1):
#         # Clicks Per-page drop-down and selects 'All'
#         # time.sleep(1)
#         # perpage = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Per Page']")))
#         # perpage.click()
#         # time.sleep(1)
#         # selectAll = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[6]//span[text()='All']")))
#         # selectAll.click()
#
#         # clicks on individual vul
#         click_on_vul = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(i)+"]/td[2]//div[@class='col']/p")))
#         vul_name = ("Common name: "+click_on_vul.text)
#         f.writelines(str(vul_name))
#         time.sleep(1)
#         click_on_vul.click()
#         time.sleep(2)
#
#         click_on_tool_name = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tabs']//div[@class='col-sm-12']//div[2]/button")))
#         click_on_tool_name.click()
#
#         grab_the_tool_given_vul_name = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tabs']//div[@class='col-sm-12']//div[2]//div[@class='el-card__body']/p")))
#         tool_given_vul_name = ("tool_given_"+grab_the_tool_given_vul_name.text)
#         f.writelines('\n'+str(tool_given_vul_name))
#
#         # moves to affected instance Section
#         move_to_ai = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Affected Instances']")))
#         move_to_ai.click()
#
#         # Gives the count of total number of affected instances under individual vulnerability.
#         affected_instance = wait.until(EC.presence_of_all_elements_located((By.XPATH,
#             "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']//header")))
#         # ai_count = ("Total number of affected_instance: "+str(len(affected_instance)))
#         # f.writelines('\n'+str(ai_count))
#
#         for j in range(1, len(affected_instance)+1):
#             click_on_individual_affected_instance = wait1.until(EC.presence_of_element_located((By.XPATH,
#                "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//header")))
#             # time.sleep(1)
#             click_on_individual_affected_instance.click()
#
#             check_the_value_of_affected_instance = wait1.until(EC.presence_of_element_located((By.XPATH,
#                 "//div[@class='tab-content']//div[@class='tab-pane active card-body']//div[@class='container-fluid']//div[@class='row']["+str(j)+"]//div[@class='collapse show']//div[@class='list-group-item']")))
#             # print(check_the_value_of_affected_instance)
#
#             if "Detailed Evidence" in check_the_value_of_affected_instance.text:
#                 Evd = ("Evidence: "+click_on_individual_affected_instance.text)
#
#                 f.writelines('\n'+str(Evd))
#
#         go_back_to_open_vul = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Opened')]")))
#         go_back_to_open_vul.click()
#         print()
#         f.writelines('\n> ')
#         f.writelines('\n')
#         time.sleep(1)
# driver.quit()
#
