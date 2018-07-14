from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_create_page.php")):
            wd.find_element_by_xpath("//ul[@class='nav nav-list']/li[7]/a").click()
            wd.find_element_by_link_text("Управление проектами").click()

    def create_project(self, project):
        wd = self.app.wd
        # Открываем страницу создания проекта
        self.open_project_page()
        # Переход на форму создания проекта
        wd.find_element_by_xpath("//button[@class='btn btn-primary btn-white btn-round']").click()
        # Заполнение полей формы
        self.fill_project_form(project)
        # Нажание на кнопку добавления проекта
        wd.find_element_by_xpath("//input[@class='btn btn-primary btn-white btn-round']").click()


    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def project_count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//div[@class='widget-box widget-color-blue2']/div[2]/div[1]/div[2]/table/tbody/tr"))

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_list = []
        for element in wd.find_elements_by_xpath("//div[@class='table-responsive']/table/tr"):
            cells = element.find_elements_by_tag_name("td")
            name = cells[1]
            description = cells[5]
            self.project_list.append(Project(name=name, description=description))
        return list(self.project_list)

    def open_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        row = wd.find_elements_by_xpath("//div[@class='table-responsive']/table/tbody/tr")[index]
        cell = row.find_elements_by_tag_name("td")[0]
        cell.find_element_by_tag_name("a").click()

    def del_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_by_index(index)
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()