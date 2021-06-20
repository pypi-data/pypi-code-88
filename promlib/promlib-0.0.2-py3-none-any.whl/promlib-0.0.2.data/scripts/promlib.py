import sys
from pathlib import PurePosixPath, Path
from os import getppid, getpid
from shutil import which
from pynpm import YarnPackage as yarn
from randomname import get_name
from time import sleep
from tqdm import tqdm
from zipfile import ZipFile as unzip
import requests as reqs

def glue(*argp):
    """
    Takes n argument paths and returns a path.
    Tolerates a medley of strings and paths in argp.
    Not good yet.
    """

    # List of map & iterable str caster
    # Helps make logic below pretty
    lmap = lambda f, l: list(map(f, l))
    istr = lambda s: str(s)

    paths = lmap(istr, argp)

    if all(paths):
        parts = argp
        glued_path = Path.cwd().joinpath(*parts)

        return glued_path

def knows(app):
    """
    Returns True if the host has app under /usr/local/bin in $PATH.
    """
    bin_path = PurePosixPath('/usr/local/bin/')
    app_path = glue(bin_path, app)

    cmd = which(app_path)
    if cmd is not None:
        return True
    else:
        return False

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', getppid())
    print('child  process:', getpid())


def init(home):
    """
    Glues a preset path to the default name this app creates and creates the 
    home directory.
    """

    # Make a home dir in root if we don't have one
    if not home.exists():
        home.mkdir(parents=False, exist_ok=True)
        return home

    # Tell me where home is if you already made it
    else:
        return home


def mkproj(homedir):
    """
    Glues the home path to a new random project name which becomes the current
    project directory.
    """
    projname = Path(get_name())
    projdir = glue(homedir, projname)

    if projdir.exists():
        mkproj(projdir)
        return projdir
    else:
        projdir.mkdir(parents=True, exist_ok=True)
        return projdir


def getrepo(thing, origin, projdir):
    """
    """
    parsed = thing.split("/")

    if origin == "github":
        user = parsed[0]
        repo = parsed[1]
        branch = parsed[2]
        url = f"https://github.com/{user}/{repo}/archive/refs/heads/{branch}.zip"
        fname = Path(f"{repo}.zip")

    pkg_path = glue(projdir, fname)
    app_dir = glue(projdir, repo)

    # Download process
    r = reqs.get(url, stream=True, allow_redirects=True)

    if r.status_code == 200:
        bytesize = int(r.headers.get('content-length', 0))
        pbar = tqdm(total=bytesize, unit='iB', unit_scale=True)
        with open(pkg_path, 'wb') as file:
            for data in r.iter_content(1024):
                pbar.update(len(data))
                file.write(data)
        pbar.close()

        # Unpackage process
        with unzip(pkg_path, 'r') as zip_ref:
            zip_ref.extractall(app_dir)
            pkg_path.unlink()
    else:
        print("I didn't get a 200.")

    return app_dir


def run_project(app_dir, yarn_commands, wait):
    pkg = yarn(f"{app_dir}/wind-main/package.json",
                      commands=yarn_commands)

    insproc = pkg.install(wait=wait)
    insproc.wait()

    runproc = pkg.start(wait=wait)
    runproc.wait()

    # Return their id's

def animator():
    pass
