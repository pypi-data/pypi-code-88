import hashlib
import os

import git
import sh

from fedeproxy.interfaces.dvcs import DVCS


class Git(DVCS):
    def __init__(self, **kwargs):
        self.args = kwargs
        self.d = os.path.join(self.args["dir"], hashlib.sha1(self.args["url"].encode("ascii")).hexdigest())
        self.g = sh.git.bake("-C", self.d)

    def directory(self):
        return self.d

    def clone(self, branch):
        clone = not os.path.exists(self.d)
        if clone:
            sh.git.clone("-b", branch, self.args["url"], self.d)
        else:
            self.g.checkout(branch)
        self.r = git.Repo(self.d)
        return clone

    def pull(self, branch):
        if self.clone(branch) is True:
            return None
        self.g.fetch.origin(branch)
        if self.r.commit(branch) == self.r.commit(f"origin/{branch}"):
            return False
        self.g.checkout(branch)
        self.g.rebase(f"origin/{branch}")
        return True

    def push(self, branch):
        if self.clone(branch) is True:
            return None
        print(self.r.commit(branch))
        print(self.r.commit(f"origin/{branch}"))
        if self.r.commit(branch) == self.r.commit(f"origin/{branch}"):
            return False
        self.pull(branch)
        self.g.push("origin", branch)
        return True
