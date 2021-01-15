from .base import BasePage
from locators.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    def wait_for_download(self):
        try:
            self.find_element(locator=MainPageLocators.HEART)
        except TimeoutException:
            print('Страница не загружена')

    def check_wish_list(self):
        assert self.find_element(locator=MainPageLocators.HEART), 'Отсутствует wish list'

    def check_len_menu_items(self):
        len_menu_items = len(self.find_elements(locator=MainPageLocators.NAVBAR_1))
        assert len_menu_items == 8, 'Неверное количество элементов меню'

    def navbar(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR_2), 'Отсутствует navbar'

    def check_logo(self):
        assert self.is_element_present(*MainPageLocators.LOGO), 'Отсутствует logo'
