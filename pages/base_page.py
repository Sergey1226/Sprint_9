from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure


class BasePage:
    
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.timeout = 10
    
    @allure.step("Открыть страницу {url}")
    def open(self, url=None):
        target_url = url or self.url
        if target_url:
            self.driver.get(target_url)
            self.wait_for_page_load()
        else:
            raise ValueError("URL не указан")
    
    @allure.step("Ждать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
        except TimeoutException:
            self.take_screenshot("page_load_timeout")
            raise
    
    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.take_screenshot(f"element_not_found_{str(locator)}")
            raise
    
    @allure.step("Найти кликабельный элемент: {locator}")
    def find_clickable(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            self.take_screenshot(f"element_not_clickable_{str(locator)}")
            raise
    
    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        element = self.find_clickable(locator)
        element.click()
    
    @allure.step("Заполнить поле {locator} значением: {text}")
    def fill_field(self, locator, text, clear=True):
        element = self.find_clickable(locator)
        if clear:
            element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text.strip()
    
    @allure.step("Получить значение атрибута: {attribute} элемента: {locator}")
    def get_attribute(self, locator, attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step("Проверить наличие элемента: {locator}")
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step("Ждать появления элемента: {locator}")
    def wait_for_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    @allure.step("Ждать видимости элемента: {locator}")
    def wait_for_element_visible(self, locator, timeout=None):
        timeout = timeout or self.timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Сделать скриншот: {name}")
    def take_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    
    @allure.step("Загрузить файл: {file_path} в элемент: {locator}")
    def upload_file(self, locator, file_path):
        element = self.find_element(locator)
        element.send_keys(str(file_path))
    
    @allure.step("Ждать обновления URL")
    def wait_for_url_change(self, initial_url, timeout=None):
        timeout = timeout or self.timeout
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != initial_url
        )
    
    @allure.step("Ждать URL содержащего: {expected_url}")
    def wait_for_url_contains(self, expected_url, timeout=None):
        timeout = timeout or self.timeout
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_url)
        )
