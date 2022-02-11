import allure

from pages.afd_5840_knowledge.knowledge_functions import *
from pages.base_page import BasePage
from pages.main_functions import проверка_ссылки, screen_allure
from pages.main_settings import MAIN_URL
from .knowledge_locators import KnowledgeLocators


@allure.epic("Прверка БЗ")
class KnowledgePageBeforeMoving(BasePage):

    @allure.story("Проверка синей плашки")
    def есть_синяя_плашка(self, data):
        if not self.is_element_present(*KnowledgeLocators.HELP_CONTAINER):
            self.attach_screenshot("Проверка синей плашки (БЗ)", "Нет синей плашки (или Отсутствует статья)")
            assert False, f"Нет синей плашки (или Отсутствует статья) " \
                          f"\n {data}" \
                          f"\n {data.get('name')}" \
                          f"\n {data.get('link_page')}"

    @allure.story("Проверка наличия текста в синей плашке")
    def есть_текст_в_плашке(self):
        assert self.is_element_present(
            *KnowledgeLocators.HELP_TEXT), "Нет текста в синей плашке"

    @allure.story("Проверка наличия кнопки для 'Перехода в Базу знаний'")
    def ссылка_в_синей_плашке(self):
        if not self.is_element_present(*KnowledgeLocators.HELP_LINK):
            self.attach_screenshot("Проверка наличия кнопки для 'Перехода в Базу знаний'", " - ")
            assert False, "Не найдена кнопка для 'Перехода в Базу знаний'"

    @allure.story("Проверка ссылки в кнопке")
    def работоспособность_ссылки_в_кнопке_бз(self, data, тариф_для_проверки):
        """
        + проверка соответствия ссылки для перехода в БЗ с json
        + проверка запроса на ссылку (ожидается 200)
        """
        bttn_help_link = self.browser.find_element(*KnowledgeLocators.HELP_LINK)
        help_link = bttn_help_link.get_attribute("href")
        data_tariff = data.get(тариф_для_проверки)
        help_link_in_json = (MAIN_URL + data_tariff.get("link_bz")).strip()

        if help_link == help_link_in_json:
            for_assert = True
        elif help_link != help_link_in_json:
            for_assert = False
            messege = f"Cсылка в кнопке не совпадает с json (link_bz)\n" \
                      f"{help_link}\n" \
                      f"{help_link_in_json}\n" \
                      f"{data}"

            переход_на_вкладку_с_БЗ(self.browser, KnowledgeLocators.HELP_LINK)
            # Делаем скрин БЗ (если смогли перейти и ничего ранее не упало)
            screen_allure(self.browser, "Страница БЗ")

        assert for_assert == True, messege
        проверка_ссылки(help_link)

    @allure.story("Проверка заголовка в БЗ с json")
    def переход_в_базу_знаний(self, data, тариф_для_проверки):
        """
        + проверка заголовка в БЗ с json
        + проверка заголовка с шагом с БЗ (если step_page)

        """
        type_page = data.get("type_page")
        need_data = data.get(тариф_для_проверки)

        # self.проверка_наличия_тарифа_в_хлебной_крошке(тариф_для_проверки)

        self.browser, zagolovok_in_knowledge = self.проверить_заголовок_в_базе_знаний_с_заголовком_в_json(self.browser,
                                                                                                          need_data,
                                                                                                          тариф_для_проверки)

        # если проверка заго    ловка сильно мешает
        if type_page == "step_page":
            need_text = получить_заголовок_до_перехода_в_базу_знаний(self.browser, KnowledgeLocators)
            self.проверить_заголовок_в_базе_знаний_с_шагом_на_странице(need_text, zagolovok_in_knowledge)

        self.проверить_список_страниц_этого_раздела()

    @allure.story("Проверка_наличия_тарифа_в_хлебной_крошке")
    def проверка_наличия_тарифа_в_хлебной_крошке(self, тариф_для_проверки):
        BREAD_CRUMBS = self.browser.find_element(*KnowledgeLocators.BREAD_CRUMBS)
        BREAD_CRUMBS = BREAD_CRUMBS.text.lower()
        тариф = тариф_для_проверки.lower()
        assert тариф in BREAD_CRUMBS, f"{тариф} не найден в {тариф_для_проверки}"

    def проверить_заголовок_в_базе_знаний_с_шагом_на_странице(self, need_text, zagolovok_in_knowledge):
        pass
        # assert need_text in zagolovok_in_knowledge, \
        #     f"Заголовок в БЗ не совпадает с полученным результатом:\n " \
        #     f"{need_text} \n {zagolovok_in_knowledge}"

    def проверить_заголовок_в_базе_знаний_с_заголовком_в_json(self, browser, data, тариф_для_проверки):
        zagolovok_in_knowledge_in_json = data.get("zagolovok_in_knowledge")
        browser, current_window = переход_на_вкладку_с_БЗ(browser, KnowledgeLocators.HELP_LINK)

        # Делаем скрин БЗ (если смогли перейти и ничего ранее не упало)
        # screen_allure(self.browser, "Страница БЗ")

        if not self.is_element_present(*KnowledgeLocators.ZAGOLOVOK_IN_KNOWLEDGE):
            self.attach_screenshot("Проверка заголовка в базе знаний", " - ")
            assert False, "Нет заголовка в базе знаний \n " + f"{KnowledgeLocators}"
        zagolovok_in_knowledge = получить_заголовок_в_базе_знаний(browser, KnowledgeLocators.ZAGOLOVOK_IN_KNOWLEDGE)
        assert zagolovok_in_knowledge == zagolovok_in_knowledge_in_json, \
            f"заголовок в БЗ и json не совпадают: \n" \
            f"{zagolovok_in_knowledge}\n" \
            f"{zagolovok_in_knowledge_in_json}" \
            f"\n{data}"

        # временное решение
        self.проверка_наличия_тарифа_в_хлебной_крошке(тариф_для_проверки)
        browser.close()
        browser.switch_to.window(current_window)
        return browser, zagolovok_in_knowledge

    @allure.story("Проверка списка страниц в разделе БЗ")
    def проверить_список_страниц_этого_раздела(self):
        pages = self.browser.find_elements(*KnowledgeLocators.PAGES_THIS_RAZDEL)
        for page in pages:
            link = page.get_attribute("href")
            проверка_ссылки(link)
