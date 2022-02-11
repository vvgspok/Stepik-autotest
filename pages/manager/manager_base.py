from pages.base_page import BasePage


class МенеджерСайта(BasePage):
    browser = None
    sidebar = None
    main_container = None
    scrollable_tabs = None
    Текущий_раздел = None  # текущий раздел
    Текущий_шаг = None  # текущий шаг

    def __init__(self, browser):
        """
        Конструктор класса Менеджера сайта.

        :param browser: элемент типа WebElement иди Driver (browser)
        """
        self.browser = browser
        self.sidebar = self.browser.find_element_by_css_selector("#sidebar")
        self.main_container = self.browser.find_element_by_css_selector(
            ".container.main-container.manager-content-wrapper")
        try:
            self.scrollable_tabs = self.browser.find_element_by_css_selector(".scrollable-tab")
        except:
            pass

    def Перейти_в_раздел(self, name):
        """

        Перейти в раздел менеджера сайта (меню слева)

        :param name: Наименование раздела
        :return: Ничего не возвращает. Результат выполнения функции - переход в раздел
        """
        panels = self.sidebar.find_elements_by_css_selector(".panel.dropdown")
        for panel in panels:
            panel_obj = МенеджерСайта.__Раздел(panel)
            if panel_obj.name == name:
                if panel_obj.is_collapse_in() == False:
                    panel_obj.element.click()
                # self.Текущий_раздел = panel_obj

    def Перейти_на_шаг(self, name):
        """
        Перейти на шаг раздела менеджера сайта. Важно - на момент вызова необходимо раскрыть раздел, в рамках которого расположен шаг

        :param name: Наименование шага раздела
        :return: Ничего не возвращает. Результат выполнения функции - переход на шаг
        """
        steps = self.sidebar.find_elements_by_css_selector(".panel.dropdown a[aria-expanded='true']+ul li")
        for step in steps:
            step_obj = МенеджерСайта.__Шаг(step)
            if (step_obj.name == name):
                step_obj.element.click()
                break

    def Перейти_на_вкладку(self, name):
        """
        Перейти на вкладку области данных

        :param name: Наименование вкладки
        :return: Ничего не возвращает. Результат выполнения функции - переход на вкладку
        """
        if self.scrollable_tabs == None:
            self.scrollable_tabs = self.browser.find_element_by_css_selector(".scrollable-tab")
        tabs = self.scrollable_tabs.find_elements_by_css_selector("li")

        for tab in tabs:
            try:
                tab_name = tab.find_element_by_css_selector("a").text
                if tab_name == name:
                    tab.click()
            except:
                pass

    class __Раздел():
        name = ""
        element = ""
        state = ""  # класс Collapsed - закрыт, нет - закрыт
        sections = []

        def __init__(self, element):
            """
            :param element: WebElement класса .panel.dropdown
            """
            self.element = element
            self.name = self.element.find_element_by_css_selector("a").get_property("title")
            self.state = self.element.find_element_by_css_selector("a").get_attribute("class")

        def is_collapse_in(self):
            """
            Получение состояния "раскрытости" разела

            :return: True - если раздел раскрыт, False - если свернут
            """
            if self.state == "":
                return True
            else:
                return False

    class __Шаг:
        element = ""
        name = ""
        href = ""

        def __init__(self, element):
            """
            :param element: WebElement класса  .panel.dropdown a[aria-expanded='true']+ul li
            """
            self.element = element
            self.name = self.element.find_element_by_css_selector("a").text
            self.href = self.element.find_element_by_css_selector("a").get_property("href")
