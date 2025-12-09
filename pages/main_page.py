from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from helpers.data import Config
import allure


class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, Config.HOME_PAGE)
        self.locators = MainPageLocators()
    
    @allure.step("Нажать кнопку 'Войти' в хедере")
    def click_header_login(self):
        self.click_element(self.locators.HEADER_LOGIN_BTN)
    
    @allure.step("Нажать кнопку 'Создать аккаунт' в хедере")
    def click_header_create_account(self):
        self.click_element(self.locators.HEADER_CREATE_ACCOUNT_BTN)
    
    @allure.step("Нажать кнопку 'Выход' в хедере")
    def click_header_logout(self):
        self.click_element(self.locators.HEADER_LOGOUT_BTN)
    
    @allure.step("Нажать кнопку 'Создать рецепт' в хедере")
    def click_header_create_recipe(self):
        self.click_element(self.locators.HEADER_CREATE_RECIPE_BTN)
    
    @allure.step("Перейти на страницу создания рецепта")
    def go_to_create_recipe(self):
        self.click_header_create_recipe()
    
    @allure.step("Проверить видимость кнопки 'Выход'")
    def is_logout_button_visible(self):
        return self.is_element_visible(self.locators.HEADER_LOGOUT_BTN)
    
    @allure.step("Проверить, что пользователь авторизован")
    def is_user_authenticated(self):
        return self.is_logout_button_visible()
    
    @allure.step("Выполнить выход")
    def logout(self):
        self.click_header_logout()
        self.wait_for_element_visible(self.locators.HEADER_LOGIN_BTN)
