import time
from pytest import mark
import pytest

'''go back to: list of engagement page and view report of individual engagement'''

'''
    These function helps us to view the reports of the individual engagement.
    It opens the report of the individual engagement and scrolls down and navigates through the pages.
'''

@mark.view_report
def test_view_report(driver):
    eng_tab = driver.find_element_by_xpath("//p[contains(text(),'Engagements')]")
    eng_tab.click()
    time.sleep(2)
    eng_action = driver.find_element_by_xpath("//div[contains(text(),'Actions')]")
    eng_action.click()
    time.sleep(1)
    # eng_view_report = driver.find_element_by_xpath("//ul[@x-placement='top-end']//li[3]")
    eng_view_report = driver.find_element_by_xpath("/html[1]/body[1]/ul[1]/li[3]/a[1]/li[1]")
    eng_view_report.click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 900);")

    vulnerabilities1 = [
        "Deserialization Of Untrusted Data",
        "Improper Neutralization Of Special Elements Used In A Command ('Command Injection')",
        "Improper Input Validation",
        "Cross-Site Scripting",
        "node-serialize_code-execution-through-iife"]
    for vulnerability1 in vulnerabilities1:
        assert vulnerability1 in driver.page_source
    eng_report_move_next_page = driver.find_element_by_xpath("//a[@aria-label='Goto next page']")
    eng_report_move_next_page.click()
    time.sleep(5)