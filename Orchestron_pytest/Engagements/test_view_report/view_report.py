from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Engagement_module_xpath import *
import time


def view_exec_report(driver, engagement_name_xpath):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException
    ])
    # clicks on Engagement section
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    eng_tab = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_tab)))
    eng_tab.click()

    WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='loading-background']")))
    click_on_individual_eng = wait.until(EC.element_to_be_clickable((By.XPATH, engagement_name_xpath)))
    click_on_individual_eng.click()

    WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='loading-background']")))
    time.sleep(2)
    action = wait.until(EC.element_to_be_clickable((By.XPATH, action_dropdown)))
    action.click()

    select_view_report = wait.until(EC.element_to_be_clickable((By.XPATH, eng_viewreport)))
    select_view_report.click()

    # Exec summary
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1000);")
    last_page_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Go to last page']")))
    last_page_btn.click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
    last_page = wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='page-item active']")))
    num_of_pages = int(last_page.text)
    first_page = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Go to first page']")))
    first_page.click()
    for i in range(1, num_of_pages+1):
        WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        print("Page: ", i)
        move_to_nxt_page = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Go to page "+str(i)+"']")))
        move_to_nxt_page.click()

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
        vul_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card mb-1']/button")))
        print("Number of vulnerabilities: ", len(vul_list))
        for j in range(1, len(vul_list)+1):
            WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            click_on_vul = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='card mb-1']["+str(j)+"]/button")))
            click_on_vul.click()

            # check if vulnerability has 'App', 'CWE', 'open for' info
            WebDriverWait(driver, 10, poll_frequency=1).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loading-background']")))
            vul_application_info = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='card mb-1']["+str(j)+"]//div[@class='row'][1]/div/p[1]/span[1]")))
            assert vul_application_info.text == "Application"

            vul_cwe_info = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='card mb-1']["+str(j)+"]//div[@class='row'][1]/div/p[2]/span[1]")))
            assert vul_cwe_info.text == "CWE"

            vul_openfor_info = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='card mb-1']["+str(j)+"]//div[@class='row'][1]/div/p[3]/span[1]")))
            assert "Open for" in vul_openfor_info.text
