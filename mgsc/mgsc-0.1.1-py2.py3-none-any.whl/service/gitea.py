from mgsc.service.service import GitService
from mgsc.blueprints import Repository, Namespace


class Gitea(GitService):
    API_BASE = "/api/v1"

    @property
    def servertype(self):
        return "gitea"

    @property
    def repositories(self) -> Repository:
        all_repos = self.session.httpaction(
            http_verb="get", path=f"{Gitea.API_BASE}/user/repos"
        ).json()

        for repo in all_repos:
            if repo["owner"]["id"] == self.userid:
                yield Repository(
                    name=repo["name"],
                    namespace=repo["owner"]["login"],
                    ssh_url=repo["ssh_url"],
                    http_url=repo["clone_url"],
                    description=repo["description"],
                )
            else:
                pass

    def get_namespace_repos(self, namespace):
        group_projects = self.session.httpaction(
            "get", f"{Gitea.API_BASE}/orgs/{namespace}/repos"
        ).json()

        for repo in group_projects:
            yield Repository(
                name=repo["name"],
                namespace=repo["owner"]["login"],
                ssh_url=repo["ssh_url"],
                http_url=repo["clone_url"],
                description=repo["description"],
            )

    def get_namespaces(self) -> Namespace:
        namespaces = self.session.httpaction(
            http_verb="get", path=f"{Gitea.API_BASE}/user/orgs"
        ).json()

        for namespace in namespaces:
            yield Namespace(
                name=namespace["username"],
                parent="root",
                repositories=self._get_namespace_repos(namespace["username"]),
            )

    @property
    def userid(self):
        userid = self.session.httpaction("get", f"{Gitea.API_BASE}/user").json()["id"]

        return userid

    def create_namespace(self):
        raise NotImplementedError()

    def create_repository(self):
        raise NotImplementedError()
