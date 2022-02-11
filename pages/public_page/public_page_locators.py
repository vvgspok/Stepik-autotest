from selenium.webdriver.common.by import By


class RegisterLocators():
    # Попробовать бесплатно (2 шт на странице)
    BTN_OPEN_REGISTER = (By.CSS_SELECTOR, "a.btn.open-register-form")

    #Кнопка "Далее" - переход на следующий шаг
    BTN_STEP1_NEXT = (By.CSS_SELECTOR, '.btn.btn-success.next-step[data-step="1"]')
    BTN_STEP2_NEXT = (By.CSS_SELECTOR, '.btn.btn-success.next-step[data-step="2"]')
    BTN_STEP3_NEXT = (By.CSS_SELECTOR, '.btn.btn-success.next-step[data-step="3"]')

    #Кнопка "Назад" - 3 кнпоки. 1-ая для 2-второго шага, 2-ая для 3-его шага, 3-яя для отзывов
    BTN_PREV_STEP = (By.CSS_SELECTOR, ".btn.btn-default")
    #Кнопка "Принять" куки
    BTN_COOKIES_YES = (By.CSS_SELECTOR, ".message-btn-yes")

    # Тип организации (для формирования профиля) - обяз
    LABEL_ORGANIZATION_TYPE = (By.CSS_SELECTOR, ".subject_type_individual-group .control-label-required")
    SELECT_ORGANIZATION = (By.CSS_SELECTOR, ".form-group.required.subject_type_individual-group")
    HELPBLOCK_ORGANIZATION_TYPE = (By.CSS_SELECTOR, ".subject_type_individual-group .help-block")
    ORGANIZATION_TYPE_FORMGROUP = (By.CSS_SELECTOR, ".subject_type_individual-group")

    # ФИО
    LABEL_FULL_USERNAME = (By.CSS_SELECTOR, ".full_username-group .control-label-required")
    FULL_USERNAME_FORMGROUP = (By.CSS_SELECTOR, ".full_username-group")
    INPUT_FULL_USERNAME = (By.ID, "id_full_username")
    HELPBLOCK_FULL_USERNAME = (By.CSS_SELECTOR, ".full_username-group .error.help-block")

    # Логин
    LABEL_USERNAME = (By.CSS_SELECTOR, "label[for='id_username'] span.control-label-required")
    INPUT_USERNAME = (By.ID, "id_username")
    HELPBLOCK_USERNAME= (By.CSS_SELECTOR, ".username-group .help-block")
    USERNAME_FORMGROUP = (By.CSS_SELECTOR, ".username-group")

    # Телефон
    LABEL_PHONE = (By.CSS_SELECTOR, "label[for='id_phone'] span.control-label-required")
    INPUT_PHONE = (By.ID, "id_phone")
    HELPBLOCK_PHONE = (By.CSS_SELECTOR, ".phone-group .help-block")
    PHONE_FORMGROUP = (By.CSS_SELECTOR, ".phone-group")

    # E-mail
    LABEL_EMAIL = (By.CSS_SELECTOR, "label[for='id_email'] span.control-label-required")
    INPUT_EMAIL = (By.ID, "id_email")
    HELPBLOCK_EMAIL = (By.CSS_SELECTOR, ".email-group .help-block")
    EMAIL_FORMGROUP = (By.CSS_SELECTOR, ".email-group")
    # ИНН
    LABEL_INN = (By.CSS_SELECTOR, ".inn-group .control-label-horizontal")
    INPUT_INN = (By.ID, "id_inn")
    HELPBLOCK_INN = (By.CSS_SELECTOR, ".inn-group .error.help-block")
    INN_FORMGROUP = (By.CSS_SELECTOR, ".inn-group")
    # Регион
    LABEL_REGION = (By.CSS_SELECTOR, "label[for='id_region'] span.control-label-required")
    SELECT_REGION = (By.ID, "s2id_id_region")
    HELPBLOCK_REGION = (By.CSS_SELECTOR, ".region-group .help-block")
    REGION_FORMGROUP = (By.CSS_SELECTOR, ".region-group")
    # Сфера
    LABEL_ACTIVITY = (By.CSS_SELECTOR, "label[for='id_activity_kind'] span.control-label-required")
    SELECT_ACTIVITY = (By.ID, "s2id_id_activity_kind")
    HELPBLOCK_ACTIVITY = (By.CSS_SELECTOR, ".activity_kind-group .help-block")
    ACTIVITY_FORMGROUP = (By.CSS_SELECTOR, ".activity_kind-group")

    # "Придумайте пароль"
    LABEL_PASSWORD1 = (By.CSS_SELECTOR, "label[for='id_password1'] span.control-label-required")
    INPUT_PASSWORD1 = (By.ID, "id_password1")
    HELPBLOCK_PASSWORD1 = (By.CSS_SELECTOR, ".password1-group .help-block")
    PASSWORD1_FORMGROUP = (By.CSS_SELECTOR, ".password1-group")
    # Повторите пароль
    LABEL_PASSWORD2 = (By.CSS_SELECTOR, "label[for='id_password2'] span.control-label-required")
    INPUT_PASSWORD2 = (By.ID, "id_password2")
    HELPBLOCK_PASSWORD2 = (By.CSS_SELECTOR, ".password2-group .help-block")
    PASSWORD2_FORMGROUP = (By.CSS_SELECTOR, ".password2-group")
    # промокод
    LABEL_PROMOCODE = (By.CSS_SELECTOR, ".promocode-group label span")
    INPUT_PROMOCODE = (By.ID, "id_promocode")
    HELPBLOCK_PROMOCODE = (By.CSS_SELECTOR, ".promocode-group .help-block")
    PROMOCODE_FORMGROUP = (By.CSS_SELECTOR, ".promocode-group")

    # чек-бокс -  Я принимаю условия пользовательского соглашения
    CHECKBOX_USER_AGREEMENT = (By.ID, "id_user_agreement")
    HELPBLOCK_USER_AGREEMENT = (By.CSS_SELECTOR, ".user_agreement-group .help-block")
    USER_AGREEMENT_FORMGROUP = (By.CSS_SELECTOR, ".user_agreement-group")

    # чек-бокс - Хочу получить предзаполненный тестовыми данными профиль
    CHECKBOX_NEED_COPY_DATA = (By.ID, "id_need_copy_data")
    NEED_COPY_DATA_FORMGROUP = (By.CSS_SELECTOR, ".need_copy_data-group")
