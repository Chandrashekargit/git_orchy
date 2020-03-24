import time
from pytest import mark
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *


@mark.assign_scans
class AssignScansTests:
    def test_assign_scans(self, driver, create_eng):
        """
        > These function checks if 'Assign and unassign' of scans happens as intended.
        """
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
        eng_tab.click()

        ind_eng = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Demo Engagement')]")))
        ind_eng.click()

        assign_scans = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Assign / Unassign Scans']")))
        assign_scans.click()

        scan1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='npm']")))
        scan1.click()
        scan2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Retire']")))
        scan2.click()
        scan3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='whitesource']")))
        scan3.click()
        scan4 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='snyk']")))
        scan4.click()
        scan5 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='OWASP']")))
        scan5.click()
        assign_scan = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='el-icon-arrow-right']")))
        assign_scan.click()
        time.sleep(3)


    @mark.unassign_scans
    def test_unassignscans(self, driver):
        driver.refresh()
        eng_tab = driver.find_element_by_xpath("//p[contains(text(),'Engagements')]")
        eng_tab.click()

        ind_eng = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Engagement111')]")))
        ind_eng.click()

        assign_unassign_scans = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Assign / Unassign Scans']")))
        assign_unassign_scans.click()

        all_scans_unassign = driver.find_element_by_xpath("//span[contains(text(),'Assigned Scans')]")
        all_scans_unassign.click()

        unassign_scans = driver.find_element_by_xpath("//i[@class='el-icon-arrow-left']")
        unassign_scans.click()
        time.sleep(3)

