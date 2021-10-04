from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class spHomepage():
    def __init__(self, driver):
        self.driver = driver

        self.URL = 'https://www.southpark.lat/'

        self.boton_cuenta = (By.CSS_SELECTOR, 'a[aria-label="Cuenta"]')

        self.seasonsHov = (By.LINK_TEXT, 'Episodios Completos')

        self.temporada = (By.CSS_SELECTOR, 'button.ek77yn3.e18ufbr50.css-1dw03p0-StyledTypography-StyledButton-StyledButton.e1wje7qk0')

        self.fullscreen = (By.CLASS_NAME, 'edge-gui-fullscreen-button')

        self.video_player = (By.CLASS_NAME, 'edge-player-ads-element')

    def abrir_url(self):
        self.driver.get(self.URL)

    def boton_inicio_sesion(self):
        self.driver.find_element_by_css_selector('a[aria-label="Cuenta"]').click()

    def seasons(self):
        cerrar_popup = self.driver.find_element_by_class_name('page-overlay_close')
        cerrar_popup.click()

        seasonsHov = self.driver.find_element(*self.seasonsHov)
        seasonsHov.click()

    def seleccionar_temp(self, index):

        boton_elegir_temporada = self.driver.find_element(*self.temporada)
        boton_elegir_temporada.click()

        seleccionar_temporada = self.driver.find_element_by_css_selector(f'[href*="temporada-{index}"]')
        seleccionar_temporada.click()

    def seleccionar_cap(self, cap):
        capitulo_elegido = self.driver.find_element_by_css_selector(f'[href*="-ep-{cap}"]')
        capitulo_elegido.click()

    def reprod_video(self):

        fullscreen = self.driver.find_element(*self.fullscreen)
        a = ActionChains(self.driver)
        video_reprod = self.driver.find_element(*self.video_player)
        a.move_to_element(video_reprod).move_to_element(fullscreen).click().perform()











