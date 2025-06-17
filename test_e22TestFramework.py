import json
import os.path
import sys
import time

import pytest

from pageObjects.homePage import HomePage

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):

    driver = browserInstance[0]
    driver.maximize_window()
    url = "https://www.santanderassetmanagement.cl/"
    driver.get(url)

    #wait = WebDriverWait(driver, 10)
    wait = browserInstance[1]
    wait.until(expected_conditions.none_of(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='uil-ring-css']"))))
    homePage = HomePage(driver,wait)

    homePage.buscar_fondo(test_list_item["filtrar_por"],test_list_item["tipo_fondo"],)

    homePage.seleccionar_fondo_tabla(test_list_item["mi_fondo_santander"])





