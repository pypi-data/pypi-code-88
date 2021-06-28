from argparse import ArgumentParser

from kubehelm.objects import ListK8sObjects
from kubehelm import apps

import sys
import os


class Handler:
    def execute(self, action, manifest, **kwargs):
        if action == 'list':
            namespace = kwargs.get('namespace') or 'default'
            print(ListK8sObjects(namespace).deployments())
            print("="*99)
            print(ListK8sObjects(namespace).pods())
            return
        try:
            app_class = getattr(apps, manifest.capitalize())
        except (IndexError, AttributeError) as err:
            self.list_all_apps()
            print("="*80)
            raise err
        context = self.read_required_context(app_class, **kwargs)
        app = app_class(**context)
        results = getattr(app, action)()
        print(results)

    def list_all_apps(self, ):
        ignore = ['RunAppScript', 'Manifest', 'Helm', ]
        for name in apps.__dict__.keys():
            if name not in ignore and not name.startswith('_'):
                print(name)

    def read_required_context(self, app_class, **kwargs):
        context = {}
        if hasattr(app_class, "required_context") and app_class.required_context:
            for field in app_class.required_context:
                if kwargs.get(field):
                    context[field] = kwargs.get(field)
                else:
                    default = app_class.default_context.get(field) or ""
                    value = input('%s (%s): ' % (field, default))
                    context[field] = value or default
        return context


class Manager(Handler):
    actions_list = ['install', 'update', 'delete', 'list']
    describe = 'Asim program.'

    def __init__(self):
        self.prog_name = os.path.basename(sys.argv[0])
        if self.prog_name == '__main__.py':
            self.prog_name = 'python -m kubehelm'

    def execute(self):
        parser = ArgumentParser(prog=self.prog_name, description=self.describe)

        parser.add_argument('action', choices=self.actions_list)
        parser.add_argument('manifest', help='The manifest name')
        parser.add_argument(
            '-n', '--namespace',
            dest='namespace',
            help='The app name')

        parser.add_argument(
            '-a', '--name',
            dest='app_name',
            help='The app name name')

        parser.add_argument(
            '-i', '--image',
            dest='image_name',
            help='The app name')

        parser.add_argument(
            '-t', '--tag',
            dest='image_tag',
            help='The app name')

        args = parser.parse_args()

        super().execute(**args.__dict__)


def execute_from_command_line():
    manage = Manager()
    manage.execute()
