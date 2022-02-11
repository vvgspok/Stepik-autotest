from selenium.webdriver.common.by import By

from manager.manager_base import МенеджерСайта
from pages.base_page import BasePage
from pages.manager.clients.invitation.active.invite_active_locators import InviteActiveLocators


# page: manager/invitation/invites/

class InviteActivePage(BasePage):

    def check_elements_форма_добавления_приглашения(self):
        # Предусловие: страница с приглашениями открыта (вкладка "создано")"
        BasePage.проверка_обновления(self)
        BasePage.ожидание_прогрузки_страницы(self)

        # 1. Нажать "Добавить приглашение"
        кнопка_добавить_приглашение = InviteActiveLocators.BTN_CREATE_INVITE
        self.нажать(кнопка_добавить_приглашение)

        # form_create_invite = BasePage.ModalWindow.searchByHeaderText(self, "Добавление приглашения")
        # data = BasePage.get_data_from_window(self, form_create_invite)

        pass

    def перейти_в_приглашения(self):
        менеджер_сайта = МенеджерСайта(self.browser)
        менеджер_сайта.Перейти_в_раздел("Клиенты")
        менеджер_сайта.Перейти_на_шаг("Приглашения")
        self.проверка_вкладок_приглашения_при_1ом_заходе()

    def проверка_вкладок_приглашения_при_1ом_заходе(self):
        try:
            # По умолчанию сразу
            active = "СОЗДАНО"
            other = ["ОЖИДАЕТ АКТИВАЦИИ", "АКТИВИРОВАНО", "ЗАБЛОКИРОВАНО"]

            # Поиск на странице вкладок
            active_tab = self.browser.find_elements_by_css_selector(".basics-tab.active")
            other_tabs = self.browser.find_elements_by_css_selector(".company-rate-tab")
            for i in range(len(other_tabs)):
                other_tabs[i] = other_tabs[i].text

            # Проверка активной вкладки
            active_tab = active_tab[0].text
            assert active_tab == active, f"Активная вкладка определена неверно \n" \
                                         f"В функции: {active},\n" \
                                         f"на странице: {active_tab}\n"
            # Проверка Неактивной вкладки
            assert other == other_tabs, f"есть несооответствие неактивных вкладок"
        except Exception as e:
            assert False, f"Ошибка при проверке вкладок \n" \
                          f"Exception: {e}"

    def проверка_наличия_элементов_создано(self):
        BasePage.ожидание_прогрузки_страницы(self)

        tab_content = self.browser.find_element(By.CLASS_NAME, "tab-content")

        BasePage.найти_элементы_на_странице.строка_поиска(self, tab_content)
        BasePage.найти_элементы_на_странице.кнопка_скрытие_столбцов(tab_content)
        BasePage.найти_элементы_на_странице.таблица(tab_content)

    def сравнивалка(self, input1, input2):
        assert input1 == input2, f"{input1}!={input2}"

    def нажать(self, el):
        try:
            self.browser.find_element(*el).click()
            BasePage.ожидание_прогрузки_страницы(self)
        except Exception as e:
            print(e)

    def delete_selected_invite_active_page(self):
        """
        Удаление выбранных приглашений на вкладке "Создано"
        """
        pass

    def send_selected_invite_active_page(self):
        """
        Отправка выделенных приглашений на вкладке "Создано"
        """
        pass

    def import_file_active_page(self):
        pass

    def create_invite(self):
        pass

    def validation_check(self):
        """
        Проверка валидации
        :param Проверяемое поле
        :return: Текст валидации
        """
        pass

    def ввести_имя_отчество_получателя(self, name=""):
        pass

    def ввести_email(self, mail):
        pass

    def выбрать_тариф(self, tarif):
        pass

    def выбрать_организацию(self, org):
        pass

    def чек_бокс_копия_письма(self, default=True):
        pass

    def выбрать_тарифную_опцию(self, option):
        pass

    def ввести_код_доступа(self, kod=""):
        pass

    def выбрать_дата_начала_действия(self, date):
        pass

    def выбрать_дата_окочания_действия(self, date):
        pass
