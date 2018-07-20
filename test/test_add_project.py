from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    app.soap.add_projects("administrator", "root", Project(name="Новый проект4", description="Описание234"))
    # Переходим на страницу с проектами
    #app.project.open_project_page()
    # Получакем количество созданных проектов по soap
    old_project = len(app.soap.get_projects("administrator", "root"))
    # Добавляем новый проект
    #app.project.create_project(Project(name="Проект1", description="Описание проекта"))
    # Возвращаемся на страницу с проектами
    #app.project.open_project_page()
    # Получаем новое значение количества проектов
    new_project = len(app.soap.get_projects("administrator", "root"))
    # Проверяем что количество изменилось
    assert old_project + 1 == new_project
