from selenium.webdriver.common.by import By

class RecipePageLocators:
    
    # ОСНОВНЫЕ ПОЛЯ
    RECIPE_NAME_INPUT = (By.XPATH, "//label[.//div[text()='Название рецепта']]/input")
    INGREDIENT_INPUT = (By.XPATH, "//label[.//div[contains(text(), 'Ингредиенты')]]/input")
    INGREDIENT_QUANTITY_INPUT = (By.XPATH, "//div[contains(@class, 'styles_ingredientsAmountInput__1F2dx')]//input")
    RECIPE_COOKING_TIME_INPUT = (By.XPATH, "//label[.//div[contains(text(), 'Время приготовления')]]/input")
    RECIPE_DESCRIPTION_INPUT = (By.XPATH, "//label[.//div[text()='Описание рецепта']]/textarea")
    
    # КНОПКИ
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    
    # АВТОДОПОЛНЕНИЕ
    INGREDIENT_SUGGESTIONS_CONTAINER = (By.XPATH, "//div[@class='styles_container__3ukwm']")
    
    # ПОСЛЕ СОЗДАНИЯ
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title__2QMPq')]")
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'styles_single-card__1yTTj')]")
