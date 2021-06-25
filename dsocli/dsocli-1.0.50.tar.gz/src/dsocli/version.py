import os
import pathlib

VERSION = '1.0'

__last_version = os.getenv('DSO_LAST_VERSION') or f"{VERSION}.0"

def get_new_release_number():
    versions =  __last_version.split('.')
    major1 = versions[0]
    minor1 = versions[1]
    release1 = int(versions[2])

    major2, minor2 = VERSION.split('.')

    if major2 == major1 and minor2 == minor1:
        release2 = release1 + 1
    else:
        release2 = 1
    
    return release2

# ### if called from setup.py 
# if __name__ == '__main__':
#     release_number = get_new_release_number()
#     dso_version = f"{VERSION}.{release_number}"
#     path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'src', 'dsocli', '.version')
#     with open(path, 'w') as f:
#         f.write(__version__)
# else:
#     path = os.path.join(pathlib.Path(__file__).parent.resolve(), '.version')
#     with open(path, 'r') as f:
#         __version__ = f.read(path).strip()

release_number = get_new_release_number()
dso_version = f"{VERSION}.{release_number}"
