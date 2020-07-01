from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *


def assign_scans(driver, individual_eng_xpath):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        ElementNotInteractableException, ElementNotVisibleException, ElementClickInterceptedException])

    eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    ind_eng = wait.until(EC.element_to_be_clickable((By.XPATH, individual_eng_xpath)))
    ind_eng.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    assign_unassign_section = wait.until(EC.element_to_be_clickable((By.XPATH, assign_unassign_xpath)))
    assign_unassign_section.click()

    scans = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@titles='Unassigned Scans,Assigned Scans'][1]//label[@class='el-checkbox el-transfer-panel__item']/span[1]")))
    print("The number of scans: ", len(scans))

    assign_all_scans = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@titles='Unassigned Scans,Assigned Scans'][1]//label[@class='el-checkbox']")))
    assign_all_scans.click()

    assign_scan = wait.until(EC.element_to_be_clickable((By.XPATH, assign_scan_submit)))
    assign_scan.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, assign_success_msg)))
    wait.until(EC.invisibility_of_element((By.XPATH, assign_success_msg)))

    # for i in range(1, len(scans)+1):
    #     print("i: ", i)
    #     select_scans = wait.until(EC.element_to_be_clickable((By.XPATH,
    #                "//div[@titles='Unassigned Scans,Assigned Scans'][1]//label[@class='el-checkbox el-transfer-panel__item']["+str(i)+"]/span[1]")))
    #     select_scans.click()
    #
    #     assign_scan = wait.until(EC.element_to_be_clickable((By.XPATH, assign_scan_submit)))
    #     assign_scan.click()
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    #     wait.until(EC.visibility_of_element_located((By.XPATH, assign_success_msg)))
    #     wait.until(EC.invisibility_of_element((By.XPATH, assign_success_msg)))
