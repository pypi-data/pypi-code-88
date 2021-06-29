#!/usr/bin/env python
#
# tools: functions for getting info from toolsheds
from bioblend import toolshed

def get_toolshed_client(url):
    ts = toolshed.ToolShedInstance(url=url)
    return toolshed.repositories.ToolShedRepositoryClient(ts)

class ToolshedRepo(object):
    def __init__(self,shed,repo_data):
        self.toolshed = shed
        self.name = repo_data['name']
        self.owner = repo_data['owner']
        self.description = repo_data['description']
        self.id = repo_data['id']
        self.revisions = []
    def add_revision(self,revision_data):
        revision = ToolshedRepoRevision(self,revision_data)
        revision.get_info()
        self.revisions.append(revision)
        # Sort into order (newest to oldest)
        self.revisions = sorted(self.revisions,
                                key=lambda r: int(r.revision_number))

class ToolshedRepoRevision(object):
    def __init__(self,repo,revision_data):
        self.repo = repo
        self.changeset_revision = revision_data['changeset_revision']
        self.revision_number = None
    def get_info(self,revision_info=None):
        if revision_info is None:
            shed_client = get_toolshed_client(self.repo.toolshed)
            revision_info = shed_client.get_repository_revision_install_info(
                self.repo.name,
                self.repo.owner,
                self.changeset_revision)
            # Returns a list of the following dictionaries:
            # - a dictionary defining the repository
            # - a dictionary defining the repository revision
            #   (RepositoryMetadata)
            # - a dictionary including the additional information
            #   required to install the repository
            revision_info = revision_info[2][self.repo.name]
            self.revision_number = revision_info[3]

class Toolshed(object):
    def __init__(self,url):
        self.url = url
        self.repos = []
        # Get a ToolShedInstance
        print "Listing tools in %s" % self.url
        shed_client = get_toolshed_client(self.url)
        # Get repositories
        repos = shed_client.get_repositories()
        # Get revisions
        revisions = shed_client.repository_revisions()
        # Populate the object
        for repo_data in repos:
            repo = ToolshedRepo(self.url,repo_data)
            print "Getting revisions for %s/%s" % (repo.owner,
                                                   repo.name)
            repo_revisions = filter(lambda r:
                                    r['repository_id'] == repo.id,
                                    revisions)
            for r in repo_revisions:
                repo.add_revision(r)
            for r in repo.revisions:
                print "- %s:%s" % (r.revision_number,
                                   r.changeset_revision)

if __name__ == "__main__":
    Toolshed("toolshed.g2.bx.psu.edu")

        
        
            
