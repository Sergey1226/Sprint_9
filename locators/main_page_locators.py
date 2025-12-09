from selenium.webdriver.common.by import By

class MainPageLocators:
    
    # Навигационные кнопки
    HEADER_CREATE_ACCOUNT_BTN = (By.XPATH, "//a[text()='Создать аккаунт']")
    HEADER_LOGIN_BTN = (By.XPATH, "//a[text()='Войти']")
    HEADER_LOGOUT_BTN = (By.XPATH, "//a[text()='Выход']")
    HEADER_CREATE_RECIPE_BTN = (By.XPATH, "//a[text()='Создать рецепт']")