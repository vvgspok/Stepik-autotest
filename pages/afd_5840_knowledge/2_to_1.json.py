import json


def concat(file1, file2):
    """
    отдельный запуск файла, просто для информации
    """
    new_tarif = 'КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ'

    with open(file2, encoding='utf-8') as f2:
        pars = json.load(f2)
        new_datas = pars.get("afd_5840_knowledge")

    with open(file1, encoding='utf-8') as f1:
        pars = json.load(f1)
        datas = pars.get("afd_5840_knowledge")
        all_links_datas = get_all_links(datas)  # все шаги в старом файле

        exists_links = []
        for new_data in new_datas:
            if new_data.get("link_page") not in all_links_datas:
                new_dict = {}
                new_dict['name'] = new_data.get("name")
                new_dict['link_page'] = new_data.get("link_page")
                new_dict['type_page'] = new_data.get("type_page")
                new_dict[new_tarif] = {
                    'link_bz': new_data.get('link_bz'),
                    'zagolovok_in_knowledge': new_data.get('zagolovok_in_knowledge')
                }
                datas.append(new_dict)
            elif new_data.get("link_page") in all_links_datas:

                for i in range(len(datas)):
                    if datas[i].get('link_page') == new_data.get('link_page'):
                        if new_tarif not in datas[i]:
                            datas[i][new_tarif] = {
                                'link_bz': new_data.get('link_bz'),
                                'zagolovok_in_knowledge': new_data.get('zagolovok_in_knowledge')
                            }

                        break

    file_path = file1
    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(datas, outfile, ensure_ascii=False)
    print()

    print()


def get_all_links(data):
    all_link = []
    for i in data:
        link = i.get("link_page")
        all_link.append(link.strip())

    return all_link


concat("knowledge_data(old).json", "КИИ_ГИС_ПДн_Бюджет_Эксперт.json")
