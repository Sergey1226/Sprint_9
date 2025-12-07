from .base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators
from helpers.data import Config
import allure
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecipePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, Config.CREATE_RECIPE_PAGE)
        self.locators = RecipePageLocators()
    
    @allure.step("Заполнить поле 'Название рецепта'")
    def fill_recipe_name(self, name):
        self.fill_field(self.locators.RECIPE_NAME_INPUT, name)
    
    @allure.step("Заполнить поле 'Описание рецепта'")
    def fill_description(self, description):
        self.fill_field(self.locators.RECIPE_DESCRIPTION_INPUT, description)
    
    @allure.step("Заполнить поле 'Время приготовления'")
    def fill_cooking_time(self, minutes):
        self.fill_field(self.locators.RECIPE_COOKING_TIME_INPUT, minutes)
    
    @allure.step("Добавить ингредиент с количеством")
    def add_ingredient(self, ingredient_name, quantity):
        self.fill_field(self.locators.INGREDIENT_INPUT, ingredient_name[:3])
        
        try:
            self.wait_for_element_visible(self.locators.INGREDIENT_SUGGESTIONS_CONTAINER, timeout=3)
            
            suggestion_locator = (
                self.locators.INGREDIENT_SUGGESTIONS_CONTAINER[0],
                f"{self.locators.INGREDIENT_SUGGESTIONS_CONTAINER[1]}/div[text()='{ingredient_name}']"
            )
            self.click_element(suggestion_locator)
        except:
            self.take_screenshot("ingredient_suggestions_not_found")
        
        self.fill_field(self.locators.INGREDIENT_QUANTITY_INPUT, quantity)
        
        self.click_element(self.locators.ADD_INGREDIENT_BUTTON)
    
    @allure.step("Загрузить изображение рецепта")
    def upload_recipe_image(self, image_path):
        image_path_obj = Path(image_path)
        if not image_path_obj.exists():
            raise FileNotFoundError(f"Изображение не найдено: {image_path}")
        
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(str(image_path_obj.absolute()))
    
    @allure.step("Нажать кнопку 'Создать рецепт'")
    def click_create_recipe_button(self):
        self.click_element(self.locators.CREATE_RECIPE_BUTTON)
    
    @allure.step("Создать рецепт")
    def create_recipe(self, recipe_data, image_path=None):
        self.fill_recipe_name(recipe_data.name)
        self.fill_description(recipe_data.description)
        self.fill_cooking_time(recipe_data.cooking_time)
        
        self.add_ingredient(recipe_data.ingredient, recipe_data.quantity)
        
        if image_path:
            self.upload_recipe_image(image_path)
        
        self.click_create_recipe_button()
    
    @allure.step("Проверить, что ушли со страницы создания")
    def is_on_create_page(self):
        current_url = self.get_current_url()
        return "/create" in current_url
    
    @allure.step("Дождаться редиректа со страницы создания")
    def wait_for_redirect_from_create(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: "/create" not in d.current_url
            )
            return True
        except:
            return False
    
    @allure.step("Дождаться появления карточки рецепта")
    def wait_for_recipe_card(self, timeout=10):
        self.wait_for_element_visible(self.locators.RECIPE_CARD, timeout)
    
    @allure.step("Получить название созданного рецепта")
    def get_created_recipe_name(self):
        return self.get_text(self.locators.RECIPE_TITLE)
    
    @allure.step("Проверить видимость карточки рецепта")
    def is_recipe_card_visible(self):
        return self.is_element_visible(self.locators.RECIPE_CARD)
