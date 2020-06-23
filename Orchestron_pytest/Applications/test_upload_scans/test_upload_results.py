from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *


def upload_res(driver, application=None, tool_name=None, file_loc=None):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # select the required app
    app = wait.until(EC.element_to_be_clickable((By.XPATH, application)))
    app.click()

    # click on action drop down
    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action.click()

    # select 'upload results' option
    upload_result = wait.until(EC.element_to_be_clickable((By.XPATH, upload_results)))
    upload_result.click()

    # select required tool from tool dropdown
    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    selectTool = wait.until(EC.element_to_be_clickable((By.XPATH, tool)))
    selectTool.click()
    selectTool.send_keys(tool_name)
    selectTool.send_keys(Keys.ARROW_DOWN)
    selectTool.send_keys(Keys.ENTER)

    # enter the scan name
    scan_name = wait.until(EC.presence_of_element_located((By.XPATH, name)))
    scan_name.send_keys(tool_name)

    # upload the required file (xml or JSON)
    uploadFile = wait.until(EC.presence_of_element_located((By.XPATH, file)))
    uploadFile.send_keys(file_loc)

    # click on submit to upload result
    submit1 = wait.until(EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
    submit1.click()

    # waits until the submit is invisible
    WebDriverWait(driver, 40).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))

    # waits until the Loading symbol is invisible
    WebDriverWait(driver, 40).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    # success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "File has been uploaded successfully!")))

