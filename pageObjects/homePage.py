import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browser_utils import BrowserUtils


class HomePage(BrowserUtils):
    def __init__(self,driver,wait):
        super().__init__(driver)

        self.driver = driver
        self.wait = wait


    def buscar_fondo(self,filtrar_por,tipo_fondo):

        self.click_radio_button(filtrar_por)
        self.click_dropdowns()
        self.select_option_dropdowns(tipo_fondo)
        self.click_button_a("Buscar")

        self._wait_for_element("//h2[contains(text(),'" + tipo_fondo + "')]")
        #self.wait.until(
         #   expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'" + tipo_fondo + "')]")))


    def seleccionar_fondo_tabla(self, mi_fondosantander):

        xpath_table = "//table[@class='table']/tbody/tr"
        self._wait_for_element(xpath_table)
        rows = self.driver.find_elements(By.XPATH, xpath_table)

        for row in range(len(rows)):

            fm = self.driver.find_element(By.XPATH, "//table[@class='table']/tbody/tr[" + str(row + 1) + "]/td[1]/p")

            if  mi_fondosantander in fm.text:
                self.driver.find_element(By.XPATH, xpath_table+"[" + str(
                    row + 1) + "]/td[8]//span[@class='str-chevron-right text-red f-32']").click()
                break

        #self.wait.until(expected_conditions.visibility_of_element_located(
         #   (By.XPATH, "//h1[@class='heading-3 font-weight-normal' and contains(text(),'" + mi_fondosantander + "')]")))

        self.validar_fondo_seleccionado(mi_fondosantander)

    def validar_fondo_seleccionado(self,mi_fondosantander):
        self._wait_for_element(f"//h1[@class='heading-3 font-weight-normal' and contains(text(),'" + mi_fondosantander + "')]")
        success_text = self.driver.find_element(By.XPATH, "//div[@class='f-16 mt-24']/p").text
        assert mi_fondosantander in success_text


