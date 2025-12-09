import allure
import pytest
from helpers.data import TestData, Config


@allure.feature("Регистрация")
@allure.story("Создание нового аккаунта")
class TestRegistration:
    
    @allure.title("Тест успешной регистрации нового пользователя")
    def test_successful_registration(self, main_page, registration_page, login_page):
        with allure.step("Нажать кнопку «Создать аккаунт»"):
            main_page.click_header_create_account()
        
        with allure.step("Заполнить все поля формы регистрации"):
            registration_page.fill_registration_form(TestData.get_new_user())
        
        with allure.step("Нажать кнопку «Создать аккаунт»"):
            registration_page.click_register_button()
        
        with allure.step("Проверить переход на страницу авторизации"):
            login_page.wait_for_url_contains("/signin")
            current_url = login_page.get_current_url()
            
            assert "/signin" in current_url, \
                f"После регистрации должен быть редирект на страницу авторизации, а не: {current_url}"
            
            assert Config.LOGIN_PAGE in current_url or "/signin" in current_url, \
                f"URL не соответствует странице авторизации: {current_url}"
        
        with allure.step("Проверить отображение формы авторизации"):
            assert login_page.is_login_form_displayed(), \
                "После регистрации должна отображаться форма авторизации"
