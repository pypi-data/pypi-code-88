from typing import Union

from snitch_ai.internal.guid import GUID
from snitch_ai.internal.api_client import ApiClient
from snitch_ai.internal.project_version import ProjectVersion

class Project:

    def __init__(self, project_id: GUID, name: str):
        self.project_id = project_id
        self.name = name


    def create_project_version(self, version_name: str) -> ProjectVersion:
        """
        Create a project version.
        :param version_name: The name of the project version to create. Must be unique for this project.
        :return: The newly created project version.
        """
        client = ApiClient()
        resp = client.post(f"project/{self.project_id}/version", data={"name": version_name})
        if resp.status_code != 201:
            raise Exception(f"Could not create project version: {resp.text}")
        json = resp.json()

        return ProjectVersion(GUID(json["projectId"]), GUID(json["id"]), json["name"])


    def get_project_version(self, target: Union[str, GUID]) -> ProjectVersion:
        """
        Gets a project version by ID or by version name.
        :param target: The ID of the version or version name.
        :return: The requested project version.
        """
        client = ApiClient()

        json = None
        if isinstance(target, str):
            resp = client.get(f"project/{self.project_id}/version", params={"name": target})
            if resp.status_code != 200:
                raise Exception(f"Could not find project version: {target}")
            json = resp.json()
        else:
            resp = client.get(f"project/{self.project_id}/version/{target}")
            if resp.status_code != 200:
                raise Exception(f"Could not find project version: {resp.text}")
            json = resp.json()

        return ProjectVersion(GUID(json["projectId"]), GUID(json["id"]), json["name"])


    def __str__(self):
        return f"Project {self.project_id}: {self.name}"


def create_project(project_name: str) -> Project:
    """
    Create a project with the specified name.
    :param project_name: The name of the project to create. Must be unique within the entire system.
    :return: The created project.
    """
    client = ApiClient()

    resp = client.post("project", data={ "name": project_name })
    if resp.status_code != 201:
        raise Exception(f"Could not create project: {resp.text}")

    json = resp.json()

    return Project(GUID(json["id"]), json["name"])


def get_project(target: Union[str, GUID]) -> Project:
    """
    Get a project by ID or project name.
    :param target: The ID of the project or project name.
    :return: The requested project.
    """
    client = ApiClient()

    json = None
    if isinstance(target, str):
        resp = client.get("project", params={ "name": target })
        if resp.status_code != 200:
            raise Exception(f"Could not find project: {resp.text}")
        json = resp.json()
    else:
        resp = client.get(f"project/{target}")
        if resp.status_code != 200:
            raise Exception(f"Could not find project: {resp.text}")
        json = resp.json()

    return Project(GUID(json["id"]), json["name"])
