import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *

categories = ["//label[contains(text(),'SAST')]",
              "//label[contains(text(),'DAST')]",
              "//label[contains(text(),'SCA')]"]

@mark.give_data_of_individual_vulnerabilities
def test_data_of_individual_vulnerabilities(driver):
    """
        > These function gives us 'BASIC INFO' of all category vulnerabilities.
        > Before running these file make sure it has only 'SAST' scans in any one of the application.
        > To create 'SAST' application and upload all SAST scans please run these below commands one after the other,
                - "pytest -m create_apps -s -v"     (Creates an application with name called 'SAST')
                - "pytest -m sast -s -v"            (uploads all SAST scans to 'SAST' application)
                - "pytest -m dast -s -v"            (uploads all DAST scans to 'DAST' application)
                - "pytest -m sca -s -v"             (uploads all SCA scans to 'SCA' application)
        """
    for category in categories:
        if category == "//label[contains(text(),'SAST')]":
            # wait = WebDriverWait(driver, 10, poll_frequency=3)
            applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, application_tab)))
            applicationTab.click()

            app = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, category)))
            app.click()

            open_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
            open_vul.click()
            for j in range(1, 85):
                time.sleep(1)
                perpage = WebDriverWait(driver, 10, poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
                perpage.click()
                time.sleep(1)

                selectAll = WebDriverWait(driver, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, all)))
                selectAll.click()
                driver.execute_script("window.scrollTo(0, 900);")
                time.sleep(1)

                click_individual_vulnerable1 = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p"))).text
                print(click_individual_vulnerable1)

                click_individual_vulnerable = WebDriverWait(driver, 10, poll_frequency=3).until(
                    EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p")))
                click_individual_vulnerable.click()

                time.sleep(2)
                data1 = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='tab-pane card-body show fade active']//div[@class='row']"))).text
                print(data1)
                print("*" * 50)

                go_back_to_opened_vul = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located(
                    (By.XPATH, "//label[contains(text(), 'Opened')]")))
                go_back_to_opened_vul.click()

        elif category == "//label[contains(text(),'DAST')]":
            applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, application_tab)))
            applicationTab.click()

            app = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, category)))
            app.click()

            open_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
            open_vul.click()
            for j in range(1, 41):
                time.sleep(1)
                perpage = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
                perpage.click()
                time.sleep(1)

                selectAll = WebDriverWait(driver, 10, poll_frequency=1).until(
                    EC.element_to_be_clickable((By.XPATH, all)))
                selectAll.click()
                driver.execute_script("window.scrollTo(0, 900);")
                time.sleep(1)

                click_individual_vulnerable1 = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p"))).text
                print(click_individual_vulnerable1)

                click_individual_vulnerable = WebDriverWait(driver, 10, poll_frequency=3).until(
                    EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p")))
                click_individual_vulnerable.click()

                time.sleep(2)
                data1 = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='tab-pane card-body show fade active']//div[@class='row']"))).text
                print(data1)
                print("*" * 50)

                go_back_to_opened_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//label[contains(text(), 'Opened')]")))
                go_back_to_opened_vul.click()

        elif category == "//label[contains(text(),'SCA')]":
            applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, application_tab)))
            applicationTab.click()

            app = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, category)))
            app.click()

            open_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.element_to_be_clickable((By.XPATH, open_vulnerability)))
            open_vul.click()
            for j in range(1, 19):
                time.sleep(1)
                perpage = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, PerPageDropdown)))
                perpage.click()
                time.sleep(1)

                selectAll = WebDriverWait(driver, 10, poll_frequency=1).until(
                    EC.element_to_be_clickable((By.XPATH, all)))
                selectAll.click()
                driver.execute_script("window.scrollTo(0, 900);")
                time.sleep(1)

                click_individual_vulnerable1 = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p"))).text
                print(click_individual_vulnerable1)

                click_individual_vulnerable = WebDriverWait(driver, 10, poll_frequency=3).until(
                    EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[3]//div//p")))
                click_individual_vulnerable.click()

                time.sleep(2)
                data1 = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='tab-pane card-body show fade active']//div[@class='row']"))).text
                print(data1)
                print("*" * 50)

                go_back_to_opened_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//label[contains(text(), 'Opened')]")))
                go_back_to_opened_vul.click()