from xpath.Application_module_xpath import *
from spinner.spinner import *
import time


def open_manual_vulnerability(driver, individual_vul_xpath, application_name_xpath):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    stop_till_spinner_is_invisible(driver)
    stop_till_spinner_is_invisible(driver)
    time.sleep(2)
    click_on_individual_eng = wait.until(EC.element_to_be_clickable((By.XPATH, application_name_xpath)))
    click_on_individual_eng.click()

    # Clicks on Open vulnerability section.
    stop_till_spinner_is_invisible(driver)
    open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    # clicks on individual vul
    stop_till_spinner_is_invisible(driver)
    time.sleep(2)
    click_on_individual_vul = wait.until(EC.element_to_be_clickable((By.XPATH, individual_vul_xpath)))
    click_on_individual_vul.click()

    # wait till affected instance section is visible
    stop_till_spinner_is_invisible(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, affected_instance)))

    # wait till vul info section is visible
    stop_till_spinner_is_invisible(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, vulnerability_info)))

    # moves to affected instance Section
    stop_till_spinner_is_invisible(driver)
    move_to_ai = wait.until(EC.element_to_be_clickable((By.XPATH, affected_instance)))
    move_to_ai.click()
    stop_till_spinner_is_invisible(driver)


def sca_evd(driver, module_name, version_id, cve_id):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
    click_on_create_evd_btn.click()

    stop_till_spinner_is_invisible(driver)
    sca_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, sca_toggle_btn)))
    sca_evd_enable.click()

    stop_till_spinner_is_invisible(driver)
    module = wait.until(EC.presence_of_element_located((By.XPATH, module_xpath)))
    module.send_keys(module_name)

    version = wait.until(EC.presence_of_element_located((By.XPATH, version_xpath)))
    version.send_keys(version_id)

    cve = wait.until(EC.presence_of_element_located((By.XPATH, cve_xpath)))
    cve.send_keys(cve_id)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
    submit.click()

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
    # wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))


def sast_evd(driver, line_no, line_range, code_snippet_location, path, file_name, param):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
    click_on_create_evd_btn.click()

    stop_till_spinner_is_invisible(driver)
    sast_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, sast_toggle_btn)))
    sast_evd_enable.click()

    stop_till_spinner_is_invisible(driver)
    enter_line_no = wait.until(EC.element_to_be_clickable((By.XPATH, line_no_xpath)))
    enter_line_no.send_keys(line_no)

    enter_line_range = wait.until(EC.element_to_be_clickable((By.XPATH, line_range_xpath)))
    enter_line_range.send_keys(line_range)

    enter_code_snippet = wait.until(EC.presence_of_element_located((By.XPATH, code_snippet_xpath)))
    enter_code_snippet.send_keys(code_snippet_location)

    enter_path = wait.until(EC.element_to_be_clickable((By.XPATH, path_xpath)))
    enter_path.send_keys(path)

    enter_file_name = wait.until(EC.element_to_be_clickable((By.XPATH, file_name_xpath)))
    enter_file_name.send_keys(file_name)

    enter_param = wait.until(EC.element_to_be_clickable((By.XPATH, param_xpath)))
    enter_param.send_keys(param)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
    submit.click()

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
    # wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))


def dast_evd(driver, enter_url, enter_param, enter_payload, req_file_loc, response_file_loc):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
    click_on_create_evd_btn.click()

    stop_till_spinner_is_invisible(driver)
    dast_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, dast_toggle_btn)))
    dast_evd_enable.click()

    stop_till_spinner_is_invisible(driver)
    url = wait.until(EC.element_to_be_clickable((By.XPATH, url_xpath)))
    url.send_keys(enter_url)

    param = wait.until(EC.element_to_be_clickable((By.XPATH, param_xpath)))
    param.send_keys(enter_param)

    payload = wait.until(EC.element_to_be_clickable((By.XPATH, payload_xpath)))
    payload.send_keys(enter_payload)

    request = wait.until(EC.presence_of_element_located((By.XPATH, request_xpath)))
    request.send_keys(req_file_loc)

    response = wait.until(EC.presence_of_element_located((By.XPATH, response_xpath)))
    response.send_keys(response_file_loc)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
    submit.click()

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
    # wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))


def container_evd(driver, enter_module, enter_version, enter_cpe, enter_image_digest, enter_registry_container, enter_image_name, enter_image_repository, enter_cve):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    click_on_create_evd_btn = wait.until(EC.element_to_be_clickable((By.XPATH, create_evidence_btn)))
    click_on_create_evd_btn.click()

    stop_till_spinner_is_invisible(driver)
    container_evd_enable = wait.until(EC.element_to_be_clickable((By.XPATH, dast_toggle_btn)))
    container_evd_enable.click()

    stop_till_spinner_is_invisible(driver)
    module = wait.until(EC.element_to_be_clickable((By.XPATH, module_xpath)))
    module.send_keys(enter_module)

    version = wait.until(EC.element_to_be_clickable((By.XPATH, version_xpath)))
    version.send_keys(enter_version)

    cpe = wait.until(EC.presence_of_element_located((By.XPATH, cpe_xpath)))
    cpe.send_keys(enter_cpe)

    image_digest = wait.until(EC.presence_of_element_located((By.XPATH, image_digest_xpath)))
    image_digest.send_keys(enter_image_digest)

    registry_container = wait.until(EC.presence_of_element_located((By.XPATH, registry_container_xpath)))
    registry_container.send_keys(enter_registry_container)

    image_name = wait.until(EC.presence_of_element_located((By.XPATH, image_digest_xpath)))
    image_name.send_keys(enter_image_name)

    image_repository = wait.until(EC.presence_of_element_located((By.XPATH, image_repository_xath)))
    image_repository.send_keys(enter_image_repository)

    cve = wait.until(EC.presence_of_element_located((By.XPATH, cve_xpath)))
    cve.send_keys(enter_cve)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, evd_submit)))
    submit.click()

    stop_till_spinner_is_invisible(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, evd_success_msg)))
    # wait.until(EC.invisibility_of_element((By.XPATH, evd_success_msg)))