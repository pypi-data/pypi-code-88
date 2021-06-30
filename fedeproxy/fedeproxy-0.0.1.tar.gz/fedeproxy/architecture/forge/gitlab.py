import copy
import logging
import os
import time

import requests
from django.conf import settings

from fedeproxy.common.retry import retry
from fedeproxy.interfaces.forge import Forge

logger = logging.getLogger(__name__)


#
# https://docs.gitlab.com/ce/api/oauth2.html#resource-owner-password-credentials
#
class GitLab(Forge):
    def __init__(self, url):
        self.url = url
        self._session()

    def _session(self):
        self.s = requests.Session()
        if "REQUESTS_CA_BUNDLE" not in os.environ:
            self.s.verify = settings.CERTS_DIR
        self.s.api = self.url + "/api/v4"

    def certs(self, certs):
        self.s.verify = certs

    def login(self, username, password):
        r = self.s.post(
            self.url + "/oauth/token",
            json={
                "username": username,
                "password": password,
                "grant_type": "password",
            },
        )
        r.raise_for_status()
        self.set_token(r.json()["access_token"])

    def set_token(self, token):
        self.s.headers["Authorization"] = f"Bearer {token}"

    def get_namespace_id(self, name):
        r = self.s.get(self.s.api + "/namespaces?search=" + name)
        r.raise_for_status()
        return r.json()[0]["id"]

    def group_members(self, group):
        r = self.s.get(self.s.api + f"/groups/{group}/members")
        r.raise_for_status()
        return r.json()

    def is_member_of_group(self, group, username):
        return any([x["username"] == username for x in self.group_members(group)])

    def is_self_member_of_group(self, group):
        r = self.s.get(f"{self.s.api}/user")
        r.raise_for_status()
        user = r.json()
        return self.is_member_of_group(group, user["username"])

    def issue_delete(self, project_id, issue_iid):
        info = self.issue_get(project_id, issue_iid)
        if info is None:
            return False
        r = self.s.delete(f"{self.s.api}/projects/{project_id}/issues/{issue_iid}")
        r.raise_for_status()
        return True

    def issue_get(self, project_id, issue_iid):
        r = self.s.get(f"{self.s.api}/projects/{project_id}/issues/{issue_iid}")
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None

    def issue_create(self, project_id, title, **data):
        data = copy.copy(data)
        data.update(
            {
                "title": title,
            }
        )
        r = self.s.post(f"{self.s.api}/projects/{project_id}/issues", data=data)
        logger.debug(r.text)
        r.raise_for_status()
        return r.json()

    def user_delete(self, user):
        info = self.user_get(user)
        if info is None:
            return False
        while True:
            r = self.s.delete(f'{self.s.api}/users/{info["id"]}')
            if r.status_code == 404:
                break
            r.raise_for_status()
        return True

    def user_get(self, user):
        r = self.s.get(f"{self.s.api}/users?username={user}")
        r.raise_for_status()
        found = r.json()
        if found:
            return found[0]
        else:
            return None

    def user_create(self, user, email):
        info = self.user_get(user)
        if info is None:
            r = self.s.post(
                f"{self.s.api}/users",
                data={
                    "name": user,
                    "username": user,
                    "email": email,
                    "password": "something",
                    "force_random_password": True,
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
        r = self.s.delete(f'{self.s.api}/projects/{info["id"]}')
        r.raise_for_status()
        while self.project_get(user, namespace, project) is not None:
            time.sleep(1)
        return True

    def project_get(self, user, namespace, project):
        r = self.s.get(f"{self.s.api}/projects/{namespace}%2F{project}")
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None

    class DeletionInProgress(Exception):
        pass

    @retry(DeletionInProgress, tries=5)
    def _project_create(self, admin, user, namespace, project, **data):
        user_id = self.user_get(user)["id"]
        admin_id = self.user_get(admin)["id"]
        namespace_id = self.get_namespace_id(namespace)
        data.update(
            {
                "name": project,
                "namespace_id": int(namespace_id),
                "visibility": "public",
                "user_id": user_id,
            }
        )
        r = self.s.post(f"{self.s.api}/projects/user/{admin_id}", data=data)
        logger.info(r.text)
        if r.status_code == 201:
            return r.json()
        if r.status_code == 400 and ("still being deleted" in r.text or "has already been taken" in r.text):
            raise GitLab.DeletionInProgress()
        r.raise_for_status()

    def project_create(self, admin, user, namespace, project, **data):
        info = self.project_get(user, namespace, project)
        if info is None:
            return self._project_create(admin, user, namespace, project, **data)
        else:
            return info

    def project_export(self, user, namespace, project, filename):
        url = f"{self.s.api}/projects/{namespace}%2F{project}/export"
        r = self.s.post(url)
        assert r.status_code == 202, f"{r.status_code} {r.text}"

        while True:
            r = self.s.get(url)
            r.raise_for_status()
            status = r.json()["export_status"]
            logger.info(f"waiting {namespace}/{project} export: status is {status}")
            if status == "finished":
                break
            time.sleep(1)
        logger.info(f"download {namespace}/{project} into {filename}")
        with self.s.get(f"{url}/download", stream=True) as r:
            r.raise_for_status()
            with open(filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return True

    def create_api_application(self, domain):
        callbacks = [
            f"https://api.{domain}/accounts/gitlab/login/callback/",
        ]
        r = self.s.post(
            self.s.api + "/applications",
            json={
                "name": "api",
                "redirect_uri": "\n".join(callbacks),
                "scopes": "api\nread_user",
            },
        )
        logger.debug(r.text)
        r.raise_for_status()
        j = r.json()
        return j["application_id"], j["secret"]

    def ensure_group_exists(self, name, **kwargs):
        r = self.s.get(f"{self.s.api}/groups/{name}")
        if r.status_code == 200:
            return
        args = {"name": name, "path": name}
        args.update(kwargs)
        r = self.s.post(f"{self.s.api}/groups", json=args)
        r.raise_for_status()
