import json
import os
from certora_cli.certoraUtils import debug_print_
from typing import Any, Dict, List
import subprocess
import argparse
from certora_cli.certoraUtils import Mode

CERTORA_METADATA_FILE = ".certora_metadata.json"


# jsonify sets as lists
class MetadataEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Mode):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class RunMetaData:
    """
    Carries information about a run of CVT.
    This includes
      - which arguments CVT was started with,
      - information about the state (snapshot) of the git repository that CVT was called in (we expect this to be the
        repository where the program and spec lie in that CVT was started on).

    arguments:
    raw_args -- arguments to `certoraRun.py`, basically python's sys.argv list
    conf -- configuration as processed by certoraConfigIO
    args -- arguments after parsing by certoraRun, includes default values
    origin -- origin URL of the git repo
    revision -- commit hash of the currently checked-out revision
    branch -- branch name of the currently checked-out revision
    cwd_relative -- current working directory, relative to the root of the git repository
    dirty -- true iff the git repository has changes (git diff is not empty)
    """
    def __init__(self, raw_args: List[str], conf: Dict[str, Any], args: Dict[str, str], origin: str, revision: str,
                 branch: str, cwd_relative: str, dirty: bool):
        self.raw_args = raw_args
        self.conf = conf
        self.args = args
        self.origin = origin
        self.revision = revision
        self.branch = branch
        self.cwd_relative = cwd_relative
        self.dirty = dirty

    def __repr__(self) -> str:
        return (
            f" raw_args: {self.raw_args}\n" +
            f" conf: {self.conf}\n" +
            f" args: {self.args}\n" +
            f" origin: {self.origin}\n" +
            f" revision: {self.revision}\n" +
            f" branch: {self.branch}\n" +
            f" cwd_relative: {self.cwd_relative}\n" +
            f" dirty: {self.dirty}\n"
        )

    def dump(self) -> None:
        debug_print_(f"writing {CERTORA_METADATA_FILE}")
        if self.__dict__:  # dictionary containing all the attributes defined for GitInfo
            try:
                with open(CERTORA_METADATA_FILE, 'w+') as output_file:
                    json.dump(self.__dict__, output_file, indent=4, sort_keys=True, cls=MetadataEncoder)
            except Exception:
                print(f"failed to write meta data file {CERTORA_METADATA_FILE}")


def collect_run_metadata(wd: str, raw_args: List[str], conf_dict: Dict[str, Any], args: argparse.Namespace,
                         debug: bool = False) -> RunMetaData:
    # collect information about current git snapshot

    git_present_out = subprocess.run(['git', '--version'], cwd=wd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    is_git_present = git_present_out.returncode == 0

    if not is_git_present:
        debug_print_('no git executable found in {wd}, not collecting any repo metadata', debug)
        return RunMetaData(list(), dict(), dict(), "", "", "", "", False)

    sha_out = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=wd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sha = sha_out.stdout.decode().strip()

    branch_name_out = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=wd, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
    branch_name = branch_name_out.stdout.decode().strip()

    origin_out = subprocess.run(['git', 'remote', 'get-url', 'origin'], cwd=wd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    origin = origin_out.stdout.decode().strip()

    base_dir_out = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=wd, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
    base_dir = base_dir_out.stdout.decode().strip()
    cwd_abs = os.path.abspath(wd)
    cwd_relative = os.path.relpath(cwd_abs, base_dir)

    dirty_out = subprocess.run(['git', 'diff', '--shortstat'], cwd=wd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dirty = dirty_out.stdout.decode().strip() != ''

    data = RunMetaData(raw_args, conf_dict, vars(args), origin, sha, branch_name, cwd_relative, dirty)

    debug_print_(f' collected data:\n{str(data)}', debug)

    return data
