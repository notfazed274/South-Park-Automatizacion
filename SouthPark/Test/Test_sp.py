from selenium import webdriver
import pytest
import time
from SouthPark.Pages.spInicioSesion import spInicioSesion
from SouthPark.Pages.spHomePage import spHomepage


class TestSP():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=r'C:/Users/Federico/Documents/Webdrivers/chromedriver.exe')
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('https://www.southpark.lat/')
        yield
        time.sleep(10)
        driver.close()
        driver.quit()
        print("Test completed")

    def test_InicioSesion(self, test_setup):
        spIS = spInicioSesion(driver)
        spHP = spHomepage(driver)
        spHP.boton_inicio_sesion()
        spIS.inicio_sesion('abc', '123')

    def test_Episodio(self, test_setup):
        spHP = spHomepage(driver)
        spHP.seasons()
        spHP.seleccionar_temp('10')
        spHP.seleccionar_cap('8')
        spHP.reprod_video()


