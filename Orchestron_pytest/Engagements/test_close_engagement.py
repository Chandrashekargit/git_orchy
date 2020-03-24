from selenium import webdriver
import time
import pytest
from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@mark.close_eng
def test_close_engagement(driver):
    eng_tab = driver.find_element_by_xpath("//p[contains(text(),'Engagements')]")
    eng_tab.click()
    time.sleep(2)
    ind_eng = driver.find_element_by_xpath("//p[contains(text(),'Engagement111')]")
    ind_eng.click()
    time.sleep(2)
    close_eng_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Close Engagement']"))
    )
    # close_eng_btn = driver.find_element_by_xpath("//button[text() = 'Close Engagement']")
    close_eng_btn.click()
    # element.submit()
    time.sleep(1)
    close_eng = driver.find_element_by_xpath("//div[@class='modal-content']//button[contains(text(),'Close')]")
    close_eng.click()
    time.sleep(2)
    back_to_eng_page = driver.find_element_by_xpath("//a[@href='/engagements/']")
    back_to_eng_page.click()
    time.sleep(2)
    assert 'Closed On' in driver.page_source, "unable to find the closed engagement"
