from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, link):
        self.driver = driver
        self.driver.get(link)

    def get_element(self, selector: str, timeout: int = 10) -> WebElement:
        """Получить элемент страницы по селектору css"""
        element = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        return element

    def get_elements(self, selector: str) -> list[WebElement]:
        """Получить элементы"""
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return elements

    @staticmethod
    def set_element_value(element: WebElement, value: str):
        """Задать значение элемента"""
        element.send_keys(value)
