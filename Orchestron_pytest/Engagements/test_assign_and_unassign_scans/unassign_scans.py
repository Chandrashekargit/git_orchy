from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *


def unassign_scans(driver, individual_eng_xpath):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        ElementNotInteractableException, ElementNotVisibleException, ElementClickInterceptedException])

    eng_tab = driver.find_element_by_xpath(engagement_tab)
    eng_tab.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    ind_eng = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, individual_eng_xpath)))
    ind_eng.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    assign_unassign_section = wait.until(EC.element_to_be_clickable((By.XPATH, assign_unassign_xpath)))
    assign_unassign_section.click()

    scans = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@titles='Unassigned Scans,Assigned Scans'][2]//label[@class='el-checkbox el-transfer-panel__item']/span[1]")))
    print("Number of unassigned scans: ", scans)

    unassign_all_scans = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@titles='Unassigned Scans,Assigned Scans'][2]//label[@class='el-checkbox']")))
    unassign_all_scans.click()

    unassign_scan = wait.until(EC.element_to_be_clickable((By.XPATH, unassign_scan_submit)))
    unassign_scan.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, unassign_success_msg)))
    wait.until(EC.invisibility_of_element((By.XPATH, assign_success_msg)))


    # for i in range(1, len(scans)+1):
    #     select_scans = wait.until(EC.element_to_be_clickable((By.XPATH,
    #        "//div[@titles='Unassigned Scans,Assigned Scans'][2]//label[@class='el-checkbox el-transfer-panel__item']["+str(i)+"]/span[1]")))
    #     select_scans.click()
    #
    #     unassign_scan = wait.until(EC.element_to_be_clickable((By.XPATH, unassign_scan_submit)))
    #     unassign_scan.click()
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    #     wait.until(EC.visibility_of_element_located((By.XPATH, unassign_success_msg)))
    #     wait.until(EC.invisibility_of_element((By.XPATH, unassign_success_msg)))
