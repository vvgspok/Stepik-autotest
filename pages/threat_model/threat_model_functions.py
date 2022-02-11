from collections import defaultdict

from pages.base_page import BasePage
from manager.manager_base import МенеджерСайта

class ThreatModelFunctions:
    class Check:
        def check_correct_generate_negative(self, negative_in_system, negative_list):
            error_massage = ""
            # Блок проверок соответствия ожидаемых негативных последствий с негативными последствиями в ИС
            if len(negative_in_system) > len(negative_list):
                error_massage = error_massage + "Количество негативных последствий в системе больше, чем предусмотрено справочником \n"
            if len(negative_in_system) < len(negative_list):
                error_massage = error_massage + "Количество негативных последствий в системе меньше, чем предусмотрено справочником \n"
            non_delete_values = []
            for negative in negative_list:
                try:
                    negative_in_system.remove(negative)
                except:
                    non_delete_values.append(negative)
            if len(non_delete_values) > 0:
                non_delete_value_str = ""
                for non_delete_value in non_delete_values:
                    non_delete_value_str = non_delete_value_str + "'" + non_delete_value + "', "
                error_massage = error_massage + "ИС не содержит ожидаемые негативные последствия:" + non_delete_value_str + "\n"

            negative_non_support_str = ""
            if len(negative_in_system) > 0 and negative_in_system[0] != 'False':
                for negative in negative_in_system:
                    negative_non_support_str = negative_non_support_str + "'" + negative + "', "
                error_massage = error_massage + "ИС содержит неожидаесые негативные последствия:" + negative_non_support_str + "\n"
            return error_massage
        def check_correct_generate_impact_negative(self,impact_types, system_impact_types):
            error_massage = ""
            for system_impact in system_impact_types:
                type = system_impact_types[system_impact]["ВИД РИСКА (УЩЕРБА)"]
                for negative in system_impact_types[system_impact]["НЕГАТИВНЫЕ ПОСЛЕДСТВИЯ"]:
                    try:
                        impact_types[type].remove(negative)
                    except:
                        pass
            types = ["У1. Ущерб физическому лицу",
                     "У2. Риски юридическому лицу, индивидуальному предпринимателю, связанные с хозяйственной деятельностью",
                     "У2. Риски юридическому лицу, индивидуальному предпринимателю, связанные с хозяйственной деятельностью"]
            for type in types:
                if len(impact_types[type]) > 0:
                    non_delete_impact = ""
                    for negative in impact_types[type]:
                        non_delete_impact = non_delete_impact + negative + ", "
                    error_massage = error_massage + "\n Указан некорректный вид воздейстивя '" + type + "' для негативных последствий: " + non_delete_impact
            return error_massage


    class Prepare:
        def get_business_precesses(self,system_name):
            '''
            Чтение бизнес процессов для указанной ИС
            '''
            self.browser.get(self.common_address + "cabinet/main_wizard/company_details/#step/business-processes")
            BasePage.ожидание_прогрузки_страницы(self)
            table = BasePage.Table.get_table_by_name(self, "Бизнес-процессы")
            rows = table.search_record_by_value("СИСТЕМЫ И СЕТИ, КОТОРЫЕ ОБЕСПЕЧИВАЮТ ВЫПОЛНЕНИЕ БИЗНЕС-ПРОЦЕССА",
                                                system_name)
            business_processes = []
            try:
                for row in rows:
                    business_processes.append(row["БИЗНЕС-ПРОЦЕСС"])
            except:
                business_processes.append(rows["БИЗНЕС-ПРОЦЕСС"])
            return business_processes

        def get_system_infromation(self,system_name):
            '''
            Чтение общих сведений об указанной ИС
            '''
            self.browser.get(self.common_address + "cabinet/main_wizard/company_details/#step/common-infosystems")
            BasePage.ожидание_прогрузки_страницы(self)
            table = BasePage.Table.get_table_by_name(self, "Общие сведения о системах")
            row = table.search_record_by_value("НАИМЕНОВАНИЕ СИСТЕМЫ", system_name)
            table.edit_row(row)
            BasePage.ожидание_прогрузки_страницы(self)
            window = BasePage.ModalWindow.searchByHeaderText(self, "Редактирование")
            parametr = window.search_parametr("Информация (данные), содержащаяся в системе")
            window.closeWindow()
            return parametr.value

        def get_negative_for_business_processes(self,business_processes):
            '''
            Чтение негативных последствий для бизнес-процессов ИС
            '''
            self.browser.get(self.common_address + "manager/")
            BasePage.ожидание_прогрузки_страницы(self)
            МенеджерСайта(self.browser).Перейти_в_раздел("Модель угроз")
            МенеджерСайта(self.browser).Перейти_на_шаг("Бизнес-процессы")
            table = BasePage.Table.get_table_by_name(self, "Бизнес-процессы")
            BasePage.ожидание_прогрузки_страницы(self)
            negative_list = []
            for proc in business_processes:
                table.search_str(proc)
                table = BasePage.Table.get_table_by_name(self, "Бизнес-процессы")
                try:
                    row = table.search_record_by_value("БИЗНЕС-ПРОЦЕСС", proc)
                    negative_list = negative_list + row["НЕГАТИВНЫЕ ПОСЛЕДСТВИЯ"]
                except:
                    pass
            return negative_list

        def get_negative_for_system_information(self,system_information):
            # Чтение негативных последчтыий для информации об ИС
            negative_list = []
            self.browser.get(self.common_address + "manager/")
            BasePage.ожидание_прогрузки_страницы(self)
            МенеджерСайта(self.browser).Перейти_в_раздел("Модель угроз")

            МенеджерСайта(self.browser).Перейти_на_шаг("Информация в ИС")
            table = BasePage.Table.get_table_by_name(self, "Информация (данные), содержащаяся в системах и сетях")
            BasePage.ожидание_прогрузки_страницы(self)

            for inform in system_information:
                table.search_str(inform)
                table = BasePage.Table.get_table_by_name(self, "Информация (данные), содержащаяся в системах и сетях")
                try:
                    row = table.search_record_by_value("ИНФОРМАЦИЯ (ДАННЫЕ)", inform)
                    negative_list = negative_list + row["НЕГАТИВНЫЕ ПОСЛЕДСТВИЯ"]
                except:
                    pass
            return negative_list

        def get_impact_from_manager(self,negative_list):
            # Получение Вида Риска (ущерба) негативных последствий
            self.browser.get(self.common_address + "manager/")
            BasePage.ожидание_прогрузки_страницы(self)
            МенеджерСайта(self.browser).Перейти_в_раздел("Модель угроз")

            МенеджерСайта(self.browser).Перейти_на_шаг("Негативные последствия")
            impact_types = defaultdict(dict)
            impact_types["Ущерб физическому лицу"] = []
            impact_types[
                "Риски юридическому лицу, индивидуальному предпринимателю, связанные с хозяйственной деятельностью"] = []
            impact_types[
                "Ущерб государству в области обеспечения обороны страны, безопасности государства и правопорядка, а также в социальной, экономической, политической, экологической сферах детальности"] = []
            table = BasePage.Table.get_table_by_name(self, "Негативные последствия")
            for negative in negative_list:
                table.search_str(negative)
                table = BasePage.Table.get_table_by_name(self, "Негативные последствия")
                row = table.search_record_by_value("НАИМЕНОВАНИЕ", negative)
                type = row["ВИД РИСКА (УЩЕРБА)"]
                impact_types[type].append(negative)
            impact_types["У1. Ущерб физическому лицу"] = impact_types["Ущерб физическому лицу"]
            impact_types[
                "У2. Риски юридическому лицу, индивидуальному предпринимателю, связанные с хозяйственной деятельностью"] = \
            impact_types[
                "Риски юридическому лицу, индивидуальному предпринимателю, связанные с хозяйственной деятельностью"]
            impact_types[
                "У3. Ущерб государству в области обеспечения обороны страны, безопасности государства и правопорядка, а также в социальной, экономической, политической, экологической сферах детальности"] = \
            impact_types[
                "Ущерб государству в области обеспечения обороны страны, безопасности государства и правопорядка, а также в социальной, экономической, политической, экологической сферах детальности"]
            impact_types.pop("Ущерб физическому лицу")
            impact_types.pop(
                "Риски юридическому лицу, индивидуальному предпринимателю, связанные с хозяйственной деятельностью")
            impact_types.pop(
                "Ущерб государству в области обеспечения обороны страны, безопасности государства и правопорядка, а также в социальной, экономической, политической, экологической сферах детальности")
            return impact_types

        def edit_threat_model(self,system_name):
            self.browser.get(self.common_address + "cabinet/threat_model/threat_assessment/list/")
            BasePage.ожидание_прогрузки_страницы(self)
            table = BasePage.Table.get_table_by_name(self, "Реестр систем")
            row = table.search_record_by_value("НАИМЕНОВАНИЕ ИС", system_name)
            try:
                table.row_command(row, "Ввод данных")
            except:
                table.row_command(row, "Изменить")
            BasePage.ожидание_прогрузки_страницы(self)

    class NegativeAftereffect:


        def get_negative_from_threat_model(self):
            table = BasePage.Table.get_table_by_name(self, "Негативные последствия")
            table_data = table.get_value()
            negative_in_system = []
            for data in table_data:
                try:
                    value = table_data[data]
                    negative_in_system.append(value['НЕГАТИВНЫЕ ПОСЛЕДСТВИЯ'])
                except:
                    pass
            return negative_in_system

        def get_impact_from_threat_model(self):
            try:
                BasePage.WizardStep.Найти(self, "Виды рисков (ущербов)").Перейти()
            except:
                pass
            BasePage.ожидание_прогрузки_страницы(self)
            table = BasePage.Table.get_table_by_name(self, "Виды рисков (ущербов)")
            system_impact_types = table.get_value()
            return system_impact_types
