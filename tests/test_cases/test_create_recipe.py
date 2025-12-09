import allure
import pytest
import os
from helpers.data import TestData, Config
from pages.main_page import MainPage
from pages.recipe_page import RecipePage

@allure.feature("Создание рецепта")
@allure.story("Создание нового рецепта")
class TestCreateRecipe:
    @pytest.mark.skipif(os.getenv("CI") == "true", reason="Требует дополнительной настройки в CI")
    @allure.title("Тест успешного создания рецепта с изображением")
    def test_successful_recipe_creation(self, authenticated_user):
        with allure.step("Проверить авторизацию пользователя"):
            main_page = MainPage(authenticated_user)
            assert main_page.is_user_authenticated(), "Пользователь должен быть авторизован"
        
        with allure.step("Перейти на страницу создания рецепта"):
            main_page.go_to_create_recipe()
            recipe_page = RecipePage(authenticated_user)
            recipe_page.wait_for_url_contains("/create")
        
        with allure.step("Заполнить все поля формы создания рецепта"):
            recipe_page.create_recipe(
                recipe_data=TestData.RECIPE,
                image_path=Config.get_test_image_path()
            )
        
        with allure.step("Проверить редирект со страницы создания"):
            assert recipe_page.wait_for_redirect_from_create(), \
                "Не произошел редирект со страницы создания рецепта"
            
            assert not recipe_page.is_on_create_page(), \
                f"Остались на странице создания. URL: {recipe_page.get_current_url()}"
        
        with allure.step("Проверить отображение карточки рецепта"):
            recipe_page.wait_for_recipe_card()
            assert recipe_page.is_recipe_card_visible(), \
                "Карточка созданного рецепта не отображается"
        
        with allure.step("Проверить название созданного рецепта"):
            created_name = recipe_page.get_created_recipe_name()
            assert TestData.RECIPE.name in created_name, \
                f"Название рецепта не совпадает. Ожидалось: '{TestData.RECIPE.name}', получено: '{created_name}'"

