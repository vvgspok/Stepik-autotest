from selenium.webdriver.common.by import By


class DataEntryLocators:
    NAVIGATION_TABS_ELEMENTS_SUCCESS = (By.XPATH, """//*[@class = "nav nav-tabs"]//*[@class = "text-success"]""")
    # так как проверяется эталонная организация - все Мастеры заполнены
    WIZARD_STEP = (By.XPATH, "//*[@class = 'wizard-step']")
    WIZARD_STEP_DISABLED = (By.XPATH, "//*[@class = 'wizard-step disabled passive']")
    WIZARD_STEP_ACTIVE = (By.XPATH, "//*[@class = 'wizard-step active']")
    WIZARD_MASTER = (By.XPATH, """//*[contains(., "<MASTER_NAME>") and @class="text-success"]""")
    STEP = (By.XPATH, """//*[@data-key= "STEP_KEY"]""")
    PANELS_NAMES = (By.XPATH, """//*[@class = "panel-title"]//*[@class = "help-link"]""")
    PANEL_BODY = (By.XPATH, """//*[@class = "help-link" and contains(text(), '<PANEL_TITLE>')]//ancestor::div[3]//*[@class = 'panel-body']""")
    TEXT_FIELDS = (By.XPATH, f"""//*[@class = "help-link" and contains(text(), '<PANEL_TITLE>')]//ancestor::div[3]//*[@class = 'panel-body']//*[@class = 'form-control']""")
    LARGE_TEXT_FIELDS = (By.XPATH, f"""//*[@class = "help-link" and contains(text(), '<PANEL_TITLE>')]//ancestor::div[3]//*[@class = 'panel-body']//*[@class = 'form-control col-md-4']""")
    CHECKBOXES = (By.XPATH, f"""//*[@class = "help-link" and contains(text(), '<PANEL_TITLE>')]//ancestor::div[3]//*[@class = 'panel-body']//input[@type='checkbox']""")
    RADIO_BUTTONS = (By.XPATH, f"""//*[@class = "help-link" and contains(text(), '<PANEL_TITLE>')]//ancestor::div[3]//*[@class = 'panel-body']//input[@type='radio']""")

