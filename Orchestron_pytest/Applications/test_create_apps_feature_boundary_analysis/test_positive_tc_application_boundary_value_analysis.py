import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from xpath.Application_module_xpath import *
from Applications.test_create_applications.create_app import create_apps


app_names = ['!@#$%^&*() 1234567890! createapp with alphanum,spl', '1234567890', 'D']
urls = ['http://demo.com', 'http://demo.com', 'http://D.com']


@mark.create_app_positive_tc
def test_positive_tc_application_boundary_value_analysis(driver):
    for (app_name, urL) in zip(app_names, urls):
        # calling the function 'create_apps' to verify if applications with different nomenclature can be created.
        create_apps(driver, application_name=app_name, url=urL)
