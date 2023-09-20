from dataclasses import dataclass

from selenium.webdriver.chrome.webdriver import WebDriver

from base_page import BasePage


class RegistrationPage(BasePage):
    link = 'https://b2c.passport.rt.ru'

    def __init__(self, driver: WebDriver):
        super().__init__(driver, self.link)
        self.goto_registration_page()

    def goto_registration_page(self):
        """Перейти на страницу регистрации"""
        register_link = self.get_element(self.Element.register_link)
        register_link.click()

    @dataclass()
    class Element:
        register_link = '.login-form__register-con a'
        first_name = 'input[name="firstName"]'
        last_name = 'input[name="lastName"]'
        region_dropdown = '.register-form__dropdown .rt-input__action'
        mail_or_telephone = '.email-or-phone input'
        password = '#password'
        password_confirm = '#password-confirm'
        submit_button = 'button[name="register"]'

        first_name_error_message = '.name-container .rt-input-container:nth-child(1) .rt-input-container__meta--error'
        last_name_error_message = '.name-container .rt-input-container:nth-child(2) .rt-input-container__meta--error'
        mail_or_telephone_error_message = '.register-form__address .rt-input-container__meta--error'
        password_error_message = '.new-password-container__password .rt-input-container__meta--error'
        password_confirm_error_message = '.new-password-container__confirmed-password .rt-input-container__meta--error'

    def set_first_name(self, value: str):
        """Установить значение поля Имя"""
        element = self.get_element(self.Element.first_name)
        self.set_element_value(element, value)

    def set_last_name(self, value: str | None):
        """Установить значение поля Фамилия"""
        element = self.get_element(self.Element.last_name)
        self.set_element_value(element, value)

    def set_region(self, value: str):
        """Установить значение поля Регион"""
        dropdown_button = self.get_element(self.Element.region_dropdown)
        dropdown_button.click()

        element = self.get_element('.rt-select__list-wrapper')
        self.set_element_value(element, value)

    def set_email_or_telephone(self, value: str):
        """Установить значение поля e-mail или телефон"""
        element = self.get_element(self.Element.mail_or_telephone)
        self.set_element_value(element, value)

    def set_password(self, value: str):
        """Установить значение поля Пароль"""
        element = self.get_element(self.Element.password)
        self.set_element_value(element, value)

    def set_password_confirm(self, value: str):
        """Установить значение поля Пароль"""
        element = self.get_element(self.Element.password_confirm)
        self.set_element_value(element, value)

    def submit(self):
        """Подтвердить форму"""
        element = self.get_element(self.Element.submit_button)
        element.click()

    def get_password_error_text(self) -> str:
        element = self.get_element(self.Element.password_error_message)
        return element.text

    def get_password_confirm_error_text(self) -> str:
        element = self.get_element(self.Element.password_confirm_error_message)
        return element.text

    def get_password_confirm_errors(self):
        errors = self.get_elements(self.Element.password_confirm_error_message)
        return errors

    def get_first_name_error_text(self) -> str:
        element = self.get_element(self.Element.first_name_error_message)
        return element.text

    def get_last_name_error_text(self) -> str:
        element = self.get_element(self.Element.last_name_error_message)
        return element.text

    def get_mail_error_text(self) -> str:
        element = self.get_element(self.Element.mail_or_telephone_error_message)
        return element.text

    def get_telephone_error_text(self) -> str:
        element = self.get_element(self.Element.mail_or_telephone_error_message)
        return element.text
