import os
import pathlib

VERSION = '1.0'

def get_new_release_number():
    last_versions = (os.getenv('DSO_LAST_VERSION') or f"{VERSION}.0").split('.')
    major1 = last_versions[0]
    minor1 = last_versions[1]
    release1 = int(last_versions[2])

    major2, minor2 = VERSION.split('.')

    if major2 == major1 and minor2 == minor1:
        release2 = release1 + 1
    else:
        release2 = 1
    
    return release2

### if called from setup.py 
if __name__ == '__main__':
    path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'src', 'dsocli', '.override_release_number')
    # if os.path.exists(path):
    #     with open(path, 'r') as f:
    #         dso_release_number = f.read(path).strip()
    # else:
    #     dso_release_number = get_new_release_number()
    dso_release_number = 53
    dso_version = f"{VERSION}.{dso_release_number}"
# else:
#     # path = os.path.join(pathlib.Path(__file__).parent.resolve(), '.version')
#     # with open(path, 'r') as f:
#     #     __version__ = f.read(path).strip()
#     from importlib.metadata import version
#     dso_version = version('dsocli')

