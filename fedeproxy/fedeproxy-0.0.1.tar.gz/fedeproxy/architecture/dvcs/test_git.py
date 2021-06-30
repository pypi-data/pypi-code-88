import os
from contextlib import contextmanager

import sh

from .git import Git


def test_git_clone(git_repository, tmpdir):
    g = Git(dir=tmpdir, url=git_repository)
    assert g.clone("master") is True
    assert os.path.exists(f"{g.directory()}/README.md")
    assert g.clone("master") is False


def modify_content(d, f, content):
    open(f"{d}/{f}", "w").write(content)
    sh.git("-C", d, "add", f)
    sh.git("-C", d, "commit", "-m", f"modify {f}")


@contextmanager
def git_repository_checkout(d):
    sh.git("-C", d, "checkout", "master")
    yield
    sh.git("-C", d, "checkout", "otherbranch")


def test_git_pull(git_repository, tmpdir):
    g = Git(dir=tmpdir, url=git_repository)
    assert g.pull("master") is None
    assert g.pull("master") is False
    assert os.path.exists(f"{g.directory()}/README.md")
    content = "SOMETHING ELSE"
    with git_repository_checkout(git_repository):
        modify_content(git_repository, "README.md", content)
    assert g.pull("master") is True
    assert open(f"{g.directory()}/README.md").read() == content


def test_git_push(git_repository, tmpdir):
    g = Git(dir=tmpdir, url=git_repository)
    assert g.push("master") is None
    assert g.push("master") is False
    info = "INFO"
    with git_repository_checkout(git_repository):
        modify_content(git_repository, "info.txt", info)
    readme = "README"
    modify_content(g.directory(), "README.md", readme)
    assert g.push("master") is True
    with git_repository_checkout(git_repository):
        assert open(f"{git_repository}/README.md").read() == readme
    assert open(f"{g.directory()}/info.txt").read() == info
