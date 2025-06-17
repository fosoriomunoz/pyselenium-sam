from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BrowserUtils:

    def __init__(self,driver):
        self.driver = driver
        self.input_dropdown_list = "//div[contains(@class,'cajaInput select-cont')]"



    def _wait_for_element(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((By.XPATH,by_locator))
            )
            return True
        except TimeoutException:
            print("El elemento no fue encontrado" + by_locator)
            return False



    def click_radio_button(self,filtro_radio_button):
        print(filtro_radio_button)
        try:
            selected_radio_button = "//label[contains(text(),'" + filtro_radio_button + "')]"
            self.driver.find_element(By.XPATH,selected_radio_button).click()

        except TimeoutException:
            raise Exception("No se pudo hacer click en radibutton")

    def click_dropdowns(self):
        try:
            self.driver.find_element(By.XPATH,self.input_dropdown_list).click()
        except TimeoutException:
            raise Exception("No se pudo hacer click en dropdows")

    def select_option_dropdowns(self, opcion):
        try:
            option_selected ="//ul/li[contains(text(),'"+opcion+"')]"
            self.driver.find_element(By.XPATH,option_selected).click()
        except TimeoutException:
            raise Exception("No se pudo hacer seleccionar elemento dropdowns")

    def click_button_a(self,texto_boton):

        try:
            boton = "//a[contains(text(),'" + texto_boton + "')]"
            self.driver.find_element(By.XPATH, boton).click()
        except TimeoutException:
            raise Exception("No se pudo hacer click en boton")



