import os

import pytest

from .gitea import Gitea


@pytest.fixture
def gitea():
    ip = os.environ.get("MY_IP", "0.0.0.0")
    gitea = Gitea(f"http://{ip}:8781")
    gitea.login("gitea_admin", "admin123")
    return gitea


@pytest.mark.gitea
def test_project_create(gitea):
    user = "testuser1"
    email = "testuser1@example.com"
    gitea.user_create(user, email)
    gitea.project_delete(user, user, "testproject")
    assert gitea.project_get(user, user, "testproject") is None
    p = gitea.project_create("root", user, user, "testproject")
    assert p["id"] == gitea.project_create("root", user, user, "testproject")["id"]
    assert gitea.project_delete(user, user, "testproject") is True
    assert gitea.project_delete(user, user, "testproject") is False
    assert gitea.user_delete(user) is True


@pytest.mark.gitea
def test_user_create(gitea):
    user = "testuser1"
    email = "testuser1@example.com"
    gitea.user_delete(user)
    u = gitea.user_create(user, email)
    assert u["id"] == gitea.user_create(user, email)["id"]
    assert gitea.user_delete(user) is True
    assert gitea.user_get(user) is None
    assert gitea.user_delete(user) is False
