from mgsc.service.service import GitService
from mgsc.blueprints import Repository, Namespace


class Github(GitService):
    @property
    def servertype(self):
        return "github"

    @property
    def repositories(self) -> Repository:
        all_repos = self.session.httpaction(http_verb="get", path=f"/user/repos").json()

        for repo in all_repos:
            yield Repository(
                name=repo["name"],
                namespace=repo["owner"]["login"],
                ssh_url=repo["ssh_url"],
                http_url=repo["clone_url"],
                description=repo["description"],
            )

    def get_namespace_repos(self, namespace):
        group_projects = self.session.httpaction(
            "get", f"https://api.github.com/orgs/{namespace}/repos"
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
        namespaces = self.session.httpaction(http_verb="get", path="/user/orgs").json()

        for namespace in namespaces:
            yield Namespace(
                name=namespace["login"],
                parent="root",
                repositories=self._get_namespace_repos(namespace["path"]),
            )

    @property
    def userid(self):
        userid = self.session.httpaction("get", "/user").json()["id"]

        return userid

    def create_namespace(self):
        raise NotImplementedError()

    def create_repository(self):
        raise NotImplementedError()
