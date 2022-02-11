from selenium.webdriver.common.by import By


# locators: manager/invitation/invites/

class InviteActiveLocators:
    #

    # Кнопка "Отправить приглашения"
    BTN_SEND_INVITES = (By.CSS_SELECTOR, "div.undertable button[title='Отправить приглашения'")
    # Кнопка "Удалить приглашения"
    BTN_DELETE_SELECTED = (By.CSS_SELECTOR, "div button[title='Удалить отмеченные']")
    # Кнопка "Загрузить файл"
    BTN_IMPORT_FILE = (By.XPATH, "//button[contains(text(),'Загрузить файл')]")
    # Кнопка "Добавить приглашение"
    BTN_CREATE_INVITE = (By.XPATH, "//button[contains(text(),'Добавить приглашение')]")


class Форма_Добавление_Приглашения:
    # Поле "Имя получателя
    INPUT_NAME_RECIPIENT = (By.ID, "id_name_recipient")
    INPUT_NAME_RECIPIENT = (By.ID, "id_name_recipient")
    # E-mail для отправки приглашения

    ПОЛЕ_EMAIL = (By.ID, "id_email")
    INPUT_EMAIL = (By.ID, "id_email")

    # Чек-бокс "Отправить мне копию письма"
    ЧЕК_БОКС_ОТПРАВИТЬ_МНЕ_КОПИЮ = (By.ID, "id_add_creator_to_cc")
    CHECKBOX_ADD_CREATOR_TO_CC = (By.ID, "id_add_creator_to_cc")

    # выпадающее поле "Организация"
    SELECT_LABEL_COMPANY = (By.ID, "s2id_id_company")
    ПОЛЕ_ОРГАНИЗАЦИЯ = (By.ID, "s2id_id_company")

    # Поле "Тариф"
    SELECT_LABEL_RATE = (By.ID, "s2id_id_rate")
    ПОЛЕ_ТАРИФ = (By.ID, "s2id_id_rate")

    # Поле "Тарифные опции"
    SELECT_LABEL_RATE_OPTIONS = (By.ID, "s2id_id_rate_options")
    ПОЛЕ_ТАРИФНЫЕ_ОПЦИИ = (By.ID, "s2id_id_rate_options")

    # Поле "Код доступа"
    INPUT_SECURITY_CODE = (By.ID, "id_security_code")
    ПОЛЕ_КОД_ДОСТУПА = (By.ID, "id_security_code")

    # Поле "Дата начала действия"
    INPUT_START_DATETIME = (By.ID, "start_date_datetime")
    ПОЛЕ_ДАТА_НАЧАЛА_ДЕЙСТВИЯ = (By.ID, "start_date_datetime")

    # Поле "Дата окончания действия"
    INPUT_START_DATETIME = (By.ID, "close_date_datetime")
    ПОЛЕ_ДАТА_ОКОНЧАНИЯ_ДЕЙСТВИЯ = (By.ID, "close_date_datetime")

    # кнопка "Отмена"
    BTN_CANCEL = (By.CLASS_NAME, "btn-cancel")

    # Кнопка "Добавить приглашение"
    BTN_CREATE_INVITE = (By.XPATH, "//div[@class='modal-content']//button[contains(text(),'Добавить приглашение')]")
    КНОПКА_ДОБАВИТЬ_ПРИГЛАШЕНИЕ = (
    By.XPATH, "//div[@class='modal-content']//button[contains(text(),'Добавить приглашение')]")

    # закрыть форму "Добавление приглашения" (крестик)
    BTN_CROSS_CLOSE = (
    By.CSS_SELECTOR, "div.modal-dialog.modal-lg > div.modal-content > div.modal-header > button.close")
    КНОПКА_ЗАКРЫТЬ_КРЕСТИК = (
    By.CSS_SELECTOR, "div.modal-dialog.modal-lg > div.modal-content > div.modal-header > button.close")
