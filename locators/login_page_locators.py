from selenium.webdriver.common.by import By

class LoginPageLocators:
    
    # Поля формы
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

