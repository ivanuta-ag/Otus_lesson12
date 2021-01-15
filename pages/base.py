from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from locators.locators import CommonPageLocators


class BasePage(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def check_cart(self):
        assert self.is_element_present(*CommonPageLocators.CART), 'Отсутствует корзина'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to(self):
        return self.driver.get(self.base_url)
