from pytest import mark
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.login_xpath import *
from xpath.Application_module_xpath import *
from xpath.Engagement_module_xpath import *
from xpath.settings_module_xpath import *
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
    # driver = webdriver.Firefox(executable_path='/home/junaid/PycharmProjects/HelloWorld/venv/bin/geckodriver_linux64/geckodriver')
    driver.get(url)
    driver.maximize_window()
    email = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
    email.click()
    email.send_keys("chandrashekar@we45.com")
    pw = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    pw.click()
    pw.send_keys("Test@1234")
    login = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    login.click()

    assert driver.current_url == url, "URL isn't matching(Conftest)"
    time.sleep(2)
    return driver


@pytest.fixture(scope="function")
def login(username=None, password=None):
    driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    email = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
    email.clear()
    email.send_keys(username)
    pw = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    pw.clear()
    pw.send_keys(password)
    login = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    login.click()
    time.sleep(2)
    return driver


@pytest.fixture(scope="function")
def create_app(driver, app='DemoApplication'):
    applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()
    create_btn = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located((By.XPATH, app_create_button)))
    create_btn.click()
    name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, app_name)))
    name.send_keys(app)
    url = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, app_url)))
    url.send_keys("http://" + app + ".com")
    platform_type = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, app_platform_type)))
    platform_type.send_keys("Python")
    platform_type.send_keys(Keys.ARROW_DOWN)
    platform_type.send_keys(Keys.ENTER)
    team = WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, app_team)))
    team.click()
    # team.send_keys('Testing')
    # team.send_keys(Keys.ENTER)
    submit_1 = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, app_submit)))
    submit_1.click()
    time.sleep(2)


@pytest.fixture(scope="function")
def create_eng(driver):
    eng_tab = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    create = WebDriverWait(driver, 10, poll_frequency=3).until(EC.element_to_be_clickable((By.XPATH, eng_create_btn)))
    create.click()
    name = WebDriverWait(driver, 10, poll_frequency=2).until(EC.presence_of_element_located((By.XPATH, eng_name)))
    name.send_keys("Demo Engagement")
    desc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, eng_desc)))
    desc.send_keys("Demo Engagement")
    eng_date = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, eng_date_btn)))
    eng_date.click()
    eng_date_popup1 = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][1]//td[@class='curMonth today']")))
    eng_date_popup1.click()
    eng_date_popup2 = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='mx-calendar'][2]//td[@title='28/02/2020']")))
    eng_date_popup2.click()
    bucket_type = WebDriverWait(driver, 10, poll_frequency=2).until(EC.presence_of_element_located((By.XPATH, eng_bucket_type)))
    bucket_type.send_keys("All")
    bucket_type.send_keys(Keys.ARROW_DOWN)
    bucket_type.send_keys(Keys.ENTER)
    app_dropdown = WebDriverWait(driver, 10, poll_frequency=2).until(EC.presence_of_element_located((By.XPATH, eng_app_dropdown)))
    app_dropdown.click()
    app_dropdown.send_keys("SCA")
    app_dropdown.send_keys(Keys.ARROW_DOWN)
    app_dropdown.send_keys(Keys.ENTER)
    submit = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, eng_submit)))
    submit.click()


@pytest.fixture(scope="function")
def create_team(driver):
    settingstab = WebDriverWait(driver,10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, settings_tab)))
    driver.execute_script("arguments[0].click();", settingstab)

    teams = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, team_section)))
    teams.click()
    create = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, create_user_btn)))
    create.click()
    name = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, team_name)))
    name.send_keys('Testing team')
    desc = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, team_desc)))
    desc.send_keys('These is testing team where only testers are assigned to these team')
    submit = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, create_team_submit)))
    submit.click()