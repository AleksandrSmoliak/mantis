from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app

    # Проверка того что юзер существует
    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.15.0/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self, username, password):
        client = Client("http://localhost/mantisbt-2.15.0/api/soap/mantisconnect.php?wsdl")
        return client.service.mc_projects_get_user_accessible(username, password)

    def add_projects(self, username, password, project):
        client = Client("http://localhost/mantisbt-2.15.0/api/soap/mantisconnect.php?wsdl")
        client.service.mc_project_add(username, password, project)