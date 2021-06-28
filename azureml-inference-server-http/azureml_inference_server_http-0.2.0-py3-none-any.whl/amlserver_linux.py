import os
import sys
import argparse

import gunicorn.app.base
from .constants import DEFAULT_HOST, DEFAULT_PORT, DEFAULT_WORKER_COUNT


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def run(host, port, worker_count):
    import create_app

    options = {
        'bind': f"{host}:{port}",
        'workers': worker_count,
        'preload_app': False,
        'logconfig': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf')
    }
    StandaloneApplication(create_app.create(), options).run()


if __name__ == "__main__":
    run(DEFAULT_HOST, DEFAULT_PORT, DEFAULT_WORKER_COUNT)
