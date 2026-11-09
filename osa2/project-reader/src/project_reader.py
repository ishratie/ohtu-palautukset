import urllib.request
import tomli
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Tiedoston lataaminen internetistä
        request = urllib.request.urlopen(self._url)
        content = request.read().decode("utf-8")

        data = tomli.loads(content)

        name = data["project"]["name"]
        description = data["project"]["description"]
        dependencies = data["project"]["dependencies"]
        dev_dependencies = data["dependency-groups"]["dev"]

        return Project(name, description, dependencies, dev_dependencies)