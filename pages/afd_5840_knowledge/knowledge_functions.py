import json

import pytest


def get_data_on_tariff(tariff):
    """
    Возвращает список ссылок по данному тарифу
    :param tariff:all,...
    :return список ссылок с данным тарифом:
    """
    import os
    aaa = os.listdir(path="../..")
    # with open(r'knowledge_data.json') as f:
    with open(r'pages/afd_5840_knowledge/knowledge_data.json', encoding="utf-8") as f:
        # with open(r'pages/afd_5840_knowledge/knowledge_data_copy.json', encoding="utf-8") as f:
        pars = json.load(f)
        data = pars.get("knowledge")
    result = []
    for knowledge_link in data:
        assert "alfa-doc" not in knowledge_link.get("link_page"), \
            "В файле json встречено alfa-doc. Исправьте на универсальную ссылку"
        tariff = (tariff.strip()).upper()
        if tariff in knowledge_link:
            result.append(knowledge_link)
    return result


def получить_заголовок_до_перехода_в_базу_знаний(browser, KnowledgeLocators):
    assert browser.find_element(*KnowledgeLocators.STEP_IN_STEPPAGE), "Элемент с шагом не найден"
    number = browser.find_element(*KnowledgeLocators.STEP_IN_STEPPAGE)
    number = int(number.text)
    name = browser.find_element(*KnowledgeLocators.NAME_IN_STEPPAGE)
    name = name.text
    need_text = f"{number} Шаг {number} «{name}»"
    return need_text


def получить_заголовок_в_базе_знаний(browser, KnowledgeLocators):
    zagolovok_in_knowledge = browser.find_element(*KnowledgeLocators)
    zagolovok_in_knowledge = zagolovok_in_knowledge.text
    # print(zagolovok_in_knowledge)
    return zagolovok_in_knowledge


def переход_на_вкладку_с_БЗ(browser, locator):
    """
    Переход на вкладку с БЗ и с закрытием лишних
    """
    current_window = browser.current_window_handle
    for handle in browser.window_handles:
        if handle != current_window:
            browser.switch_to.window(handle)
            browser.close()
    browser.switch_to.window(current_window)
    browser.find_element(*locator).click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    return browser, current_window


def проверка_на_skip_test(data, tariff):
        if data.get("skip") == True:
            pytest.skip()
        elif tariff in data:
            if "skip" in data.get(tariff):
                data_tariff = data.get(tariff)
                if data_tariff.get("skip") == 1:
                    pytest.skip()
