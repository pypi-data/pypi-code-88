import gzip
import os

import pytest

from .gitlab import GitLab


@pytest.fixture
def gitlab():
    ip = os.environ.get("MY_IP", "0.0.0.0")
    gitlab = GitLab(f"http://{ip}:8181")
    gitlab.login("root", "Wrobyak4")
    return gitlab


@pytest.mark.gitlab
def test_project_create(gitlab):
    user = "testuser1"
    email = "testuser1@example.com"
    gitlab.user_create(user, email)
    gitlab.project_delete(user, user, "testproject")
    assert gitlab.project_get(user, user, "testproject") is None
    p = gitlab.project_create("root", user, user, "testproject")
    assert p["id"] == gitlab.project_create("root", user, user, "testproject")["id"]
    assert gitlab.project_delete(user, user, "testproject") is True
    assert gitlab.project_delete(user, user, "testproject") is False
    assert gitlab.user_delete(user) is True


@pytest.mark.gitlab
def test_user_create(gitlab):
    user = "testuser1"
    email = "testuser1@example.com"
    gitlab.user_delete(user)
    u = gitlab.user_create(user, email)
    assert u["id"] == gitlab.user_create(user, email)["id"]
    assert gitlab.user_delete(user) is True
    assert gitlab.user_delete(user) is False


@pytest.mark.gitlab
def test_issue_create(gitlab):
    gitlab.project_delete("root", "root", "testproject")
    p = gitlab.project_create("root", "root", "root", "testproject")
    title = "THE TITLE"
    i = gitlab.issue_create(p["id"], title)
    assert i["id"] == gitlab.issue_get(p["id"], i["iid"])["id"]
    assert gitlab.issue_delete(p["id"], i["iid"]) is True
    assert gitlab.issue_get(p["id"], i["iid"]) is None
    assert gitlab.issue_delete(p["id"], i["iid"]) is False
    assert gitlab.project_delete("root", "root", "testproject") is True


@pytest.mark.gitlab
def test_project_export(gitlab, tmpdir):
    gitlab.project_delete("root", "root", "testproject")
    gitlab.project_create("root", "root", "root", "testproject")
    exported = f"{tmpdir}/testproject.tar.gz"
    gitlab.project_export("root", "root", "testproject", exported)
    assert gzip.open(exported)
