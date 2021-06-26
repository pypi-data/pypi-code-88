import inspect
import json
import logging
import os
import threading
from collections import defaultdict
from functools import partial
from typing import Any, Callable

import pkg_resources
from kikyo import Kikyo
from kikyo.settings import Settings
from pydantic import BaseModel

from kikyopp.annotation import KIKYOPP_SOURCE, KIKYOPP_SINK
from kikyopp.consumer.base import BaseConsumer
from kikyopp.consumer.kikyo import KikyoConsumer

log = logging.getLogger(__name__)


class ComponentConfig(BaseModel):
    kikyo_factory: Callable = None
    consumer_factory: Callable = None


class BaseWorker:
    name: str
    kikyo: Kikyo
    consumer: BaseConsumer

    def __init__(self, settings: dict):
        self.settings = Settings(settings)

        log.info('settings: %s', json.dumps(self.settings, ensure_ascii=False, indent=4))

        self._init_env()
        assert self.name is not None
        self.debug = self.settings.get('debug', False)
        self.workers = self.settings.get('workers', 1)

        self._sinks = defaultdict(list)
        self._sources = defaultdict(list)
        for name in dir(self):
            method = getattr(self, name)
            if inspect.ismethod(method):
                if hasattr(method, KIKYOPP_SOURCE):
                    self._sources[getattr(method, KIKYOPP_SOURCE)].append(method)
                if hasattr(method, KIKYOPP_SINK):
                    self._sinks[getattr(method, KIKYOPP_SINK)].append(method)

        self.is_running = False

        self.plugins = self._init_plugins()
        self._init_components(self._before_init_components())

    def _init_env(self):
        worker_name = os.environ.get('KIKYOPP_WORKER_NAME')
        if worker_name:
            self.name = worker_name

    def _init_plugins(self) -> dict:
        plugins = {
            entry_point.name: entry_point.load()
            for entry_point in pkg_resources.iter_entry_points('kikyopp.plugins')
        }
        return plugins

    def _before_init_components(self) -> ComponentConfig:
        config = ComponentConfig()

        config.consumer_factory = partial(KikyoConsumer, self)

        try:
            from kikyo_bundle import configure_by_consul

            config.kikyo_factory = partial(configure_by_consul, self.settings['kikyo_config_url'])
        except ImportError:
            pass

        for name, plugin in self.plugins.items():
            if hasattr(plugin, 'before_init_components'):
                plugin.before_init_components(self, config)

        return config

    def _init_components(self, config: ComponentConfig):
        self.kikyo = config.kikyo_factory()
        self.consumer = config.consumer_factory()

    def flow_to(self, data: Any, sink: str = None):
        if sink and sink not in self._sinks:
            log.error(f'No sink named "{sink}"')
            return
        for func in self._sinks[sink]:
            try:
                func(data)
            except Exception:
                log.error(f'Error occurred: sink={sink}, func={func.__name__}', exc_info=True)

    def start(self):
        if self.is_running:
            return

        if len(self._sources) == 0:
            log.warning('No defined source')

        self.is_running = True

        jobs = []
        for name in list(self._sources.keys()):
            t = threading.Thread(target=partial(self._subscribe, name), daemon=True)
            t.start()

            jobs.append(t)

        for job in jobs:
            job.join()

    def process(self, name, data: dict):
        for func in self._sources[name]:
            try:
                func(data)
            except Exception:
                log.error(f'Error occurred: source={name}, func={func.__name__}', exc_info=True)

    def _subscribe(self, name: str):
        jobs = []
        for i in range(self.workers):
            t = threading.Thread(target=partial(self.consumer.run, name), daemon=True)
            t.start()
            jobs.append(t)

        for job in jobs:
            job.join()

    def stop(self):
        if not self.is_running:
            return
        self.is_running = False
        self.consumer.stop()
