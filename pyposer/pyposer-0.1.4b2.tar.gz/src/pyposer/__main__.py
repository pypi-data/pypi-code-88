#!/usr/bin/python3
# coding=utf-8

from sys import argv, exit
import click
import time
import subprocess
import json
import os
from pathlib import Path

import pyposer.libs.generate__pyposer as init_run
import pyposer.libs.colors as colors
from pyposer.libs.install__libs import install as installPkg, remove as removePkg
from pyposer.libs.exec__script import execCmd
from pyposer.libs.exec__venv import down, up
from pyposer.libs.create__venv import create

_VERSION = '0.1.4b2'
_FIRST_ARG = argv[1] if len(argv) > 1 else "install"
_SHELL = os.environ['SHELL'].split('/')[-1]
_HOME_DIR = str(Path.home())
_RCFILE = ".zshrc" if _SHELL == "zsh" else ".bashrc"
_BANNER = f"{colors.BOLD}pyposer {_FIRST_ARG} {_VERSION}{colors.ENDC}"
_PYPOSER_EXIST = os.path.exists('pyposer.json')


def print_version(ctx, param, value):
    if value:
        click.echo(_VERSION)
        exit()
    else:
        pass


@click.group()
@click.option("-v",
              "--version",
              is_flag=True,
              help="show version number and exit",
              callback=print_version)
def group(version):
    pass


@group.command(short_help="start a python project with pyposer.")
@click.option("-y",
              "--yes",
              is_flag=True,
              help="Set default values in pyposer.json")
def init(yes):
    start_time = time.time()
    create()
    init_run.createPyposer(click, yes)
    click.echo(f"done in {time.time() - start_time:.2f}")


@group.command(
    short_help="Installs a package and any packages that it depends on.")
@click.option("-D", "--dev", is_flag=True, help="install how devDependencies")
@click.option("-q",
              "--quiet",
              is_flag=True,
              help="install how devDependencies")
@click.argument("libs", required=True, nargs=-1)
def add(dev, libs, quiet):
    start_time = time.time()
    for lib in libs:
        installPkg(lib, dev, quiet)
    click.echo(f"done in {time.time() - start_time:.2f}")


@group.command(short_help="Removes a package and updating your pyposer.json .")
@click.option("-q",
              "--quiet",
              is_flag=True,
              help="install how devDependencies")
@click.argument("libs", required=True, nargs=-1)
def remove(libs, quiet):
    start_time = time.time()
    for lib in libs:
        removePkg(lib, quiet)
    click.echo(f"done in {time.time() - start_time:.2f}")


@group.command(
    short_help='activates the virtual environment present in the directory.')
def activate():
    up(_SHELL)


@group.command(
    short_help='disables the virtual environment present in the directory.')
def deactivate():
    down(_SHELL)


@group.command(short_help='Runs a defined package script.')
@click.argument("cmd", required=True)
def run(cmd):
    click.echo(f"{colors.BOLD}{colors.GREY}$ {execCmd(cmd)}{colors.ENDC}")
    os.system(execCmd(cmd))


@group.command(short_help='used to install all dependencies for a project')
def install():
    with open('pyposer.json') as f:
        pyposer = json.load(f)
        if bool(pyposer['dependencies']):
            for pkg in list(pyposer['dependencies'].items()):
                package = f'{pkg[0]}=={pkg[1]}'
                installPkg(package)
        if bool(pyposer['devDependencies']):
            for pkg in list(pyposer['dependencies'].items()):
                package = f'{pkg[0]}=={pkg[1]}'
                group.commands['add'].callback(package, True, False)


def main():
    if "-" in _FIRST_ARG:
        pass
    elif not "activate" in _FIRST_ARG:
        print(_BANNER)
    if _PYPOSER_EXIST:
        if not _FIRST_ARG in list(
                group.commands.keys()) and not "-" in _FIRST_ARG:
            group.commands['run'].callback(_FIRST_ARG)
            exit()
        if _FIRST_ARG == 'install':
            group.commands['install'].callback()
            exit()
    group()


if __name__ == '__main__':
    main()