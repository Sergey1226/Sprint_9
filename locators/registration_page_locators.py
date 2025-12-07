from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    
    # Основные поля
    REG_FIRST_NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    REG_LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
    REG_USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    
    REG_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    
    # Кнопки
    REG_REGISTER_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    
