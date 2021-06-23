from mgsc.service.service import GitService
from mgsc.blueprints import Repository, Namespace


class Stash(GitService):
    @property
    def servertype(self):
        return "stash"

    @staticmethod
    def _get_clone_address(clone_links_json, addr_type):
        for addr in clone_links_json:
            if addr["name"] == addr_type:
                return addr["href"]
        raise RuntimeError(f"Cannot find the clone address of type {addr_type}")

    @property
    def repositories(self) -> Repository:
        all_repos = self.session.httpaction(
            http_verb="get",
            # todo: remove hardcoded limit and use pagination
            path=f"/rest/api/1.0/projects/~{self.session.username}/repos?limit=1000",
        ).json()

        for repo in all_repos["values"]:
            yield Repository(
                name=repo["name"],
                namespace=repo["project"]["key"],
                ssh_url=self._get_clone_address(repo["links"]["clone"], "ssh"),
                http_url=self._get_clone_address(repo["links"]["clone"], "http"),
                description=repo["id"],
            )

    def get_namespace_repos(self, namespace):
        group_projects = self.session.httpaction(
            "get", f"/rest/api/1.0/projects/{namespace}/repos?limit=1000"
        ).json()

        for repo in group_projects["values"]:
            yield Repository(
                name=repo["name"],
                namespace=repo["project"]["key"],
                ssh_url=self._get_clone_address(repo["links"]["clone"], "ssh"),
                http_url=self._get_clone_address(repo["links"]["clone"], "http"),
                description=repo["id"],
            )

    def get_namespaces(self) -> Namespace:
        namespaces = self.session.httpaction(
            http_verb="get", path="/rest/api/1.0/projects?limit=1000"
        ).json()

        for namespace in namespaces["values"]:
            namespace_obj = Namespace(
                name=namespace["key"],
                parent="root",
            )

            namespace_obj.repositories = (self.get_namespace_repos(namespace["key"]),)
            yield namespace_obj

    @property
    def userid(self):
        raise NotImplementedError()

    def create_namespace(self):
        raise NotImplementedError()

    def create_repository(self):
        raise NotImplementedError()
