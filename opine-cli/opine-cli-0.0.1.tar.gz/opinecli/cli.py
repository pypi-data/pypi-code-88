import fire
# from . import config
# from . import auth
# from . import projects
from opinecli import init, config, auth, projects, data

def version():
    print("Opine CLI version 0.0.1")

class Actions(object):
    def __init__(self):
        self.config = config.Config()
        self.auth = auth.SignIn()
        self.projects = projects.Projects()
        self.data = data.Data()

    def init(self,endpoint="https://api.opine.world"):
        init.Init().start(endpoint)

    def version(self):
        self.version = version()

def main():
    fire.Fire(Actions)

if __name__ == '__main__':
    main()