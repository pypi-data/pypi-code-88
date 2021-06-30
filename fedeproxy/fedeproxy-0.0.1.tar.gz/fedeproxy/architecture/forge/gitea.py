import logging
import time

import requests

from fedeproxy.common.retry import retry
from fedeproxy.interfaces.forge import Forge

logger = logging.getLogger(__name__)


class Gitea(Forge):
    def __init__(self, url):
        self.url = url
        self._session()

    def _session(self):
        self.s = requests.Session()
        self.s.api = f"{self.url}/api/v1"

    def login(self, username, password):
        r = self.s.post(
            f"{self.s.api}/users/{username}/tokens",
            auth=(username, password),
            json={
                "name": f"TEST{time.time()}",
            },
        )
        r.raise_for_status()
        self.set_token(r.json()["sha1"])

    def set_token(self, token):
        self.s.headers["Authorization"] = f"token {token}"

    def user_delete(self, user):
        info = self.user_get(user)
        if info is None:
            return False
        while True:
            r = self.s.delete(f"{self.s.api}/admin/users/{user}")
            if r.status_code == 404:
                break
            r.raise_for_status()
        return True

    def user_get(self, user):
        r = self.s.get(f"{self.s.api}/users/search?q={user}")
        r.raise_for_status()
        found = r.json()
        if found and found["ok"] and len(found["data"]):
            info = found["data"][0]
            info["username"] = user
            return info
        else:
            return None

    def user_create(self, user, email):
        info = self.user_get(user)
        if info is None:
            r = self.s.post(
                f"{self.s.api}/admin/users",
                data={
                    "username": user,
                    "email": email,
                    "password": "something",
                },
            )
            logger.debug(r.text)
            r.raise_for_status()
            info = r.json()
        return info

    def project_delete(self, user, namespace, project):
        info = self.project_get(user, namespace, project)
        if info is None:
            return False
        r = self.s.delete(f"{self.s.api}/repos/{user}/{project}")
        r.raise_for_status()
        while self.project_get(user, namespace, project) is not None:
            time.sleep(1)
        return True

    def project_get(self, user, namespace, project):
        r = self.s.get(f"{self.s.api}/repos/{user}/{project}")
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None

    class DeletionInProgress(Exception):
        pass

    @retry(DeletionInProgress, tries=5)
    def _project_create(self, admin, user, namespace, project, **data):
        data.update(
            {
                "name": project,
            }
        )
        r = self.s.post(f"{self.s.api}/admin/users/{user}/repos", data=data)
        logger.info(r.text)
        if r.status_code == 201:
            return r.json()
        r.raise_for_status()

    def project_create(self, admin, user, namespace, project, **data):
        info = self.project_get(user, namespace, project)
        if info is None:
            return self._project_create(admin, user, namespace, project, **data)
        else:
            return info

    def project_export(self, user, namespace, project, filename):
        assert 0, "not implemented"
