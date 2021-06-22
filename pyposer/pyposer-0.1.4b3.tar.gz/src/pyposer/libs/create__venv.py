import os
import shutil
import sys
from pip._internal.cli.main import main
from virtualenv import cli_run, run


def create():
    cli_run(['venv'])
    sys.stdout = open(os.devnull, 'w')
    for lib in ['click', 'virtualenv', 'inquirer']:
        main([
            'install',
            f'--target={os.getcwd()}/venv/lib/python3.9/site-packages', lib
        ])
    sys.stdout = sys.__stdout__
    # for lib in [
    #         'click', 'virtualenv', 'six', 'filelock', 'appdirs', 'distlib'
    # ]:
    #     if os.path.exists(f'/usr/lib/python3.9/site-packages/{lib}'):
    #         if not os.path.exists(
    #                 f'{os.getcwd()}/venv/lib/python3.9/site-packages/{lib}'):
    #             shutil.copytree(
    #                 f'/usr/lib/python3.9/site-packages/{lib}',
    #                 f'{os.getcwd()}/venv/lib/python3.9/site-packages/{lib}')
    #     else:
    #         if not os.path.exists(
    #                 f'{os.getcwd()}/venv/lib/python3.9/site-packages/{lib}.py'
    #         ):
    #             shutil.copyfile(
    #                 f'/usr/lib/python3.9/site-packages/{lib}.py',
    #                 f'{os.getcwd()}/venv/lib/python3.9/site-packages/{lib}.py')
