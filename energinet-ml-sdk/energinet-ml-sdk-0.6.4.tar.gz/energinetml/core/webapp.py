import os
import sys
import subprocess


class WebAppEngine(object):
    def serve(self, project):
        raise NotImplementedError


class WsgiWebApp(WebAppEngine):
    """
    WSGI
    """
    def serve(self, project):
        os.chdir(os.path.join(project.path, 'src'))

        command = ('gunicorn', 'app:app')

        subprocess.check_call(
            command, stdout=sys.stdout, stderr=subprocess.STDOUT)


class AsgiWebApp(WebAppEngine):
    """
    ASGI
    """
    def serve(self, project):
        os.chdir(os.path.join(project.path, 'src'))

        command = ('uvicorn', 'app:app')

        subprocess.check_call(
            command, stdout=sys.stdout, stderr=subprocess.STDOUT)


class OpyratorWebApp(WebAppEngine):
    """
    opyrator
    """
    def serve(self, path):
        raise NotImplementedError
