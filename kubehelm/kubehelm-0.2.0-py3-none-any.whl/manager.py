from argparse import ArgumentParser

from kubehelm.handler import handle_args

import sys
import os


class Manager:
    actions_list = ['install', 'update', 'delete', 'list']

    def __init__(self):
        self.prog_name = os.path.basename(sys.argv[0])
        if self.prog_name == '__main__.py':
            self.prog_name = 'python -m kubehelm'

    def execute(self):
        parser = ArgumentParser(prog=self.prog_name,
                                description='Asim program.')

        parser.add_argument('action', choices=self.actions_list)
        parser.add_argument('app_name', help='The app name')
        parser.add_argument('-n', '--namespace', help='The app name')
        parser.add_argument('-m', '--image', help='The app name')
        parser.add_argument('-t', '--tag', help='The app name')
        handle_args(parser.parse_args())


def execute_from_command_line():
    manage = Manager()
    manage.execute()
