from selenium.webdriver.common.keys import Keys
from xpath.Application_module_xpath import *
import time
from spinner.spinner import *


def upload_res(driver, application, tool_name, scan_name, file_loc):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    time.sleep(2)
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # select the required app
    stop_till_spinner_is_invisible(driver)
    app = wait.until(EC.element_to_be_clickable((By.XPATH, application)))
    app.click()

    # click on action drop down
    stop_till_spinner_is_invisible(driver)
    time.sleep(2)
    action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action.click()

    # select 'upload results' option
    upload_result = wait.until(EC.element_to_be_clickable((By.XPATH, upload_results)))
    upload_result.click()

    # select required tool from tool dropdown
    stop_till_spinner_is_invisible(driver)
    selectTool = wait.until(EC.element_to_be_clickable((By.XPATH, tool)))
    selectTool.click()
    selectTool.send_keys(tool_name)
    selectTool.send_keys(Keys.ARROW_DOWN)
    selectTool.send_keys(Keys.ENTER)

    # enter the scan name
    scan_Name = wait.until(EC.presence_of_element_located((By.XPATH, name)))
    scan_Name.send_keys(scan_name)

    # upload the required file (xml or JSON)
    uploadFile = wait.until(EC.presence_of_element_located((By.XPATH, file)))
    uploadFile.send_keys(file_loc)

    try:
        # click on submit to upload result
        submit1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, upload_results_submit)))
        submit1.click()
        stop_till_spinner_is_invisible(driver)
    except TimeoutException:
        print("Submit button not visible")

    # waits until the submit is invisible
    # WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.XPATH, upload_results_submit)))

    # stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, success_msg_for_scan_uploaded)))
    # stop_till_spinner_is_invisible(driver)
