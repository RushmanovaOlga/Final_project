from selenium.webdriver.chrome.webdriver import WebDriver

from auth_page import AuthorizationPage
from register_page import RegistrationPage


class TestRosTeleCom:

    def test_auth_telephone_incorrect(self, driver: WebDriver):
        """Тест авторизации по телефону неверный пароль"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_telephone)
        page.set_username('9084338349')
        page.set_password('HeaHea1111\n')
        error_text = page.get_password_error_text_auth()
        assert error_text == 'Неверный логин или пароль'

    def test_auth_telephone(self, driver: WebDriver):
        """Тест авторизации по телефону"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_telephone)
        page.set_username('9084338349')
        page.set_password('HeaHea111')
        page.submit()
        assert driver.current_url.startswith('https://b2c.passport.rt.ru/account_b2c')

    def test_auth_telephone_incorrect_format(self, driver: WebDriver):
        """Тест авторизации по телефону неверный формат телефона"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_telephone)
        page.set_username('90843383')
        page.set_password('HeaHea111\n')
        error_text = page.get_auth_telephone_format()
        assert error_text == 'Неверный формат телефона'

    def test_auth_mail(self, driver: WebDriver):
        """Тест авторизации по почте"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_mail)
        page.set_username('hea007@yandex.ru')
        page.set_password('HeaHea111')
        page.submit()
        assert driver.current_url.startswith('https://b2c.passport.rt.ru/account_b2c')

    def test_auth_telephone_empty(self, driver: WebDriver):
        """Тест авторизации по телефону пустое значение телефона"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_telephone)
        page.set_username('\n')
        page.set_password('HeaHea111\n')
        error_text = page.get_auth_telephone_empty()
        assert error_text == 'Введите номер телефона'

    def test_auth_telephone(self, driver: WebDriver):
        """Тест авторизации по телефону"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_telephone)
        page.set_username('9084338349')
        page.set_password('HeaHea111')
        page.submit()
        assert driver.current_url.startswith('https://b2c.passport.rt.ru/account_b2c')

    def test_auth_mail_format(self, driver: WebDriver):
        """Тест авторизации по почте неверный формат"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_mail)
        page.set_username('hea007@yandex\n')
        error_text = page.get_auth_mail_format()
        assert error_text == 'Неверный формат адреса email'

    def test_auth_telephone(self, driver: WebDriver):
        """Тест авторизации по телефону"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_telephone)
        page.set_username('9084338349')
        page.set_password('HeaHea111')
        page.submit()
        assert driver.current_url.startswith('https://b2c.passport.rt.ru/account_b2c')

    def test_auth_mail_empty(self, driver: WebDriver):
        """Тест авторизации по пустой почте"""
        page = AuthorizationPage(driver)
        page.change_tab(AuthorizationPage.Element.tab_mail)
        page.set_username('\n')
        error_text = page.get_auth_mail_empty()
        assert error_text == 'Введите адрес, указанный при регистрации'

    def test_reg_short_password(self, driver: WebDriver):
        """Тест регистрации пароль менее 8 символов"""
        page = RegistrationPage(driver)
        page.set_password('123\n')
        error_text = page.get_password_error_text()
        assert error_text == 'Длина пароля должна быть не менее 8 символов'

    def test_reg_lower_case_password(self, driver: WebDriver):
        """Тест регистрации пароль должен содержать хотя бы одну заглавную букву"""
        page = RegistrationPage(driver)
        page.set_password('hea456-111\n')
        error_text = page.get_password_error_text()
        assert error_text == 'Пароль должен содержать хотя бы одну заглавную букву'

    def test_reg_capital_letters_password(self, driver: WebDriver):
        """Тест регистрации пароль должен содержать хотя бы одну строчную букву"""
        page = RegistrationPage(driver)
        page.set_password('HEA456-111\n')
        error_text = page.get_password_error_text()
        assert error_text == 'Пароль должен содержать хотя бы одну строчную букву'

    def test_reg_confirm_password_missmatch(self, driver: WebDriver):
        """Тест регистрации пароли не совпадают"""
        page = RegistrationPage(driver)
        page.set_password('Hea456-111\n')
        page.set_password_confirm('Ha456-111\n')
        error_text = page.get_password_confirm_error_text()
        assert error_text == 'Пароли не совпадают'

    def test_reg_confirm_password_match(self, driver: WebDriver):
        """Тест регистрации пароли совпадают"""
        page = RegistrationPage(driver)
        page.set_password('Hea456-111\n')
        page.set_password_confirm('Hea456-111\n')
        errors = page.get_password_confirm_errors()
        assert len(errors) == 0

    def test_reg_short_first_name(self, driver: WebDriver):
        """Тест регистрации имя короче 2х символов"""
        page = RegistrationPage(driver)
        page.set_first_name('Ф\n')
        error_text = page.get_first_name_error_text()
        assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_reg_long_first_name(self, driver: WebDriver):
        """Тест регистрации имя длиннее 31 символа"""
        page = RegistrationPage(driver)
        page.set_first_name(f'{"Й"*31}\n')
        error_text = page.get_first_name_error_text()
        assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_reg_non_cyrillic_first_name(self, driver: WebDriver):
        """Тест регистрации имя заполнить кириллицей"""
        page = RegistrationPage(driver)
        page.set_first_name('Andrey\n')
        error_text = page.get_first_name_error_text()
        assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_reg_short_last_name(self, driver: WebDriver):
        """Тест регистрации фамилия короче 2х символов"""
        page = RegistrationPage(driver)
        page.set_last_name('Ф\n')
        error_text = page.get_last_name_error_text()
        assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_reg_long_last_name(self, driver: WebDriver):
        """Тест регистрации фамилия длиннее 31 символа"""
        page = RegistrationPage(driver)
        page.set_last_name(f'{"Й"*31}\n')
        error_text = page.get_last_name_error_text()
        assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_reg_non_cyrillic_last_name(self, driver: WebDriver):
        """Тест регистрации фамилию заполнить кириллицей"""
        page = RegistrationPage(driver)
        page.set_last_name('Andrey\n')
        error_text = page.get_last_name_error_text()
        assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_reg_not_ru_mail(self, driver: WebDriver):
        """Тест регистрации неверный формат почты"""
        page = RegistrationPage(driver)
        page.set_email_or_telephone('hea007@yandex\n')
        error_text = page.get_mail_error_text()
        assert error_text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

    def test_reg_short_telephone(self, driver: WebDriver):
        """Тест регистрации неверный формат телефона"""
        page = RegistrationPage(driver)
        page.set_email_or_telephone('354546\n')
        error_text = page.get_telephone_error_text()
        assert error_text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'