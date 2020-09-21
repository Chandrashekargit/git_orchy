from pytest import mark
from selenium import webdriver
import pytest
import time
from xpath.login_xpath import *
from xpath.Application_module_xpath import *
from xpath.Engagement_module_xpath import *
from xpath.settings_module_xpath import *
from selenium.webdriver.common.keys import Keys
from spinner.spinner import *


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
    # driver = webdriver.Firefox(executable_path='/home/junaid/PycharmProjects/HelloWorld/venv/bin/geckodriver_linux64/geckodriver')
    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])

    stop_till_spinner_is_invisible(driver)
    email = wait.until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
    email.click()
    email.send_keys("chandrashekar@we45.com")
    pw = wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    pw.click()
    pw.send_keys("Test@1234")
    login = wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    login.click()
    stop_till_spinner_is_invisible(driver)
    stop_till_spinner_is_invisible(driver)
    assert driver.current_url == url+'org/dashboard', "URL isn't matching(Conftest)"
    return driver


# @pytest.fixture(scope="session")
# def driver():
#     driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
#     # driver = webdriver.Firefox(executable_path='/home/junaid/PycharmProjects/HelloWorld/venv/bin/geckodriver_linux64/geckodriver')
#     driver.get(url)
#     driver.maximize_window()
#     wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
#         ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException])
#     stop_till_spinner_is_invisible(driver)
#     # login with Microsoft
#     login_via_ms = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.='Login with Microsoft']")))
#     login_via_ms.click()
#     time.sleep(2)
#     print(driver.window_handles)
#     driver.switch_to.window(driver.window_handles[1])
#     stop_till_spinner_is_invisible(driver)
#
#     email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='loginfmt']")))
#     email.send_keys("chandrashekar@we45.com")
#
#     wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
#     next = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
#     next.click()
#
#     pswd = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='passwd']")))
#     pswd.send_keys("Ceramicwhite@2")
#
#     signin = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
#     signin.click()
#     assert driver.current_url == url+'org/dashboard', "URL isn't matching(Conftest)"
#     return driver

@pytest.fixture(scope="function")
def create_app(driver, app='DemoApplication'):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
    # click on Application section
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()
    # create application by filling all the mandatory fields
    create_btn = wait.until(EC.presence_of_element_located((By.XPATH, app_create_button)))
    create_btn.click()
    name = wait.until(EC.presence_of_element_located((By.XPATH, app_name)))
    name.send_keys(app)
    url = wait.until(EC.presence_of_element_located((By.XPATH, app_url)))
    url.send_keys("http://" + app + ".com")
    platform_type = wait.until(EC.presence_of_element_located((By.XPATH, app_platform_type)))
    platform_type.send_keys("Python")
    platform_type.send_keys(Keys.ARROW_DOWN)
    platform_type.send_keys(Keys.ENTER)
    team = wait.until(EC.presence_of_element_located((By.XPATH, app_team)))
    team.click()
    # team.send_keys('Testing')
    # team.send_keys(Keys.ENTER)
    submit_1 = wait.until(EC.element_to_be_clickable((By.XPATH, app_submit)))
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