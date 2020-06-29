import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from selenium.webdriver.common.action_chains import ActionChains


def create_manual_evd(driver, individual_vul_xpath):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    # Clicks on Open vulnerability section.
    open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    # clicks on individual vul
    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, individual_vul_xpath)))
    click_on_individual_vul.click()

    # wait till affected instance section is visible
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, affected_instance)))

    # moves to affected instance Section
    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    move_to_ai = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
    move_to_ai.click()


def sca_evd(driver, module_name, version_id, cve_id):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
    click_on_create_evd_btn.click()

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    sca_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, sca_toggle_btn)))
    sca_evd_enable.click()

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    module = wait.until(EC.presence_of_element_located((By.XPATH, module_xpath)))
    module.send_keys(module_name)

    version = wait.until(EC.presence_of_element_located((By.XPATH, version_xpath)))
    version.send_keys(version_id)

    cve = wait.until(EC.presence_of_element_located((By.XPATH, cve_xpath)))
    cve.send_keys(cve_id)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
    submit.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
    wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))


def sast_evd(driver, line_no, line_range, code_snippet_location, path, file_name, param):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
    click_on_create_evd_btn.click()

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    sast_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, sast_toggle_btn)))
    sast_evd_enable.click()

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    enter_line_no = wait.until(EC.element_to_be_clickable((By.XPATH, line_no_xpath)))
    enter_line_no.send_keys(line_no)

    enter_line_range = wait.until(EC.element_to_be_clickable((By.XPATH, line_range_xpath)))
    enter_line_range.send_keys(line_range)

    wait.until(EC.visibility_of_element_located((By.XPATH, code_snippet_xpath)))
    enter_code_snippet = wait.until(EC.presence_of_element_located((By.XPATH, code_snippet_xpath)))
    ActionChains(driver).move_to_element(enter_code_snippet).send_keys(code_snippet_location).perform()

    enter_path = wait.until(EC.element_to_be_clickable((By.XPATH, path_xpath)))
    enter_path.send_keys(path)

    enter_file_name = wait.until(EC.element_to_be_clickable((By.XPATH, file_name_xpath)))
    enter_file_name.send_keys(file_name)

    enter_param = wait.until(EC.element_to_be_clickable((By.XPATH, param_xpath)))
    enter_param.send_keys(param)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
    submit.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
    wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))


def dast_evd(driver, enter_url, enter_param, enter_payload, req_file_loc, response_file_loc):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
    click_on_create_evd_btn.click()

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    dast_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, dast_toggle_btn)))
    dast_evd_enable.click()

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    url = wait.until(EC.element_to_be_clickable((By.XPATH, url_xpath)))
    url.send_keys(enter_url)

    param = wait.until(EC.element_to_be_clickable((By.XPATH, param_xpath)))
    param.send_keys(enter_param)

    payload = wait.until(EC.element_to_be_clickable((By.XPATH, payload_xpath)))
    payload.send_keys(enter_payload)

    request = wait.until(EC.element_to_be_clickable((By.XPATH, request_xpath)))
    # request.send_keys(req_file_loc)
    ActionChains(driver).move_to_element(request).send_keys(req_file_loc).perform()

    response = wait.until(EC.element_to_be_clickable((By.XPATH, response_xpath)))
    response.send_keys(response_file_loc)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
    submit.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
    wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))
