import allure
import pytest
from helpers.data import TestData


@allure.feature("Авторизация")
@allure.story("Вход в систему")
class TestAuthorization:
    
    @allure.title("Тест успешной авторизации пользователя")
    def test_successful_login(self, main_page, login_page):

        with allure.step("Нажать кнопку «Войти» на главной странице"):
            main_page.click_header_login()
        
        with allure.step("Заполнить все поля формы авторизации"):
            login_page.login(
                username=TestData.EXISTING_USER.username,
                password=TestData.EXISTING_USER.password
            )
        
        with allure.step("Проверить успешную авторизацию"):
            assert login_page.verify_successful_login(), \
                "Авторизация не удалась - не произошел редирект на главную"
        
        with allure.step("Проверить отображение кнопки «Выход»"):
            assert main_page.is_logout_button_visible(), \
                "Кнопка 'Выход' не отображается после авторизации"

