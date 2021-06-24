#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pathlib as pt

import click

from ioproc.config import configProvider
from ioproc.defaults import *
from ioproc.logger import mainlogger as log
from ioproc.logger import datalogger as dlog
from ioproc.datamanager import DataManager
from ioproc.actionmanager import getActionManager
from ioproc.tools import freeze, setupFolderStructure
from ioproc.exceptions import CheckPointError, UnknownAction, UnknownActionModule


__author__ = ["Benjamin Fuchs", "Judith Vesper", "Felix Nitsch"]
__copyright__ = "Copyright 2020, German Aerospace Center (DLR)"
__credits__ = ["Niklas Wulff", "Hedda Gardian", "Gabriel Pivaro", "Kai von Krbek"]

__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = "Felix Nitsch"
__email__ = "ioProc@dlr.de"
__status__ = "Production"


IOPROCINSTALLROOT = pt.Path(__file__).resolve().parent
SCHEMAPATH = pt.Path(IOPROCINSTALLROOT, "schema")
HOME = pt.Path.home()

defaultConfigContent = defaultConfigContent.format(IOPROCINSTALLROOT.as_posix())


@click.group()
@click.pass_context
def ioproc(ctx):
    ctx.ensure_object(dict)


@ioproc.command(help="setup default folder structure")
@click.option("--workflowname", default="workflow1", help="name of your workflow")
def setupfolders(workflowname):
    setupFolderStructure(workflowname)


@ioproc.command(
    help="create all necessary files for workflow in current folder or at userconfig location"
)
@click.option(
    "--path", "-p", default=None, help="path to folder where to create workflow"
)
def setupworkflow(path):
    if path is None:
        path = pt.Path.cwd()
    else:
        path = pt.Path(path)

    if not path.exists():
        raise IOError(f"workflow folder not found: {path.as_posix()}")

    p = path / "user.yaml"
    if not p.exists():
        with p.open("w") as opf:
            opf.write(defaultUserContent)

    p = path / "run.py"
    if not p.exists():
        with p.open("w") as opf:
            opf.write(defaultRunPyFile)


def format_override(ctx, self, s):
    try:
        d = tuple(i.strip().split("=") for i in s)
        d = dict(d)
    except:
        raise click.exceptions.BadArgumentUsage(
            f"the overwrites need to be of shape: ioproc overwrites a=1 b=2"
        )

    return d


@ioproc.command(help="setup default folder structure")
@click.option("--useryaml", "-u", default=None, help="path to user.yaml")
@click.option(
    "--override/--no-override",
    "-o",
    default=False,
    help="override values of the user.yaml (based on jinja2 syntax)",
)
@click.argument("overridedata", nargs=-1, callback=format_override)
def execute(useryaml, override, overridedata):

    if override and not overridedata:
        raise click.exceptions.ClickException("Missing override data")
    elif not override and overridedata:
        raise click.exceptions.ClickException(
            "overrides need to be specified with ioproc execute -o"
        )

    _execute(useryaml, overridedata=overridedata, return_data=False)


def _execute(
    path_to_user_yaml: pt.Path,
    overridedata: [dict, None] = None,
    return_data: bool = False,
) -> [dict, None]:
    if overridedata is None:
        overridedata = {}

    userConfigPath = pt.Path(pt.Path.cwd(), "user.yaml")

    if path_to_user_yaml is not None:
        userConfigPath = pt.Path(path_to_user_yaml)

    configProvider.setPathes(userConfigPath=userConfigPath,)

    print(overridedata)
    config = configProvider.get(overridedata)

    if "debug" in config["user"] and "log_level" in config["user"]["debug"]:
        log.setLevel(config["user"]["debug"]["log_level"])
        dlog.setLevel(config["user"]["debug"]["log_level"])
    else:
        log.setLevel("INFO")
        dlog.setLevel("INFO")

    actionMgr = getActionManager(config)
    assert (
        len(actionMgr) > 0
    ), "ActionManager is not defined. Ensure 'actionFolder' path in 'user.yaml' is set correctly."
    dmgr = DataManager(config["user"]["debug"]["enable development mode"])

    log.info("starting workflow")

    log.debug("commencing action calling")

    FROMCHECKPOINT = config["user"]["fromCheckPoint"] != "start"

    if FROMCHECKPOINT:
        given_tag = config["user"]["fromCheckPoint"]
        if not pt.Path("./Cache_{}.h5f".format(given_tag)).is_file():
            message = "cannot find cache file with given tag name `{}`".format(
                given_tag
            )
            log.exception(message)
            raise Exception(message)

    CHECKPOINTDEFINEDINWORKFLOW = False

    # this is a cross check loop to identify early problems in the workflow.
    for iActionInfo in config["user"]["workflow"]:
        iActionInfo = iActionInfo[list(iActionInfo.keys())[0]]
        if iActionInfo["project"] not in actionMgr:
            raise UnknownActionModule(
                f'The action module "{iActionInfo["project"]}" is not known to ioproc.\n'
                f'please check in the action folder for it: "{config["user"]["actionFolder"]}"'
            )

        if iActionInfo["call"] not in actionMgr[iActionInfo["project"]]:
            raise UnknownAction(
                f'The action "{iActionInfo["call"]}" is not known to ioproc.\n'
                f'please check in the action folder "{config["user"]["actionFolder"]}"\n'
                f'in the module {iActionInfo["project"]} for the action.'
            )

    for iActionInfo in config["user"]["workflow"]:
        iActionInfo = iActionInfo[list(iActionInfo.keys())[0]]
        if (
            FROMCHECKPOINT
            and "tag" in iActionInfo
            and iActionInfo["tag"] != config["user"]["fromCheckPoint"]
        ):
            continue
        elif (
            FROMCHECKPOINT
            and "tag" in iActionInfo
            and iActionInfo["tag"] == config["user"]["fromCheckPoint"]
        ):
            FROMCHECKPOINT = False
            CHECKPOINTDEFINEDINWORKFLOW = True
            dmgr.fromCache(config["user"]["fromCheckPoint"], iActionInfo)
            log.info(
                'reading from cache for tag "{}"'.format(
                    config["user"]["fromCheckPoint"]
                )
            )
            continue
        elif FROMCHECKPOINT:
            continue

        log.debug('executing action "' + iActionInfo["call"] + '"')
        dmgr.entersAction(iActionInfo)

        try:
            actionMgr[iActionInfo["project"]][iActionInfo["call"]](
                dmgr, config, freeze(iActionInfo)
            )
        except Exception as e:
            log.exception(
                'Fatal error during execution of action "'
                + iActionInfo["call"]
                + '":\nData manager log:\n'
                + dmgr.report()
            )
            raise e
        dmgr.leavesAction()

    if not CHECKPOINTDEFINEDINWORKFLOW and FROMCHECKPOINT:
        raise CheckPointError(
            f'The requested checkpoint "{config["user"]["fromCheckPoint"]}" '
            f"is not defined in the workflow!"
        )

    if return_data:
        return dmgr.export_to_dict()


if __name__ == "__main__":
    ioproc()
