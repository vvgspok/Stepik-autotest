
from pages.base_page import  BasePage
from collections import defaultdict
from selenium import webdriver
from common_detail_locators import CompanyCommionLocators, GISLocators,PDNLocators
'''
class Ввод_данных:
    class Общие_сведения:
        class Сведения_об_организации():
            class ИНН:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_INN).get_property("value")
            class КПП:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_KPP).get_property("value")
            class ОГРН:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_OGRN).get_property("value")
            class Основной_вид_деятельности:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_PRIMARY_OKVED).text
            class Дополнительный_вид_деятельности:
                def Получить(self):
                    return BasePage.select2_chooices_parse(self.browser.find_elements(*CompanyCommionLocators.CommonInformationLocators.COMMON_ADDITIONAL_OKVED))
            class Краткое_наименование_организации:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_SHORT_NAME).get_property("value")
            class Полное_наименование_организации:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_FULL_NAME).get_property("value")
            class Условное_сокращение:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_SYMBOL).get_property("value")
            class Тип_организации:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_KIND).text
            class Наименование_и_реквизиты_учредительного_документа:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_CHARTER).get_property("value")
            class Лицензия_на_вид_деятельности:
                def Получить(self):
                    return BasePage.select2_chooices_parse(self.browser.find_elements(*CompanyCommionLocators.CommonInformationLocators.COMMON_LIC))
            class Есть_официальный_сайт:
                def Получить(self):
                    checkbox = self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_WEB_SITE_CHECKBOX)
                    return BasePage.checkbox_get_state(checkbox)
            class Населённый_пункт:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_LOCALCITY).get_property("value")
            class Юридический_адрес:
                class Индекс:
                    def Получить(self):
                        return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_UR_INDEX).get_property("value")
                class Адрес:
                    def Получить(self):
                        return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_UR_ADDRESS).get_property("value")
            class Фактический_адрес:
                class Индекс:
                    def Получить(self):
                        return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_FACT_INDEX).get_property("value")
                class Адрес:
                    def Получить(self):
                        return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_FACT_ADDRESS).get_property("value")
            class Почтовый_адрес:
                class Индекс:
                    def Получить(self):
                        return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_MAIL_INDEX).get_property("value")
                class Адрес:
                    def Получить(self):
                        return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_MAIL_ADDRESS).get_property("value")
            class Адрес_электронной_почты:
                def Получить(self):
                    return self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_EMAIL).get_property("value")
            class Есть_структурное_подразделение:
                def Получить(self):
                    checkbox = self.browser.find_element(*CompanyCommionLocators.CommonInformationLocators.COMMON_HAS_DEPARTAMENTS_CHECKBOX)
                    return BasePage.checkbox_get_state(checkbox)

            def Получить(self):
                # Юр.лицо. Добавить обраюотку физика
                tab = Ввод_данных.Общие_сведения.Сведения_об_организации
                common_information = defaultdict(dict)
                common_information["ИНН"] = tab.ИНН.Получить(self)
                common_information["КПП"] = tab.КПП.Получить(self)
                common_information["ОГРН"] = tab.ОГРН.Получить(self)
                common_information["Основной вид деятельности"]= tab.Основной_вид_деятельности.Получить(self)
                common_information["Дополнительный вид деятельности"] = tab.Дополнительный_вид_деятельности.Получить(self)
                common_information["Краткое наименование организации"]=   tab.Краткое_наименование_организации.Получить(self)
                common_information["Полное наименование организации"]=  tab.Полное_наименование_организации.Получить(self)
                common_information["Условное сокращение"]= tab.Условное_сокращение.Получить(self)
                common_information["Тип организации"]= tab.Тип_организации.Получить(self)
                common_information["Наименование и реквизиты учердительного документа"]=  tab.Наименование_и_реквизиты_учредительного_документа.Получить(self)
                common_information["Лицензия на вид деятельности"]=  tab.Лицензия_на_вид_деятельности.Получить(self)
                common_information["Есть официальный сайт"]= tab.Есть_официальный_сайт.Получить(self)
                common_information["Населённый пункт"] = tab.Населённый_пункт.Получить(self)
                common_information["Юриридический адрес"]["Индекс"] = tab.Юридический_адрес.Индекс.Получить(self)
                common_information["Юриридический адрес"]["Адрес"] = tab.Юридический_адрес.Адрес.Получить(self)
                common_information["Фактический адрес"]["Индекс"] = tab.Фактический_адрес.Индекс.Получить(self)
                common_information["Фактический адрес"]["Адрес"] = tab.Фактический_адрес.Адрес.Получить(self)
                common_information["Почтовый адрес"]["Индекс"] = tab.Почтовый_адрес.Индекс.Получить(self)
                common_information["Почтовый адрес"]["Адрес"] = tab.Почтовый_адрес.Адрес.Получить(self)
                common_information["Адрес электронной почты"] = tab.Адрес_электронной_почты.Получить(self)
                common_information["Есть структурное подразделение"]= tab.Есть_структурное_подразделение.Получить(self)
                return common_information
        class Бизнец_процессы():
            def Получить(self):
                return BasePage.get_table(self, *CompanyCommionLocators.CompanyBusinessProcessesLocators.BUSINESS_PROCESSES_TABLE)

        class Цели_и_способы_обработки_информации():
            #Способы эксплуатации. ПДн обрабатываются на бумажных носителях. Состояние
            class Способы_Эксплуатации():
                class ПДН_обрабатываются_на_бумажных_носителях():
                    def Получить(self):
                        checkBox = self.browser.find_element(*CompanyCommionLocators.CompanyAimsLocators.PAPER_PROCESSING_CHECKBOX)
                        return BasePage.checkbox_get_state(checkBox)

                    def Установить(self, value):
                        state = Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Способы_Эксплуатации.ПДН_обрабатываются_на_бумажных_носителях.Получить(self)
                        if (state != value):
                            self.browser.find_element_(*CompanyCommionLocators.CompanyAimsLocators.PAPER_PROCESSING_CHECKBOX).click()
                class Информация_обрабатывается_с_использованием_компьютерной_техники():
                     # Способы эксплуатации. Информация обрабатывается с использованием компьютерной техники . Состояние
                    def Получить(self):
                        checkbox = self.browser.find_element(*CompanyCommionLocators.CompanyAimsLocators.SOFTWARE_PROCESSING_CHECKBOX)
                        return BasePage.checkbox_get_state(checkbox)
                    def Установить(self,value):
                            state = Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Способы_Эксплуатации.Информация_обрабатывается_с_использованием_компьютерной_техники.Получить(self)
                            if (state != value):
                                self.browser.find_element(*CompanyCommionLocators.CompanyAimsLocators.SOFTWARE_PROCESSING_CHECKBOX).click()
            class Вид_эксплуатируемых_информационных_систем():
                class Государственные_ГИС():
                    def Получить(self):
                        raddio = self.browser.find_element(*CompanyCommionLocators.CompanyAimsLocators.CURRENT_USED_SYSTEMS_GIS)
                        if raddio.find_element_by_css_selector("input").get_attribute("checked"):
                            state = "True"
                        else:
                            state = "False"
                        return state
                    def Установить(self):
                        if (Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Вид_эксплуатируемых_информационных_систем.Государственные_ГИС.Получить(self) == "False"):
                            self.browser.find_element(*CompanyCommionLocators.CompanyAimsLocators.CURRENT_USED_SYSTEMS_GIS).click()
                class Муниципальные_МИС():
            #Вид эксплуатируемых информационных систем. Муниципаальные (МИС). Состояние
                    def Получить(self):
                        raddio = self.browser.find_element(*CompanyCommionLocators.CompanyAimsLocators.CURRENT_USED_SYSTEMS_MIS)
                        if raddio.find_element_by_css_selector("input").get_attribute("checked"):
                            state = "True"
                        else:
                            state = "False"
                        return state
                    def Установить(self):
                        if (Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Вид_эксплуатируемых_информационных_систем.Муниципальные_МИС.Получить(self) == "False"):
                            self.browser.find_element(*CompanyCommionLocators.CompanyAimsLocators.CURRENT_USED_SYSTEMS_MIS).click()
            class Цели_обработки_информации():
                def Получить(self):
                    return BasePage.get_table(self,*CompanyCommionLocators.CompanyAimsLocators.AIMS_TABLE)
            def Получить(self):
                aims = defaultdict(dict)
                try:
                    aims["ПДн обрабатываются на бумажных носителях"] = Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Способы_Эксплуатации.ПДН_обрабатываются_на_бумажных_носителях.Получить(self)
                except:
                    pass
                try:
                    aims["Информация обрабатывается с использованием компьютерной техники"] = Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Способы_Эксплуатации.Информация_обрабатывается_с_использованием_компьютерной_техники.Получить(self)
                except:
                    pass
                try:
                    aims["Ввид эксплуатируемых информационных систем"]["Государственные (ГИС)"] = Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Вид_эксплуатируемых_информационных_систем.Государственные_ГИС.Получить(self)
                except:
                    pass
                try:
                    aims["Ввид эксплуатируемых информационных систем"]["Муниципальные (МИС)"] = Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Вид_эксплуатируемых_информационных_систем.Муниципальные_МИС.Получить(self)
                except:
                    pass
                try:
                    aims["Цели обработки информации"] = Ввод_данных.Общие_сведения.Цели_и_способы_обработки_информации.Цели_обработки_информации.Получить(self)
                except:
                    pass
                return aims
        class Структура_организации():
            def Получить(self):
                  return BasePage.get_table(self, *CompanyCommionLocators.CompanyStructureLocators.STRUCTURE_TABLE)
        class Перечень_программных_комплексов():
            class Перечень_программных_комплексов():
                def Получить(self):
                    BasePage.is_element_present(self, *CompanyCommionLocators.CompanySoftwareLocators.AIMS_DETAILS_TABLE)
                    return BasePage.get_table(self, *CompanyCommionLocators.CompanySoftwareLocators.AIMS_DETAILS_TABLE)
            class Сотрудники_имееют_доступ_к_программным_комплексам_других_организаций():
                 def Получить(self):
                     checkbox = self.browser.find_element(*CompanyCommionLocators.CompanySoftwareLocators.USER_ACCESS_CHECKBOX)
                     return BasePage.checkbox_get_state(checkbox)
            class Программные_комплексы_других_организаций():
                def Получить(self):
                    return BasePage.get_table(self, *CompanyCommionLocators.CompanySoftwareLocators.EXTERNAL_SOFTWARE_TABLE)
            def Получить(self):
                software = defaultdict(dict)
                software["aims_details"] = Ввод_данных.Общие_сведения.Перечень_программных_комплексов.Перечень_программных_комплексов.Получить(self)
                software["user_access"] = Ввод_данных.Общие_сведения.Перечень_программных_комплексов.Сотрудники_имееют_доступ_к_программным_комплексам_других_организаций.Получить(self)
                if (software["user_access"]=="True"):
                    software["external_software"] = Ввод_данных.Общие_сведения.Перечень_программных_комплексов.Программные_комплексы_других_организаций.Получить(self)
                return software
        class Помещения_и_хранилища:
            class Помещения():
                def Получить(self):
                    return BasePage.get_table(self, *CompanyCommionLocators.CompanyRoomsVaultsLocators.ROOMS_TABLE)
            class Хранилища():
                def Получить(self):
                    return BasePage.get_table(self, *CompanyCommionLocators.CompanyRoomsVaultsLocators.VAULT_TABLE)
        class Общие_сведения_о_системах():
            def Получить(self):
                return BasePage.get_table(self, *CompanyCommionLocators.CompanyInfoSystemsLocators.INFOSYSTEMS_TABLE)
        class Сотрудники_организации():
            def Получить(self):
                return BasePage.get_table(self, *CompanyCommionLocators.CompanyEmployeesLocators.EMPLOYEES_TABLE)
    class ГИС:
        class Характеристики_ПК_входящих_в_состав_ГИС():
            def Получить(self):
                return BasePage.get_table(self, *GISLocators.GisSoftWareLocators.GIS_SOFTWARE_TABLE)
        class Перечень_помещений_с_обработкой_информации():
            class Перечень_помещений_в_которых_размещены_ГИС():
                def Получить(self):
                    return BasePage.get_table(self, *GISLocators.GisRoomAccessLocators.GIS_ROOMS_TABLE)
            class Перечень_помещений_в_которых_размещены_программные_комплексы_дургих_организаций():
                def Получить(self):
                    return BasePage.get_table(self, *GISLocators.GisRoomAccessLocators.GIS_SOFT_ROOMS_TABLE)
            class Порядок_доступа():
                def Получить(self):
                    raddio = self.browser.find_element(*GISLocators.GisRoomAccessLocators.GIS_ACCESS_OWN_DESCRIPTION_GROUP)
                    if raddio.find_element_by_css_selector("input").get_attribute("checked"):
                        state = "Использовать типовое описание порядка доступа"
                    else:
                        state = "Использовать собственное описание порядка доступа"
                    return state
        class Перечень_лиц_допущенных_к_обработке_информации_в_ГИС():
            class Параметры_доступ:
                def Получить(self):
                    raddio = self.browser.find_element(*GISLocators.GisUsersAccessLocators.GIS_ACCESS_DESCRIPTION_GROUP)
                    if raddio.find_element_by_css_selector("input").get_attribute("checked"):
                        state = "Доступ к программным комплексам, входящих в ГИС"
                    else:
                        state = "Доступ к ГИС в целом"
                    return state
            class Перечень_лиц_имеющих_доступ_к_ГИС:
                def Получить(self):
                    return  BasePage.get_table(self,*GISLocators.GisUsersAccessLocators.GIS_USER_ACCESS_TABLE)
            class Перечень_лиц_имеющих_доступ_к_программным_комплексам_других_организаций:
                def Получить(self):
                    return BasePage.get_table(self, *GISLocators.GisUsersAccessLocators.GIS_USER_EXTERNAL_ACCESS_TABLE)
        class Особенности_обработки_информации():
            class Наименование_территориального_органа_ФСТЭК_России():
                def Получить(self):
                    element = self.browser.find_element(*GISLocators.GisFeaturesProcessingLocators.GIS_FSTEK_TERRITORIAL_AUTHORITY)
                    return  BasePage.get_select(element)


            class Руководитель_Управления_ФСТЭК_России():
                def Получить(self):
                    return self.browser.find_element(*GISLocators.GisFeaturesProcessingLocators.GIS_FSTEK_TERRITORIAL_AUTHORITY_CHEIF).get_property("value")

    class ПДН:
        class Характеристики_ПК_входящие_в_состав_ИСПДН:
            def Получить(self):
                return BasePage.get_table(self,*PDNLocators.PDNSoftWareLocators.PDN_SOFTWARE_TABLE)

        class Особенности_неавтоматизированной_обработки_ПДН:
            def Получить(self):
                return BasePage.get_table(self,*PDNLocators.PDNAimsCategoryLocators.PDN_AIMS_CATEGORY_TABLE)

        class Перечень_помещений_с_обработкой_ПДН:
            class Перечень_помещений_в_которых_размещены_ИСПДН:
                def Получить(self):
                    return BasePage.get_table(self,*PDNLocators.PDNRoomsAccess.PDN_ROOMS_DYNAMIC_TABLE)

            class Уровень_детализации:
                def Получить(self):
                    element = self.browser.find_element(*PDNLocators.PDNRoomsAccess.PDN_ROOM_DETAIL_LEVEL_RADDIOBUTTON)
                    return BasePage.get_raddiobutton_state(element)

            class Перечень_помещений_в_которых_хранятся_материальные_носители_ПДн:
                def Получить(self):
                    return  BasePage.get_table(self,*PDNLocators.PDNRoomsAccess.PDN_SUBJECT_CATEGORY_PDN_ROOMS_TABLE)

            class Перечень_помещений_в_которых_размещены_прогрммные_комплексы_других_организаций:
                def Получить(self):
                    return BasePage.get_table(self,*PDNLocators.PDNRoomsAccess.PDN_EXTERNAL_SOFT_DYNAMIC_TABLE)
            class Порядок_доступа:
                def Получить(self):
                    element = self.browser.find_element(*PDNLocators.PDNRoomsAccess.PDN_ACCESS_DESRIPTION_RADDIOBUTTON)
                    return BasePage.get_raddiobutton_state(element)

        class Перечень_лиц_допущенных_к_обработке_ПДН:
            class Перечень_доступа:
                def Получить(self):
                    element = self.browser.find_element(*PDNLocators.PDNUserAccess.PDN_GET_ACCESS_RADIIOBUTTON)
                    return BasePage.get_raddiobutton_state(element)

            class Перечень_лиц_имеющих_доступ_к_ПДН:
                def Получить(self):
                    return BasePage.get_table(self,*PDNLocators.PDNUserAccess.PDN_USER_ACCESS_TABLE)
            class Перечень_лиц_имеющих_доступ_к_программным_комплексам_других_организаций:
                def Получить(self):
                    return BasePage.get_table(self,*PDNLocators.PDNUserAccess.PDN_USER_EXTERNAL_ACCESS_TABLE)
            class Перечень_лиц_отвественных_за_хранение_материальных_носителей_ПДн:
                def Получить(self):
                    return BasePage.get_table(self,*PDNLocators.PDNUserAccess.PDN_STORAGE_RESPOSIBLE_EMPLOYESS_TABLE)


        class Обезличивание_ПДН:
            class Обезличивание_ПДН:
                def Получить(self):
                    element = self.browser.find_element(*PDNLocators.PDNDepersonalization.PDN_DEPERSONALIZATIOND_RADDIOBUTTON)
                    return BasePage.get_raddiobutton_state(element)

            class Должности_ответственных_за_обезличивание_ПДн:
                def Получить(self):
                    return  BasePage.get_table(self,*PDNLocators.PDNDepersonalization.PDN_DEPERSONALIZATIOND_TABLE)

        class Особенности_обработки_ПДн:
            class Подано_уведомление_об_обработке_ПД_в_Роскомнадзор:
                def Получить(self):
                    element = self.browser.find_element(*PDNLocators.PDNProcessing.PDN_POSTED_NOTIFICATION_CHECKBOX)
                    return BasePage.checkbox_get_state(element)

            class Регистрационный_номер_в_Реестре_операторов_ПДн:
                def Получить(self):
                    return self.browser.find_element(*PDNLocators.PDNProcessing.PDN_REGISTRATION_NUMBER).text

            class Наименование_территориального_органа_Роскомнадзора:
                def Получить(self):
                    text =  "Управление Федеральной службы по надзору в сфере связи, информационных технологий и массовых коммуникаций по "
                    element = self.browser.find_element(*PDNLocators.PDNProcessing.PDN_AGENCY_NAME)
                    return text+BasePage.select2_chooices_parse(element)

            class Регионы_в_которых_осуществляется_обработка_ПДн:
                def Получить(self):
                    element = self.browser.find_element(*PDNLocators.PDNProcessing.PDN_PERSONAL_DATA_PROCESSING_REGIONS_ALL_CHECKBOX)
                    return  BasePage.checkbox_get_state(element )

            class Дата_начала_обработки_ПДн:
                def Получить(self):
                    pass

            class Организация_предоставляет_государственные_муниципальные_услуги:
                def Получить(self):
                    pass

            class Осуществляется_обработка_персональных_данных_в_целях_продвижения_товаров_работ_услуг_на_рынке_а_также_в_целях_политической_агитации:
                def Получить(self):
                    pass

            class Осуществляется_принятие_на_основании_исключительно_автоматизированной_обработки_персональных_данных_решений_порождающих_юридические_последствия_в_отношении_субъекта_персональных_данных_или_иным_образом_затрагивающих_его_права_и_законные_интересы:

                def Получить(self):
                    pass

            class Используется_система_видеонаблюдения:
                def Получить(self):
                    pass

            class В_общедоступных_источниках_ПДн_организации_обрабатываются_ПДн_несовершеннолетних:
                pass
            class Поручается_обработка_персональных_данных:
                def Получить(self):
                    pass
            class Введен_пропускной_режим_на_территорию_Оператора:
                def Получить(self):
                    pass
            class Осуществляется_трансграничная_передача_персональных_данных:
                def Получить(self):
                    pass
        class Сведения_о_месте_нахождения_базы_данных_информации_содержащей_ПДн_граждан_РФ:
            def Получить(self):
                pass

        class Оценка_вреда:
            pass

        class Перечень_помещений_в_которых_установлены_видеокамеры:
            pass

        class Перечень_должностей_имеющих_доступ_к_системе_видеонаблюдения:
            def Получить(self):
                pass

        class Использование_официального_сайта:
            pass





    # Заглушки
    class КИИ:
        pass
    class Ответственные:
        pass
    class Информационные_технологии:
        pass
    class Эксплуатация_криптосредств:
        pass
    class Дополнительно:
        pass
'''
