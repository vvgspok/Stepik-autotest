MAIN_URL = "http://rc.alfa-doc.ru/"


# MAIN_URL = "https://alfa-doc.ru/"

import os

# Простые профили с простыми роганизациями
def Global_Profile(tariff):
    try:
        user_tariff = {
            "КИИ.СТАНДАРТ": ("kii_standart", "kii_standartkii_standart"),
            "КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ": ("kii_gis_pdn_bdjt_exprt", "kii_gis_pdn_bdjt_exprtkii_gis_pdn_bdjt_exprt"),
            "ПДН.БЮДЖЕТ.ЭКСПЕРТ": ("pdn_bdjt_exprt", "pdn_bdjt_exprtpdn_bdjt_exprt"),
            "КИИ.ПДН.ЭКСПЕРТ": ("kii_pdn_exprt", "kii_pdn_exprtkii_pdn_exprt"),
            "ГИС.ЭКСПЕРТ": ("gis_exprt", "gis_exprtgis_exprt"),
            "ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ": ("gis_pdn_bdjt_exprt", "gis_pdn_bdjt_exprtgis_pdn_bdjt_exprt"),
        }
        return user_tariff.get(tariff)
    except:
        print("Нет пользователя для указанного тарифа")


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BROWSER_DIR = os.path.join(ROOT_DIR, 'chromedriver.exe')
