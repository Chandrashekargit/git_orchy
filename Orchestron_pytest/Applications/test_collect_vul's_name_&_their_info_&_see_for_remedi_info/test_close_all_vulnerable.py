import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


@mark.close_all_vulnerabilities
def test_close_all_vulnerable(driver):
    # wait = WebDriverWait(driver, 10, poll_frequency=3)
    applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    app = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'SAST')]")))
    app.click()

    open_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
        EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    # for j in range(1, 41):
    #     time.sleep(1)
    #     perpage = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH,
    #                                           "//input[@placeholder='Per Page']")))
    #     perpage.click()
    #     time.sleep(1)
    #     selectAll = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable(
    #         (By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[6]//span[text()='All']")))
    #     selectAll.click()
    #     driver.execute_script("window.scrollTo(0, 900);")
    #     time.sleep(1)
    #
    #     click_individual_vulnerable = WebDriverWait(driver, 10, poll_frequency=3).until(EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p")))
    #     click_individual_vulnerable.click()
    #     time.sleep(1.5)
    #     close = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, close_btn)))
    #     close.click()
    #
    #     fix_btn = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, fix)))
    #     fix_btn.click()
    #
    #     justi = WebDriverWait(driver, 10, poll_frequency=2).until(EC.presence_of_element_located((By.XPATH, justification)))
    #     justi.send_keys('vulnerable is fixed')
    #
    #     submit = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, fix_submit)))
    #     submit.click()
    #     time.sleep(1.5)
    #
    #     go_to_opened_vul = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable(
    #         (By.XPATH, "//a[text()='Opened']")))
    #     go_to_opened_vul.click()

    # time.sleep(2)
    # data1 = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located(
    #     (By.XPATH, "//div[@class='tab-pane card-body show fade active']//div[@class='row']"))).text
    # print(data1)
    # print("*" * 50)
    #
    # go_to_opened_vul = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located(
    #     (By.XPATH, "//label[contains(text(), 'Opened')]")))
    # go_to_opened_vul.click()

    j = 1
    while j <= 1:
        time.sleep(1)
        # perpage = WebDriverWait(driver, 10, poll_frequency=2).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Per Page']")))
        # perpage.click()
        # time.sleep(1)
        # selectAll = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable(
        #     (By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[6]//span[text()='All']")))
        # selectAll.click()
        driver.execute_script("window.scrollTo(0, 900);")
        time.sleep(1)

        click_individual_vulnerable = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p")))
        click_individual_vulnerable.click()
        time.sleep(1.5)
        close = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, close_btn)))
        close.click()

        fix_btn = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, fix)))
        fix_btn.click()

        justi = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located((By.XPATH, justification)))
        justi.send_keys('vulnerable is fixed, Hence closing the vulnerable')

        submit = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, fix_submit)))
        submit.click()
        time.sleep(1.5)

        go_to_opened_vul = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Opened']")))
        go_to_opened_vul.click()

