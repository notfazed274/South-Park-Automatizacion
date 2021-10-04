from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class spInicioSesion():
    def __init__(self, driver):
        self.driver = driver
        self.URL = ('https://www.southpark.lat/')
        self.email_input = (By.NAME, 'email')
        self.password_input = (By.NAME, 'password')
        self.mostrar_password = (By.CLASS_NAME, 'show')
        self.entrar = (By.CLASS_NAME, 'btn.confirm-form')

    def abrir_url(self):
        self.driver.get(self.URL)

    def inicio_sesion(self, cuenta, password):

        input_email = self.driver.find_element(*self.email_input)
        input_email.clear()
        input_email.send_keys(cuenta)

        self.driver.find_element(*self.mostrar_password).click()

        input_pass = self.driver.find_element(*self.password_input)
        input_pass.clear()
        input_pass.send_keys(password)

        self.driver.find_element(*self.entrar).click()