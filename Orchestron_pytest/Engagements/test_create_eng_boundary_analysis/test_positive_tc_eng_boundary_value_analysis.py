import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *
from xpath.Application_module_xpath import *
import conftest


@mark.engagement_boundary_value_analysis_positive
@mark.parametrize('engagement_name, eng_description', [
    ('!@#$%^&*() 1234567890! createapp with alphanum,spl', "@1q,2/3==0" * 20),
    ('1234567890', ' '),
    ('D', 'http://D.com')
])
def test_create_eng(driver, engagement_name, eng_description):
    eng_tab = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, Engagement_tab)))
    eng_tab.click()

    create_btn = WebDriverWait(driver, 10, poll_frequency=3).until(
        EC.element_to_be_clickable((By.XPATH, eng_create_btn)))
    create_btn.click()

    name = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.presence_of_element_located((By.XPATH, eng_name)))
    name.send_keys(engagement_name)

    desc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, eng_desc)))
    desc.send_keys(eng_description)

    eng_date = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, eng_date_btn)))
    eng_date.click()
    eng_date_popup1 = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][1]//td[@class='curMonth today']")))
    eng_date_popup1.click()
    eng_date_popup2 = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][2]//td[@title='28/02/2020']")))
    eng_date_popup2.click()

    bucket_type = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.presence_of_element_located((By.XPATH, eng_bucket_type)))
    bucket_type.send_keys("All")
    bucket_type.send_keys(Keys.ARROW_DOWN)
    bucket_type.send_keys(Keys.ENTER)

    app_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, eng_app_dropdown)))
    app_dropdown.send_keys("SCA")
    app_dropdown.send_keys(Keys.ARROW_DOWN)
    app_dropdown.send_keys(Keys.ENTER)

    submit = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, eng_submit)))
    driver.execute_script("arguments[0].click();", submit)
    driver.refresh()
