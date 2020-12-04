from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
from spinner.spinner import *
import time
import pytest


@pytest.mark.correlation
def test_correlation(driver):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException])

    stop_till_spinner_is_invisible(driver)
    applicationTab = wait.until(EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    stop_till_spinner_is_invisible(driver)
    click_on_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'all res')]")))
    # click_on_app = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[.='WebGoat Application']")))
    click_on_app.click()

    stop_till_spinner_is_invisible(driver)
    open_vul = wait.until(EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
    open_vul.click()

    stop_till_spinner_is_invisible(driver)
    time.sleep(1)
    perpage_dp = wait.until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
    perpage_dp.click()
    sel_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, all)))
    sel_all_option.click()
    stop_till_spinner_is_invisible(driver)

    try:
        # checks if vulnerabilities are present, if not, it prints out the msg.
        # else, it goes to affected instance section.
        WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print("\nNo vulnerabilities are present for this application")
    except TimeoutException:
        vuls = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]//div[@class='col']/p")))
        print('\nTotal number of vul: ', len(vuls))

        for i in range(1, len(vuls)+1):
            # print('i: ', i)
            try:
                stop_till_spinner_is_invisible(driver)
                take_cwe = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(i)+"]/td[3]//a")))
                cwe = take_cwe.text
            except TimeoutException:
                stop_till_spinner_is_invisible(driver)
                take_cwe = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(i)+"]/td[3]//p")))
                cwe = take_cwe.text
            j = 1
            while j in range(len(vuls)+1):
                # print('j: ', j)
                try:
                    take_cwe_2 = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(j)+"]/td[3]//a")))
                except:
                    take_cwe_2 = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(j)+"]/td[3]//p")))

                if cwe == take_cwe_2.text:
                    # print(take_cwe_2.text)
                    get_vul_name = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(j)+"]/td[2]//p")))
                    print(get_vul_name.text+": "+take_cwe_2.text)
                j += 1
            print("*" * 20)

            # except TimeoutException:
            #     stop_till_spinner_is_invisible(driver)
            #     take_cwe = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(i)+"]/td[3]//p")))
            #     cwe = take_cwe.text
            #     j = 1
            #     while j in range(len(vuls) + 1):
            #         # print('j: ', j)
            #         take_cwe_2 = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(j)+"]/td[3]//a")))
            #         if cwe == take_cwe_2.text:
            #             # print(take_cwe_2.text)
            #             get_vul_name = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(j)+"]/td[2]//p")))
            #             print(get_vul_name.text + ": " + take_cwe_2.text)
            #         j += 1
            #     print("*" * 20)

            # rest_vuls = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tr[@class='el-table__row']/td[3]//a")))
            # if cwe in rest_vuls.text:
            #     get_vul_name = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(i+1)+"]/td[2]//p")))
            #     print(get_vul_name.text)
            # for j in range(1, len(rest_vuls)+1):
            #     take_cwe_of_remaining_vuls = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(j+1)+"]/td[3]//a")))
            #     if take_cwe_of_remaining_vuls.text == cwe:
            #         get_vul_name = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='el-table__row']["+str(j+1)+"]/td[2]//p")))
            #         print(get_vul_name.text)
