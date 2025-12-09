from pathlib import Path
from dataclasses import dataclass
import random
import string


class Config:
    
    # Базовые URL
    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru"
    HOME_PAGE = BASE_URL
    LOGIN_PAGE = f"{BASE_URL}/signin"
    SIGNUP_PAGE = f"{BASE_URL}/signup"
    CREATE_RECIPE_PAGE = f"{BASE_URL}/recipes/create"
    
    # Пути к файлам
    PROJECT_DIR = Path(__file__).parent.parent
    ASSETS_DIR = PROJECT_DIR / 'assets'
    TEST_IMAGE = ASSETS_DIR / 'test_recipe_image.jpg'
    
    @classmethod
    def get_test_image_path(cls):
        if not cls.TEST_IMAGE.exists():
            raise FileNotFoundError(
                f"Тестовое изображение не найдено: {cls.TEST_IMAGE}\n"
                f"Поместите изображение в папку: {cls.ASSETS_DIR}"
            )
        return str(cls.TEST_IMAGE.absolute())


@dataclass
class UserData:
    username: str
    email: str
    password: str
    first_name: str = "Test"
    last_name: str = "User"


@dataclass
class RecipeData:
    name: str
    description: str
    cooking_time: str
    ingredient: str
    quantity: str


class TestData:
    
    @classmethod
    def get_new_user(cls):
        random_suffix = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        return UserData(
            username=f"test_user_{random_suffix}",
            email=f"test_{random_suffix}@example.com",
            password="TestPass123!",
            first_name="Иван",
            last_name="Тестов"
        )
    
    # Существующий пользователь для авторизации
    EXISTING_USER = UserData(
        username="TestFN",
        email="testfn@ya.ru",
        password="78787878jk"
    )
    
    # Данные для рецепта
    RECIPE = RecipeData(
        name="Тестовый рецепт",
        description="Описание тестового рецепта",
        cooking_time="30",
        ingredient="ванилин",
        quantity="2"
    )
