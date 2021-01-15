from .base import BasePage
from locators.locators import AdminLocators, CommonPageLocators
from selenium.common.exceptions import TimeoutException


class AdminPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    def wait_for_download(self):
        try:
            self.find_element(locator=AdminLocators.LOGIN_TEXT)
        except TimeoutException:
            print('Страница не загружена')

    def check_login_text(self):
        assert self.find_element(locator=AdminLocators.LOGIN_TEXT), "Некорректный текст с просьбой залогиниться"

    def check_input_username(self):
        assert self.is_element_present(*AdminLocators.INPUT_USERNAME), "Отсутствует поле ввода логина"

    def check_login_field(self):
        assert self.is_element_present(*AdminLocators.LOGIN), "Отсутствует поле E-Mail Address"

    def check_input_password(self):
        assert self.is_element_present(*CommonPageLocators.INPUT_PASSWORD), "Отсутствует поле Password"

    def check_help_block(self):
        assert self.is_element_present(*AdminLocators.HELP_BLOCK), "Отсутствует help-block"

    def check_login(self):
        self.find_element(locator=AdminLocators.LOGIN).click()
        assert self.is_element_present(*AdminLocators.USER_PROFILE), 'Пользователь не залогинен'

    def check_logout(self):
        self.find_element(locator=AdminLocators.LOGOUT).click()
        assert self.is_element_present(*AdminLocators.LOGIN_TEXT), "Не появился текст с просьбой залогиниться"

    def table_responsive(self):
        self.find_element(locator=AdminLocators.PARENT_COLLAPSE).click()
        self.find_element(locator=AdminLocators.PRODUCTS_CATALOG).click()

        self.is_element_present(*AdminLocators.TABLE_RESPONSIVE), 'Пользователь не залогинен'
