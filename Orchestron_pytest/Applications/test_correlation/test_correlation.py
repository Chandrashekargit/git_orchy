# import time
# from pytest import mark
# from selenium.common.exceptions import *
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import pytest
# from xpath.Application_module_xpath import *
# # from Applications.test_create_applications.test_create_application import *
# from Applications.test_manual_entry_scans.manual_entry import manual_entry_vul
# from Applications.test_upload_scans.test_upload_results import upload_res
#
#
# @pytest.mark.run(order=1)
# def test_manual_entry(driver, create_app):
#     manual_entry_vul(driver, search_key="DemoApplication",
#                      individual_app_xpath="//label[contains(text(),'DemoApplication')]",
#                      scan_name="Manual scan", vul_name="SQL injection", cwe_num=89, owasp_status="injection")
#
#
# @pytest.mark.run(order=2)
# def test_uploadresult(driver):
#     upload_res(driver, application="//label[contains(text(), 'DemoApplication')]", tool_name="zap",
#                file_loc="/home/junaid/Downloads/results_supported_by_orchy/zap.xml")
#     time.sleep(8)
#
#
# @pytest.mark.run(order=3)
# def test_check_for_correlation(driver):
#     wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
#         NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
#
#     applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
#     applicationTab.click()
#
#     search_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
#     search_tab.send_keys("DemoApplication")
#
#     select_individual_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'DemoApplication')]")))
#     select_individual_app.click()
#
#     open_vulnerabilities = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
#     open_vulnerabilities.click()
#
#     driver.execute_script("window.scrollTo(0, 900)")
#
#     sql1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[@title='Sql Injection']")))
#     sql1.click()
#
#     tools = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/section/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div[1]/table/tr[1]")))
#     # print(tools.text)
#     assert tools.text == 'Tool : Manual,ZAP' or tools.text == 'Tool : ZAP,Manual', "correlation isn't happening"
#
