from dataclasses import dataclass

from selenium.webdriver.chrome.webdriver import WebDriver

from base_page import BasePage


class AuthorizationPage(BasePage):
    link = 'https://b2c.passport.rt.ru'

    def __init__(self, driver: WebDriver):
        super().__init__(driver, self.link)


    @dataclass()
    class Element:
        tab_telephone = '#t-btn-tab-phone'
        tab_mail = '#t-btn-tab-mail'
        tab_login = '#t-btn-tab-login'
        tab_account = '#t-btn-tab-ls'
        username = '#username'
        password = '#password'
        remember_checkbox = 'input[name="rememberMe"]'
        submit_button = '#kc-login'

        password_error_message_auth = '#form-error-message'
        password_error_telephone_empty = '.rt-input-container__meta.rt-input-container__meta--error'
        password_error_telephone_format = '.rt-input-container__meta.rt-input-container__meta--error'
        password_error_mail_format = '.rt-input-container__meta.rt-input-container__meta--error'
        password_error_mail_empty = '.rt-input-container__meta.rt-input-container__meta--error'

    def change_tab(self, new_tab: str):
        """Перейти на вкладку"""
        element = self.get_element(new_tab)
        element.click()

    def set_username(self, value: str):
        """Установить значение поля Почта/Телефон"""
        element = self.get_element(self.Element.username)
        self.set_element_value(element, value)

    def set_password(self, value: str):
        """Установить значение поля Пароль"""
        element = self.get_element(self.Element.password)
        self.set_element_value(element, value)

    def submit(self):
        """Подтвердить форму"""
        element = self.get_element(self.Element.submit_button)
        element.click()

    def get_password_error_text_auth(self) -> str:
        element = self.get_element(self.Element.password_error_message_auth)
        return element.text

    def get_auth_telephone_empty(self) -> str:
        element = self.get_element(self.Element.password_error_telephone_empty)
        return element.text

    def get_auth_telephone_format(self) -> str:
        element = self.get_element(self.Element.password_error_telephone_format)
        return element.text

    def get_auth_mail_format(self) -> str:
        element = self.get_element(self.Element.password_error_mail_format)
        return element.text

    def get_auth_mail_empty(self) -> str:
        element = self.get_element(self.Element.password_error_mail_format)
        return element.text