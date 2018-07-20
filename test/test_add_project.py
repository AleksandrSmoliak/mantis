from model.project import Project
import random
import string


def random_projectname(perfix, maxlen):
    symbols = string.ascii_letters
    return perfix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project_name = random_projectname("project_", 10)
    # Получакем количество созданных проектов по soap
    old_project = len(app.soap.get_projects("administrator", "root"))
    # Создаем новый проект через soap
    app.soap.add_projects("administrator", "root", Project(name=project_name, description="Описание2555"))
    # Получаем новое значение количества проектов
    new_project = len(app.soap.get_projects("administrator", "root"))
    # Проверяем что количество изменилось
    assert old_project + 1 == new_project
