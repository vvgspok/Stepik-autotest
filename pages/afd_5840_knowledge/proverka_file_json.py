import json
from collections import Counter


def proverka_json_file():
    """
    отдельный запуск файла, просто для информации
    """

    with open(r'knowledge_data.json', encoding='utf-8') as f:
        pars = json.load(f)
        data = pars.get("knowledge")
    print(f"► Всего страниц для проверки: {len(data)}")

    tarifs = ["КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ",
              "ПДН.БЮДЖЕТ.ЭКСПЕРТ",
              "КИИ.СТАНДАРТ",
              "КИИ.ПДН.ЭКСПЕРТ",
              "ГИС.ЭКСПЕРТ",
              "ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ",
              "ПДН.НОТАРИУС"
              ]

    # all_link - собирает все ссылки в json
    all_link = get_all_links(data, tarifs)
    print(f"► Всего ссылок: {len(all_link)}")
    for i in all_link:
        if i.strip() != i:
            print(f"________Надо убрать пробелы в ссылке_____: {i}")

    # кол-во тестов для каждого тарифа
    count_tests_for_tarif(data, tarifs)

    # здесь ищутся дубли в ссылках all_link
    dubli_links = [k for k, v in Counter(all_link).items() if v > 1]
    if len(dubli_links) != 0:
        print(f"_____________________________________ Есть дубли ссылок = {len(dubli_links)}\n")
        for i in range(dubli_links.__len__()):
            print(f"{i + 1}) {dubli_links[i]}")

    # поиск ломанных ссылок
    find_broken_link(data)


def find_broken_link(data):
    # поиск ломанных ссылок
    # писал вспешку, хз что там творится
    broken_link, count_broken_link = [], 0
    count_link_page = 0
    new_links_page = []
    for knowledge_link in data:
        new_links_page.append(knowledge_link.get("link_page"))
        silka = knowledge_link.get("link_page")
        if len(silka) == 0:
            print("Отсутствкет ссылка")
            print(knowledge_link.get("name"))
            continue
        if silka[0] == "/":
            broken_link.append(knowledge_link.get("link_page"))
            count_broken_link += 1
        if ("." or "alfa" or "//") in knowledge_link.get("link_page"):
            broken_link.append(knowledge_link.get("link_page"))
            count_broken_link += 1
        for key in knowledge_link:
            if "link_bz" in list(knowledge_link.keys()):
                link = (knowledge_link.get(key)).get("link_bz")
                new_links_page.append(link)
                if ('//' or "." or "alfa") in link:
                    broken_link.append(link)
                    count_broken_link += 1

    if count_broken_link != 0:
        print(f"► Есть ссылки для переделки в кол-ве: {count_broken_link}")
        for i in broken_link:
            print(i)


def get_all_links(data, tarifs):
    all_link = []
    for i in data:
        all_link.append(i.get("link_page"))
        for tarif in tarifs:
            if tarif in i:
                all_link.append((i.get(tarif)).get("link_bz"))
    return all_link


def count_tests_for_tarif(data, tarifs_all):
    tarifs_chet = {"КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ": 0,
                   "ПДН.БЮДЖЕТ.ЭКСПЕРТ": 0,
                   "КИИ.СТАНДАРТ": 0,
                   "КИИ.ПДН.ЭКСПЕРТ": 0,
                   "ГИС.ЭКСПЕРТ": 0,
                   "ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ": 0,
                   "ПДН.НОТАРИУС": 0
                   }
    for dat in data:
        for tarif in tarifs_all:
            if tarif in dat:
                tarifs_chet.update({tarif: tarifs_chet.get(tarif) + 1})
    print("► Кол-во тестов для каждого тарифа:")
    for i in tarifs_chet.items():
        print('  ', i)
    print('  Итого: ', sum(tarifs_chet.values()))
    # input()

proverka_json_file()
