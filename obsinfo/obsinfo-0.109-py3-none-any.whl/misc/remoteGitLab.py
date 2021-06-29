import gitlab
import urllib
import json
import base64
import re
import os

# private token or personal token authentication

class gitLabFile(object):
    
    @staticmethod
    def get_gitlab_file(uri, read_file=True):
        
        gitlab_repository = os.environ.get('OBSINFO_GITLAB_REPOSITORY')
        project_path = os.environ.get('OBSINFO_PROJECTPATH')
        
        if not gitlab_repository or not project_path:
            raise ValueError("Dne or several environment variables, OBSINFO_GITLAB_REPOSITORY or \
                      OBSINFO_PROJECTPATH, are missing")
        
        pattern = gitlab_repository + "/"
        uri = re.sub(pattern, "", uri)
        
        gl = gitlab.Gitlab("http://" + gitlab_repository)
        
        project = gl.projects.get(project_path)
        #uri = urllib.parse.urlsplit(str(uri)).path
        #if uri[0] == '/': # gitlab.projects.get doesn't like an absolute path'
        #    uri = uri[1:]

        try:
            f = project.files.get(file_path=uri, ref='v0.109')
            if not read_file:
                return True
        except gitlab.exceptions.GitlabOperationError:
            if read_file:
                print(f'Error reading remote (gitlab) file: {uri}')
                return None               
            else:
                return False
        # get the decoded content. Two decodes are necessary, from 8character string to bytes and 
        # from bytes to a python string
        bytecontent = base64.b64decode(f.content)
        ret = bytecontent.decode("utf-8")

        return ret
    
    @staticmethod
    def isRemote(file):
        return re.match('^http:', file) or re.match('^https:', file)

#obsinfo/_examples2/Information_Files/network/BBOBS.INSU-IPGP,network.yaml/raw?ref=v0.109')

