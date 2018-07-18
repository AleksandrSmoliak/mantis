from random import randrange
from model.project import Project


def test_del_project(app):
    app.session.login("administrator", "root")
    # открываем страницуц с проектами
    app.project.open_project_page()
    # Получаем количествво созданных проектов
    old_project = app.project.project_count()
    # Реализуем предусловие
    if old_project == 0:
        app.project.create_project(Project(name="Проект1", description="Описание проекта"))
    # Герерируем случайный индекс с ограничением по количеству существующих проектов
    index = randrange(0, old_project)
    # Удаляем проект по индексу
    app.project.del_project_by_index(index)
    # Получаем новое значение количества проектов
    new_project = app.project.project_count()
    # Проверяем что количество проектов изменилось
    assert old_project - 1 == new_project
