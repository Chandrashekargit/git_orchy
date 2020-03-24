import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.Application_module_xpath import *
import conftest


@mark.check_remediation_info
def test_remediation_info(driver):
    """
    > These function lets us check the remediation info all the vulnerabilities (in app variable,
        enter the required application xpath whose vul's needs the check on remediation info)
    > if the vulnerability has remediation info it will close that vulnerable, if not it moves to next vulnerable
    > These script is very fragile, breaks at multiple points and i'm not fixing it. [its a conscious decision,
        i m not fixing it coz, xpath's will be changed once the placement of vulnerability is changed,
        solution is take the xpath in such a way that it should contain vulnerable name i mean grab the text of element
        and create a list with those xpath's, if you have 100 vul's need to make 100 xpath's (these function is executed
         in a special way which cant be explained here)]
    > To check the remediation info of any application vulnerabilities change the application xpath in 'app' variable.
    """
    applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    app = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'SCA')]")))
    app.click()

    close_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
        EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
    close_vul.click()
    for j in range(1, 6):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 900);")
        time.sleep(1)

        individual_vulnerable1 = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[2]//div//p"))).text

        click_individual_vulnerable = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[2]//div//p")))
        click_individual_vulnerable.click()
        time.sleep(6)
        data1 = WebDriverWait(driver, 10, poll_frequency=3).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='tab-pane card-body show fade active']//div[@class='row']"))).text

        if data1[0:10]:
            # print("Remediation info is visible")
            # print(data1)
            time.sleep(1)
            reopen = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable((By.XPATH, reopen_btn)))
            reopen.click()

            justi = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.presence_of_element_located((By.XPATH, justification)))
            justi.send_keys("SQL vulnerable isn't fixed, reopening the vulnerable")

            re_open_vul_submit = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.presence_of_element_located((By.XPATH, reopen_submit)))
            re_open_vul_submit.click()

            time.sleep(2)
            close_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
            close_vul.click()
        else:
            time.sleep(1)
            print("\nvul name: ", individual_vulnerable1)
            go_back_to_closed_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Closed')]")))
            go_back_to_closed_vul.click()


@mark.reopen_no_remedi_info
def test_data(driver):
    """
    These function needs no attention and i know i haven't incremented 'i' value in while loop. Chill.
    """
    # wait = WebDriverWait(driver, 10, poll_frequency=3)
    applicationTab = WebDriverWait(driver, 10, poll_frequency=1).until(
        EC.element_to_be_clickable((By.XPATH, application_tab)))
    applicationTab.click()

    app = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'SCA')]")))
    app.click()

    close_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
        EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
    close_vul.click()
    j = 1
    while j <= 1:
        driver.execute_script("window.scrollTo(0, 900);")
        time.sleep(1)

        # click_individual_vulnerable1 = WebDriverWait(driver, 10, poll_frequency=3).until(
        #     EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[2]//div//p"))).text

        click_individual_vulnerable = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, f"//tr[@aria-rowindex={j}]//td[2]//div//p")))
        click_individual_vulnerable.click()
        time.sleep(5)

        # print("Remediation info is visible")
        # print(data1)
        time.sleep(1)
        reopen = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.element_to_be_clickable((By.XPATH, reopen_btn)))
        reopen.click()

        justi = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.presence_of_element_located((By.XPATH, justification)))
        justi.send_keys("SQL vulnerable isn't fixed, reopening the vulnerable")

        re_open_vul_submit = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.presence_of_element_located((By.XPATH, reopen_submit)))
        re_open_vul_submit.click()

        time.sleep(2)
        close_vul = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.element_to_be_clickable((By.XPATH, closed_vulnerability)))
        close_vul.click()
