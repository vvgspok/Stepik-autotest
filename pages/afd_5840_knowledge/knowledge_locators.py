from selenium.webdriver.common.by import By

from pages.afd_5840_knowledge.knowledge_functions import *


class KnowledgeLocators():
    HELP_CONTAINER = (By.CSS_SELECTOR, ".help-wrapper > .help-container")
    HELP_TEXT = (By.CSS_SELECTOR, ".help-container > .alert.alert-info > div:nth-child(1) > p:nth-child(1)")
    HELP_LINK = (By.CSS_SELECTOR, ".help-container > .alert.alert-info > div:nth-child(2) > a")
    ZAGOLOVOK_IN_KNOWLEDGE = (By.CSS_SELECTOR, ".page-content > h1")
    STEP_IN_STEPPAGE = (By.CSS_SELECTOR, "ul.wizard-steps li.active > a span.step-number > span")
    NAME_IN_STEPPAGE = (By.CSS_SELECTOR, "ul.wizard-steps li.active > a span.step-name")
    SPISOK_PAGES_THIS_RAZDEL = (By.CSS_SELECTOR, ".summary.clearfix  > .text-uppercase")
    PAGES_THIS_RAZDEL = (By.CSS_SELECTOR, ".summary.clearfix  > ul li a")
    BREAD_CRUMBS = (By.CSS_SELECTOR, "div.jbreadcrumbs.jbreadcrumbs-line ul li:nth-child(3) a")
    DATA_TARIFF_ПДН_БЮДЖЕТ_ЭКСПЕРТ = get_data_on_tariff("ПДН.БЮДЖЕТ.ЭКСПЕРТ")
    DATA_TARIFF_КИИ_СТАНДАРТ = get_data_on_tariff("КИИ.СТАНДАРТ")
    DATA_TARIFF_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ = get_data_on_tariff("КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
    DATA_TARIFF_КИИ_ПДН_ЭКСПЕРТ = get_data_on_tariff("КИИ.ПДН.ЭКСПЕРТ")
    DATA_TARIFF_ГИС_ЭКСПЕРТ = get_data_on_tariff("ГИС.ЭКСПЕРТ")
    DATA_TARIFF_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ = get_data_on_tariff("ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
