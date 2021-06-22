import logging
import pathlib

import git

LOG = logging.getLogger(__name__)


def is_git_repo(path: pathlib.PosixPath) -> bool:
    try:
        git.Repo(path)
    except git.exc.InvalidGitRepositoryError:
        return False

    return True


class Repository:
    def __init__(
        self,
        name: str,
        namespace: str,
        ssh_url: str,
        http_url: str,
        localfs_url: pathlib.PosixPath = None,
        description: str = None,
    ):
        self.name = name
        self.namespace = namespace
        self.ssh_url = ssh_url
        self.http_url = http_url
        self.localfs_url = localfs_url
        self.description = description

    def __repr__(self):
        return f"{self.namespace}/{self.name}"

    def clone(self, base_path: pathlib.PosixPath, name: str = None):
        LOG.info(f"Cloning repository: {self}")
        git.Git().clone(self.ssh_url, str(base_path / (name or self.name)), "--mirror")

    def update_mirror(self, base_path: pathlib.PosixPath, name: str = None):
        LOG.info(f"Updating repository: {self}")
        repo = git.Repo(str(base_path / (name or self.name)))
        repo.remote().fetch()

    def clone_or_update(self, base_path: pathlib.PosixPath, name: str = None):
        LOG.info(f"Processing repository: {self}")
        base_path = pathlib.Path(base_path)
        path = base_path / (name or self.name)
        if path.is_dir():
            LOG.info(f"Repository directory already exists: {path}")
            try:
                git.Repo(path)
                self.update_mirror(path)
                return
            except (git.exc.InvalidGitRepositoryError):
                pass
        LOG.info(
            "Repository directory does not exist or is not a " f"valid gir repo: {path}"
        )
        self.clone(base_path, name)
        return
