
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from helpers.data import Config
import allure


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, Config.LOGIN_PAGE)
        self.locators = LoginPageLocators()
    
    @allure.step("Выполнить авторизацию")
    def login(self, username, password):
        self.fill_field(self.locators.LOGIN_EMAIL_INPUT, username)
        self.fill_field(self.locators.LOGIN_PASSWORD_INPUT, password)
        self.click_element(self.locators.LOGIN_BUTTON)
    
    @allure.step("Проверить видимость формы авторизации")
    def is_login_form_displayed(self):
        return self.is_element_visible(self.locators.LOGIN_BUTTON)
    
    @allure.step("Проверить успешную авторизацию")
    def verify_successful_login(self):
        self.wait_for_url_change(Config.LOGIN_PAGE)
        return Config.HOME_PAGE in self.get_current_url()
