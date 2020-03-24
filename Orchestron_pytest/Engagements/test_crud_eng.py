import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *
from xpath.Application_module_xpath import *


@mark.crud_eng
def test_create_eng(driver, create_eng):
    """
    > These function checks the basic CRUD operations of engagement (create, update, delete)
    > Before running these function make sure there are application (app name: SAST, SCA)
    """
    if "//label[contains(text(), 'Demo Engagement')]":
        def test_update_eng():
            time.sleep(1)
            eng_tab = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, engagement_tab)))
            eng_tab.click()

            select_eng = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Demo Engagement')]")))
            select_eng.click()
            time.sleep(1)

            action = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, action_dropdown)))
            action.click()
            select_update = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, eng_update)))
            select_update.click()

            update_name = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@class='inline-form-control-count form-control is-valid']")))
            update_name.clear()
            update_name.send_keys('Updated Demo Engagement')

            update_desc = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//div[@class='col-sm-12']//textarea[@class='form-control is-valid']")))
            update_desc.clear()
            update_desc.send_keys('Updated Demo Engagement')

            update_app = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//div[@class='modal-content']//input[@class='el-input__inner']")))
            update_app.send_keys('SAST')
            update_app.send_keys(Keys.ARROW_DOWN)
            update_app.send_keys(Keys.ENTER)

            update_bucket = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/div[2]/div[1]/div/div/div/div/form/div/div[2]/div[1]/div/div/div[1]/input")))
            update_bucket.send_keys('SAST')
            update_bucket.send_keys(Keys.ARROW_DOWN)
            update_bucket.send_keys(Keys.ENTER)

            update_submit = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, eng_submit)))
            update_submit.click()
            driver.refresh()
        if "//label[contains(text(), 'Updated Demo Engagement')]":
            def test_delete_engagement():
                time.sleep(1)
                eng_tab = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, engagement_tab)))
                eng_tab.click()

                select_eng = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Updated Demo Engagement')]")))
                select_eng.click()
                time.sleep(1)

                action = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, action_dropdown)))
                action.click()
                select_delete = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, eng_delete)))
                select_delete.click()

                eng_del = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, eng_delete)))
                eng_del.click()
                delete = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Delete')]")))
                delete.click()
            test_update_eng()
            test_delete_engagement()
            print("\nBasic Engagement crud operations are successful")

