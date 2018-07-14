from random import randrange
def test_del_project(app):
    app.project.open_project_page()
    old_project = app.project.project_count()
    index = randrange(0, old_project)
    app.project.del_project_by_index(index)