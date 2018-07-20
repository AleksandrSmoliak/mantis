from random import randrange
from model.project import Project
import random
import string


def random_projectname(perfix, maxlen):
    symbols = string.ascii_letters
    return perfix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_del_project(app):
    project_name = random_projectname("project_", 10)
    # Получаем количествво созданных проектов по SOAP
    old_project = len(app.soap.get_projects("administrator", "root"))
    # Реализуем предусловие
    if old_project == 0:
        app.soap.add_projects("administrator", "root", Project(name=project_name, description="Описание2555"))
    # Герерируем случайный индекс с ограничением по количеству существующих проектов
    index = randrange(1, old_project)
    # Удаляем проект по индексу
    app.soap.del_projects("administrator", "root", index)
    # Получаем новое значение количества проектов
    new_project = len(app.soap.get_projects("administrator", "root"))
    # Проверяем что количество проектов изменилось
    assert old_project - 1 == new_project
