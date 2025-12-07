import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers.data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.recipe_page import RecipePage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope="function")
def driver():
    selenoid_uri = os.getenv("SELENOID_URI")
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    

    is_ci = os.getenv("CI")
    if is_ci and not selenoid_uri:
        chrome_options.add_argument("--headless=new")
    
    if selenoid_uri:
        chrome_options.add_argument("--disable-gpu")
        
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False,
                "enableLog": True,
                "logName": "chrome.log",
                "sessionTimeout": "5m",
                "timeZone": "UTC",
                "env": ["TZ=UTC"]
            }
        }
        
        chrome_options.set_capability("selenoid:options", capabilities["selenoid:options"])
        
        driver = webdriver.Remote(
            command_executor=selenoid_uri,
            options=chrome_options
        )
    else:
        driver = webdriver.Chrome(options=chrome_options)
    
    driver.maximize_window()
    
    yield driver
    
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def recipe_page(driver):
    return RecipePage(driver)


@pytest.fixture
def authenticated_user(driver):
    main_page = MainPage(driver)
    main_page.open()
    
    if main_page.is_user_authenticated():
        return driver
    
    main_page.click_header_login()
    
    login_page = LoginPage(driver)
    login_page.login(
        username=TestData.EXISTING_USER.username,
        password=TestData.EXISTING_USER.password
    )
    
    return driver


@pytest.fixture(autouse=True)
def allure_environment(request):
    if hasattr(request, 'node'):
        allure.dynamic.title(request.node.name)
        allure.dynamic.description(
            f"Тест: {request.node.name}"
        )
