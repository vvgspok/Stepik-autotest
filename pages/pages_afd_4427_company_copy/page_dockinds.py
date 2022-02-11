import allure

from pages.base_page import BasePage
from .locators_dockinds import DockindsLocators


@allure.epic("Сравнение настроек оформления")
class DockindsPage(BasePage):

    @allure.story("Проверка синей плашки")
    def сравнение_настроек_поверхностое(self):
        edit_containers = self.browser.find_elements(*DockindsLocators.EDIT_CONTAINER)

        edit_containers = 2
