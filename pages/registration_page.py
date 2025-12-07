from .base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from helpers.data import Config
import allure


class RegistrationPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, Config.SIGNUP_PAGE)
        self.locators = RegistrationPageLocators()
    
    @allure.step("Заполнить всю форму регистрации")
    def fill_registration_form(self, user_data):
        self.fill_field(self.locators.REG_FIRST_NAME_INPUT, user_data.first_name)
        self.fill_field(self.locators.REG_LAST_NAME_INPUT, user_data.last_name)
        self.fill_field(self.locators.REG_USERNAME_INPUT, user_data.username)
        self.fill_field(self.locators.REG_EMAIL_INPUT, user_data.email)
        self.fill_field(self.locators.REG_PASSWORD_INPUT, user_data.password)
    
    @allure.step("Нажать кнопку 'Создать аккаунт'")
    def click_register_button(self):
        self.click_element(self.locators.REG_REGISTER_BUTTON)
