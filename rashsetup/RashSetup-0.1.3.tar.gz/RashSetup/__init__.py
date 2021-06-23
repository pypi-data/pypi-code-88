import multiprocessing
import os
import json
import threading
import sys
import time
import gc
import pathlib
import subprocess
import urllib.request
import concurrent.futures
import importlib
import scrapy.crawler

from .RashScrappers.RashScrappers.spiders import *

__all__ = [
    "JsonHandler",
    "TempHandler",
    "Launcher",
    "Processes"
]

URL = "https://github.com/RahulARanger/RashSetup"


class JsonHandler:
    def __init__(self, file=None):
        self.file = file

    def load(self):
        with open(self.file, 'r') as loaded:
            return json.load(loaded)

    def dump(self, store):
        with open(self.file, 'w') as loaded:
            return json.dump(store, loaded, indent=4)

    def __call__(self, raw: str):
        return json.loads(raw)

    def __str__(self):
        return self.file


"""
LOCK SAUCE:
    GLOBAL LOCK:
    'e' - exited
    '1' - high state
    '' - low state

    MAX LOCK:
        '1' - someone tried to open
        'e' - close application [TODO]

    Rash is opened if it toggle s between high and low state for every second

"""


class Launcher:
    def __init__(self, pwd, manager: concurrent.futures.ThreadPoolExecutor):
        self.pwd = pathlib.Path(pwd)
        self.pwd = self.pwd.parent if self.pwd.is_file() else self.pwd

        if not self.pwd.exists():
            raise FileNotFoundError(self.pwd)

        self.global_mutex = self.pwd / "GLOBAL.lock"
        self.max_mutex = self.pwd / "MAX.lock"

        None if self.test() else self._notify()

        self.workers = threading.Lock(), threading.Lock()

        manager.submit(
            self.read_thread
        )

        manager.submit(
            self.write_thread
        )

        self.remainder = None

    def _notify(self):
        self.max_mutex.write_text("1")
        return sys.exit(0)

    def register(self):
        pass

    def test(self):
        if not self.global_mutex.exists():
            self.global_mutex.write_text("")
            return True

        test_1 = self.global_mutex.read_text()

        if test_1 == 'e':
            return True

        time.sleep(1)

        test_2 = self.global_mutex.read_text()

        time.sleep(0.1)

        test_3 = self.global_mutex.read_text()

        if test_1 == test_2 and test_3 == test_1:
            return True

        return False

    def read_thread(self):
        self.workers[0].acquire()

        while self.workers[0].locked():

            code = None if self.max_mutex.exists() else self.max_mutex.write_text("")
            code = code if code else self.max_mutex.read_text()

            result = None if code == '' else self.remainder(code == '1') if self.remainder else None

            if result:
                break

            time.sleep(1)

        self.max_mutex.write_text("")

    def write_thread(self):
        self.workers[1].acquire()

        toggle = False

        while self.workers[1].locked():
            None if self.global_mutex.exists() else self.global_mutex.write_text("")

            self.global_mutex.write_text("" if toggle else "1")
            toggle = not toggle

            time.sleep(1)

    def close(self):
        for _ in self.workers:
            _.release()


class PluginManager:
    def __init__(self, logger=None):
        self.file = JsonHandler(os.path.join(
            os.path.dirname(__file__), "settings.json"
        ))

        self.logger = logger
        self.employ()

    def is_useful(self, cache=None):
        cache = cache if cache else self.file.load()
        return all(
            importlib.util.find_spec(_) for _ in cache["general"]["modules"]
        )

    def employ(self):
        reactor = None if os.path.exists(str(self.file)) else self.scrape_settings()
        reactor = self.setup(reactor) if reactor or not self.is_useful() else None
        reactor.start() if reactor else None

    def scrape_settings(self):
        process = scrapy.crawler.CrawlerProcess()

        settings = process.crawl(
            SettingsSpider,
            url=URL,
            path=None,
            pipe=self.update_settings
        )

        settings.addCallback(
            lambda _: self.setup(process)
        )

        return process

    def update_settings(self, path, url):
        temp = JsonHandler(os.path.join(
            path, "settings.json")
        ) if path else self.file

        with urllib.request.urlopen(url) as o_json:
            parsed = temp(
                o_json.read()
            )

        if parsed is None:
            raise TypeError(f"Not able to parse {url}")

        parsed["user"].update(temp.load()["user"]) if os.path.exists(temp.file) else None

        self.file.dump(parsed)

    def setup(
            self,
            process=None
    ):
        process = process if process else scrapy.crawler.CrawlerProcess()

        general = self.file.load()['general']['modules']

        for _ in general:
            if importlib.util.find_spec(_):
                continue

            self.install_module(
                process, _, general[_]
            )

        return process

    def install_module(self, process, name, url):
        process.crawl(
            RepoSpider,
            url=url,
            pipe=lambda saved: self.install_settings(saved),
            name=name
        )

    def install_settings(self, saved):
        # assumes that ur module has settings.json inside it
        settings = os.path.join(saved, "settings.json")
        setup = os.path.join(saved, "setup.py")

        if not os.path.exists(settings):
            raise FileNotFoundError(f"Settings File not found for {settings}")

        Processes.setup_tools(setup)
        Processes.pip_install(saved)

    def uninstall_module(self, name):
        importlib.util.find_spec(name)  # TODO: a simple pip uninstall may not delete everything
        # TODO: this affects when reinstalling the package

        subprocess.run([
            sys.executable,
            "-m",
            "pip",
            "uninstall",
            name,
            "-y"
        ])


class Processes:
    @staticmethod
    def pip_install(package, *args):
        subprocess.run([
            sys.executable, "-m", 'pip', 'install', package, *args
        ])

    @staticmethod
    def setup_tools(setup_file):
        subprocess.run([
            sys.executable, setup_file, "sdist bdist"
        ])

    @staticmethod
    def pip_uninstall(package):
        subprocess.run([
            sys.executable, "-m", "pip", "uninstall", package, "-y"
        ])

    @staticmethod
    def rash_process():
        try:
            temp = PluginManager()

        except Exception as error:
            print("Failed to Setup Rash! because of", error)

            while True:
                pass

    @staticmethod
    def search(
            url,
            queue: multiprocessing.Queue
    ):
        raw_link = None

        def results(path, raw):
            queue.put(
                raw
            )

        process = scrapy.crawler.CrawlerProcess()
        process.crawl(SettingsSpider, url=url, pipe=results, path=None)
        process.start()

        return raw_link


gc.collect()
