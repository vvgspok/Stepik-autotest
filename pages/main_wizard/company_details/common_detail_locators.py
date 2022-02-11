from selenium.webdriver.common.by import By


class CompanyCommionLocators:
    class CommonInformationLocators():
        ### Шаг "Сведения об организации"
        # ИНН
        COMMON_INN = (By.CSS_SELECTOR, "#id_inn")
        # КПП
        COMMON_KPP = (By.CSS_SELECTOR, "#id_kpp")
        # ОГРН
        COMMON_OGRN = (By.CSS_SELECTOR, "#id_ogrn")
        # Основной вид деятельности
        COMMON_PRIMARY_OKVED = (By.CSS_SELECTOR, "#s2id_id_primary_okved .select2-choice .select2-chosen")  # .text
        # Дополнительный вид деятельности
        COMMON_ADDITIONAL_OKVED = (
        By.CSS_SELECTOR, "#s2id_id_additional_okved .select2-choices .select2-search-choice div")  # .text
        # Краткое наименование организации
        COMMON_SHORT_NAME = (By.CSS_SELECTOR, "#id_short_name_0")  # .get_property("value")
        # Полное наименование организации
        COMMON_FULL_NAME = (By.CSS_SELECTOR, "#id_full_name_0")  # .get_property("value")
        # Условное сокращение
        COMMON_SYMBOL = (By.CSS_SELECTOR, "#id_symbol_0")  # .get_property("value")
        # Тип организации
        COMMON_KIND = (By.XPATH, '//select[@id="id_kind"]//option[@selected]')  # .text
        # Наименование и реквизиты учредительного документа
        COMMON_CHARTER = (By.CSS_SELECTOR, "#id_charter")  # .get_property("value")
        # Лицензии на вид деятельности
        COMMON_LIC = (By.CSS_SELECTOR, "#s2id_id_activity_licenses .select2-choices .select2-search-choice div")
        # Есть веб-сайт
        COMMON_WEB_SITE_CHECKBOX = (By.CSS_SELECTOR, "#id_has_website")
        # Населённый пункт
        COMMON_LOCALCITY = (By.CSS_SELECTOR, "#id_locality")
        # Юридический адрес
        COMMON_UR_INDEX = (By.CSS_SELECTOR, ".input-group #id_legal_address_0")
        COMMON_UR_ADDRESS = (By.CSS_SELECTOR, ".input-group #id_legal_address_1")
        # Фактический адрес
        COMMON_FACT_INDEX = (By.CSS_SELECTOR, ".input-group #id_actual_address_0")
        COMMON_FACT_ADDRESS = (By.CSS_SELECTOR, ".input-group #id_actual_address_1")
        # Почтовый адрес
        COMMON_MAIL_INDEX = (By.CSS_SELECTOR, ".input-group #id_mailing_address_0")
        COMMON_MAIL_ADDRESS = (By.CSS_SELECTOR, ".input-group #id_mailing_address_1")
        # Адрес электронной почты
        COMMON_EMAIL = (By.CSS_SELECTOR, "#id_email")
        # Есть структурное подразделение
        COMMON_HAS_DEPARTAMENTS_CHECKBOX = (By.CSS_SELECTOR, "#id_has_departments")
    class CompanyBusinessProcessesLocators():
        BUSINESS_PROCESSES_TABLE = (By.CSS_SELECTOR,".business-processes-table.table")
    class CompanyAimsLocators():
        PAPER_PROCESSING_CHECKBOX = (By.CSS_SELECTOR, ".paper_processing-group .checkbox label input")
        SOFTWARE_PROCESSING_CHECKBOX = (By.CSS_SELECTOR, ".software_processing-group .checkbox label input")
        CURRENT_USED_SYSTEMS_GROUP = (By.CSS_SELECTOR,".form-group.current_used_systems-group")
        CURRENT_USED_SYSTEMS_GIS = (By.CSS_SELECTOR,".radio:nth-child(1)")
        CURRENT_USED_SYSTEMS_MIS = (By.CSS_SELECTOR,".radio:nth-child(2)")
        AIMS_TABLE = (By.CSS_SELECTOR,".table.aims-table")
    class CompanyEmployeesLocators():
        EMPLOYEES_TABLE = (By.CSS_SELECTOR,".table.table-hover.employeestable")
    class CompanyInfoSystemsLocators():
        INFOSYSTEMS_TABLE = (By.CSS_SELECTOR,".table.common-infosystems-table")
    class CompanyRoomsVaultsLocators():
        ROOMS_TABLE = (By.CSS_SELECTOR,".table.rooms_table")
        VAULT_TABLE= (By.CSS_SELECTOR,".table.vault-table")
    class CompanySoftwareLocators():
        AIMS_DETAILS_TABLE = (By.CSS_SELECTOR,".table.aims-details-table")
        EXTERNAL_SOFTWARE_TABLE = (By.CSS_SELECTOR,".table.external-software-table")
        USER_ACCESS_CHECKBOX = (By.CSS_SELECTOR,".external_software-group .checkbox label input")
    class CompanyStructureLocators():
        STRUCTURE_TABLE = (By.CSS_SELECTOR,".department_table.table")

class GISLocators:
    class GisSoftWareLocators():
        GIS_SOFTWARE_TABLE = (By.CSS_SELECTOR, ".table.softwares-table")
    class GisRoomAccessLocators():
        GIS_ROOMS_TABLE = (By.CSS_SELECTOR, ".table.rooms_dynamic_table")
        GIS_SOFT_ROOMS_TABLE = (By.CSS_SELECTOR, ".table.ext_soft_rooms_dynamic_table")
        GIS_ACCESS_DESCRIPTION_GROUP = (By.CSS_SELECTOR, "#access_description_form")
        GIS_ACCESS_TYPICAL_DESCRIPTION_GROUP = (By.CSS_SELECTOR, "#access_description_form .radio:nth-child(2)")
        GIS_ACCESS_OWN_DESCRIPTION_GROUP = (By.CSS_SELECTOR, "#access_description_form .radio:nth-child(3)")
    class GisUsersAccessLocators():
        GIS_ACCESS_DESCRIPTION_GROUP = (By.CSS_SELECTOR, "form.form-horizontal.target-form")
        GIS_USER_ACCESS_TABLE = (By.CSS_SELECTOR,".table.access_table")
        GIS_USER_EXTERNAL_ACCESS_TABLE = (By.CSS_SELECTOR,".table.external_access_table")
    class GisFeaturesProcessingLocators():
        GIS_FSTEK_TERRITORIAL_AUTHORITY = (By.CSS_SELECTOR,"#id_fstek_territorial_authority")
        GIS_FSTEK_TERRITORIAL_AUTHORITY_CHEIF = (By.CSS_SELECTOR,"#id_fstek_territorial_authority_chief")

class PDNLocators:
    class PDNSoftWareLocators():
        PDN_SOFTWARE_TABLE = (By.CSS_SELECTOR,".table.softwares-table")
    class PDNAimsCategoryLocators():
        PDN_AIMS_CATEGORY_TABLE = (By.CSS_SELECTOR,".table.aims-category-table")
    class PDNRoomsAccess:
        PDN_ROOMS_DYNAMIC_TABLE = (By.CSS_SELECTOR,".table.rooms_dynamic_table")
        PDN_SUBJECT_CATEGORY_PDN_ROOMS_TABLE = (By.CSS_SELECTOR,".table.subject_category_pdn_rooms_table")
        PDN_EXTERNAL_SOFT_DYNAMIC_TABLE = (By.CSS_SELECTOR,".external_soft_dynamic_table.table")
        PDN_ROOM_DETAIL_LEVEL_RADDIOBUTTON = (By.CSS_SELECTOR,".room-detail-level-form")
        PDN_ACCESS_DESRIPTION_RADDIOBUTTON = (By.CSS_SELECTOR,"#access_description_form")
    class PDNUserAccess:
        PDN_GET_ACCESS_RADIIOBUTTON =(By.CSS_SELECTOR,".form-horizontal.target-form")
        PDN_USER_ACCESS_TABLE = (By.CSS_SELECTOR,".table.access_table")
        PDN_USER_EXTERNAL_ACCESS_TABLE = (By.CSS_SELECTOR,".table.external_access_table")
        PDN_STORAGE_RESPOSIBLE_EMPLOYESS_TABLE = (By.CSS_SELECTOR,".table.storage-responsible-employees-table")
    class PDNDepersonalization:
        PDN_DEPERSONALIZATIOND_RADDIOBUTTON = (By.CSS_SELECTOR,".form-group.doing_depersonalization-group")
        PDN_DEPERSONALIZATIOND_TABLE = (By.CSS_SELECTOR,".table.table-condensed")
    class PDNProcessing:
        PDN_POSTED_NOTIFICATION_CHECKBOX = "#id_posted_notification"
        PDN_REGISTRATION_NUMBER = "#id_registration_number"
        PDN_AGENCY_NAME = "#select2-chosen-15"
        PDN_PERSONAL_DATA_PROCESSING_REGIONS_ALL_CHECKBOX = "#id_personal_data_processing_regions_all"
        PDN_PERSONAL_DATA_PROCESSING_REGIONS_SELECT2 = "#s2id_id_personal_data_processing_regions"