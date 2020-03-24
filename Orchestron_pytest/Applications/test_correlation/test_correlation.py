# import time
# from pytest import mark
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import pytest
# from xpath.Application_module_xpath import *
# from Applications.test_create_applications.test_create_application import *
#
#
# @pytest.mark.run(order=1)
# def test_create_apps(driver):
#     applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
#         EC.element_to_be_clickable((By.XPATH, application_tab)))
#     applicationTab.click()
#
#     create_btn = WebDriverWait(driver, 10, poll_frequency=2).until(
#         EC.presence_of_element_located((By.XPATH, app_create_button)))
#     create_btn.click()
#
#     name = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, app_name)))
#     name.send_keys("App_0")
#
#     url = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, app_url)))
#     url.send_keys("http://demo.com")
#
#     platform_type = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, app_platform_type)))
#     platform_type.send_keys("Python")
#     platform_type.send_keys(Keys.ARROW_DOWN)
#     platform_type.send_keys(Keys.ENTER)
#
#     team = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, app_team)))
#     team.click()
#     # team.send_keys('Testing')
#     # team.send_keys(Keys.ARROW_DOWN)
#     # team.send_keys(Keys.ENTER)
#
#     submit_1 = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, app_submit)))
#     submit_1.click()
#     time.sleep(2)
#
#
# @pytest.mark.run(order=2)
# def test_manual_entry(driver):
#     applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
#         EC.element_to_be_clickable((By.XPATH, application_tab)))
#     applicationTab.click()
#
#     search_tab = WebDriverWait(driver, 10, poll_frequency=2).until(
#         EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
#     search_tab.click()
#     search_tab.send_keys("App_0")
#     time.sleep(2)
#     select_individual_app = WebDriverWait(driver, 10, poll_frequency=2).until(
#         EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'App_0')]")))
#     select_individual_app.click()
#     time.sleep(2)
#
#     action_dp = WebDriverWait(driver, 10, poll_frequency=1).until(
#         EC.element_to_be_clickable((By.XPATH, action_dropdown)))
#     action_dp.click()
#
#     manual_entry_option = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, manual_entry)))
#     manual_entry_option.click()
#
#     scan_name = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, man_scan_name)))
#     scan_name.send_keys("Manual scan")
#
#     vulnerability_name = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, man_vul_name)))
#     vulnerability_name.send_keys("SQL injection")
#
#     cwe = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, man_cwe)))
#     ActionChains(driver).move_to_element(cwe).click(cwe).send_keys("89").send_keys(Keys.ENTER).perform()
#
#     owasp = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, man_owasp)))
#     owasp.send_keys("injection")
#     owasp.send_keys(Keys.ENTER)
#
#     if 'Next' in driver.page_source:
#         print("Next button visible")
#     else:
#         print("Unable to see the 'Next' button")
#
#     next = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))
#     next.click()
#
#     descrption = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, man_desc)))
#     descrption.send_keys("xyz " * 20)
#
#     remediation = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, man_remed)))
#     remediation.send_keys("xyz " * 20)
#
#     previous_btn = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Previous')]")))
#     previous_btn.click()
#
#     next = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))
#     next.click()
#
#     if 'Submit' in driver.page_source:
#         print("submit button visible")
#     else:
#         print("submit button not visible")
#
#     submit = WebDriverWait(driver, 10, poll_frequency=1).until(
#         EC.element_to_be_clickable((By.XPATH, man_submit)))
#     submit.click()
#     time.sleep(3)
#
#
# @pytest.mark.run(order=3)
# @mark.upload_results
# def test_uploadresult(driver):
#     applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
#         EC.element_to_be_clickable((By.XPATH, application_tab)))
#     applicationTab.click()
#
#     search_tab = WebDriverWait(driver, 10, poll_frequency=2).until(
#         EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
#     search_tab.clear()
#     time.sleep(2)
#     search_tab.send_keys("App_0")
#     time.sleep(2)
#     select_individual_app = WebDriverWait(driver, 10, poll_frequency=3).until(
#         EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'App_0')]")))
#     select_individual_app.click()
#
#     action_dp = WebDriverWait(driver, 10, poll_frequency=1).until(
#         EC.element_to_be_clickable((By.XPATH, action_dropdown)))
#     action_dp.click()
#
#     upload_result = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, upload_results)))
#     upload_result.click()
#
#     select_tool = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, tool)))
#     select_tool.click()
#     select_tool.send_keys('zap')
#     select_tool.send_keys(Keys.ENTER)
#
#     tool_name = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, name)))
#     tool_name.send_keys('zap scans')
#
#     upload_file = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, file)))
#     upload_file.send_keys("/home/junaid/Downloads/results_supported_by_orchy/zap.xml")
#
#     submit1 = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
#     submit1.click()
#     time.sleep(0.5)
#     driver.refresh()
#     time.sleep(2)
#
#
# @pytest.mark.run(order=4)
# def test_check_for_correlation(driver):
#     applicationTab = WebDriverWait(driver, 10, poll_frequency=2).until(
#         EC.element_to_be_clickable((By.XPATH, application_tab)))
#     applicationTab.click()
#     time.sleep(2)
#     search_tab = WebDriverWait(driver, 10, poll_frequency=2).until(
#         EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
#     search_tab.send_keys("App_0")
#     time.sleep(2)
#     select_individual_app = WebDriverWait(driver, 10, poll_frequency=2).until(
#         EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'App_0')]")))
#     select_individual_app.click()
#
#     open_vulnerabilities = WebDriverWait(driver, 10, poll_frequency=1).until(
#         EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav nav-tabs']/li[2]")))
#     open_vulnerabilities.click()
#
#     driver.execute_script("window.scrollTo(0, 900)")
#
#     sql1 = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//p[@data-original-title='Sql Injection']")))
#     sql1.click()
#
#     tools = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/section/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div[1]/table/tr[1]")))
#     # print(tools.text)
#     assert tools.text == 'Tool : Manual,ZAP' or tools.text == 'Tool : ZAP,Manual', "correlation isn't happening"
#     # if tools.text == 'Tool : Manual,ZAP' or tools.text == 'Tool : ZAP,Manual':
#     #     print('\ncorrelation is successful')
#     # else:
#     #     print("\ncorrelation isn't successful")
#
#
