from model.project import Project

def test_add_project(app):
    app.project.open_project_page()
    old_project = app.project.project_count()
    app.project.create_project(Project(name="Проект1", description="Описание проекта"))
    app.project.open_project_page()
    new_project = app.project.project_count()
    assert old_project + 1 == new_project
