from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    # Переходим на страницу с проектами
    app.project.open_project_page()
    # Получакем количество созданных проектов
    old_project = app.project.project_count()
    # Добавляем новый проект
    app.project.create_project(Project(name="Проект1", description="Описание проекта"))
    # Возвращаемся на страницу с проектами
    app.project.open_project_page()
    # Получаем новое значение количества проектов
    new_project = app.project.project_count()
    # Проверяем что количество изменилось
    assert old_project + 1 == new_project
