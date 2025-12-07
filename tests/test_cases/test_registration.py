import allure
import pytest
from helpers.data import TestData
from pages.login_page import LoginPage


@allure.feature("Регистрация")
@allure.story("Создание нового аккаунта")
class TestRegistration:
    
    @allure.title("Тест успешной регистрации нового пользователя")
    def test_successful_registration(self, main_page, registration_page):
        with allure.step("Нажать кнопку «Создать аккаунт»"):
            main_page.click_header_create_account()
        
        with allure.step("Заполнить все поля формы регистрации"):
            registration_page.fill_registration_form(TestData.get_new_user())
        
        with allure.step("Нажать кнопку «Создать аккаунт»"):
            registration_page.click_register_button()
        
        with allure.step("Проверить переход на страницу авторизации"):
            registration_page.wait_for_url_change(registration_page.url)
            current_url = registration_page.get_current_url()
            assert "/signin" in current_url, \
                f"После регистрации должен быть редирект на страницу авторизации, а не: {current_url}"
        
        with allure.step("Проверить отображение формы авторизации"):
            login_page = LoginPage(registration_page.driver)
            assert login_page.is_login_form_displayed(), \
                "После регистрации должна отображаться форма авторизации"
