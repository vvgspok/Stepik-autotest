from selenium.webdriver.common.by import By


class BaseLocators:
    class Table:
    # локатор строки поиска
        search_control = (By.CLASS_NAME, "search-control")
        # локатор кнопки фильтр
        filter_control = (By.CLASS_NAME, "filter-control")
        # локатор кнопки "столбцы"
        column_сontrol = (By.CLASS_NAME, "column-control")
        # локатор кнопки "Обновить"
        refresh_control = (By.CLASS_NAME, "refresh-control")
        # локатор "кол-во элементов"
        page_control = (By.CLASS_NAME, "page-control")
        # локатор "таблицы"
        ksb_table_wrapper = (By.CLASS_NAME, "ksb-table-wrapper")

        undertable = (By.XPATH, "//*[contains(@class,'undertable table-buttons')]")
        page_size_dropdown_toggle = (By.CSS_SELECTOR,".page-size.dropdown-toggle")