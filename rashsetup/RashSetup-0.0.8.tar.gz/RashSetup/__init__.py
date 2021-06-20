import os
import json
import threading
import sys
import time
import gc
import pathlib
import shutil
import subprocess
import urllib.request

import scrapy.crawler
from .RashScrappers.RashScrappers.spiders import *

__all__ = [
    "JsonHandler",
    "TempHandler",
    "Launcher"
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
    def __init__(self, pwd):
        self.pwd = pathlib.Path(pwd)
        self.pwd = self.pwd.parent if self.pwd.is_file() else self.pwd

        if not self.pwd.exists():
            raise FileNotFoundError(self.pwd)

        self.global_mutex = self.pwd / "GLOBAL.lock"
        self.max_mutex = self.pwd / "MAX.lock"

        None if self.test() else self._notify()

        read_thread = threading.Thread(target=self.read_thread)
        read_thread.setName("Global Mutex Thread")
        read_thread.setDaemon(True)
        write_thread = threading.Thread(target=self.write_thread)
        write_thread.setName("Max Mutex Thread")
        write_thread.setDaemon(True)

        self.workers = threading.Lock(), threading.Lock()
        self.remainder = None

        read_thread.start()
        write_thread.start()

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


def export_rash(current_path):
    if not os.path.isdir(current_path):
        raise NotADirectoryError(f"{current_path} is not a directory")


def pip_install(*packages):
    for _ in packages:
        subprocess.run([
            sys.executable, "-m", "pip", "install", _
        ])


def is_rash():
    return sys.executable.endswith("Rash.exe")


def check_settings(path):
    return "settings.json" in os.listdir(path)


gc.collect()


class PluginManager:
    def __init__(self, logger=None):
        self.file = JsonHandler(os.path.join(
            os.path.dirname(__file__), "settings.json"
        ))

        self.modules = os.path.join(
            os.path.dirname(__file__), "Modules"
        )

        self.logger = logger

        self.general = os.path.join(
            self.modules, "General"
        )

        self.user = os.path.join(
            self.modules, "User"
        )

        self.employ()

    def is_useful(self):
        return os.path.exists(str(self.file)) and all(
            os.path.exists(__)
            for _ in self.file.load()["general"]["modules"]
            for __ in os.path.join(self.user, _)
        )

    def employ(self):
        reactor = self.scrape_settings() if not os.path.exists(
            str(self.file)) else None if self.is_useful() else self.setup(refresh=True)
        reactor.start() if reactor else None

    def scrape_settings(self):
        process = scrapy.crawler.CrawlerProcess()

        settings = process.crawl(
            SettingsSpider,
            url=URL,
            pipe=self.update_settings
        )

        settings.addCallback(
            lambda _: self.setup(process, True)
        )

        process.start()

    def setup(
            self,
            process=None,
            refresh=False
    ):

        shutil.rmtree(self.modules) if refresh and os.path.exists(self.modules) else None

        process = process if process else scrapy.crawler.CrawlerProcess()
        self.ensure_paths()

        general = self.file.load()['general']['modules']

        for _ in general:
            module = os.path.join(
                self.user, _
            )

            if os.path.exists(module):
                continue

            process.crawl(
                RepoSpider,
                url=general[_],
                pipe=lambda name, from_, to: self.download_module(name, from_, to),
                save=os.path.join(self.general, _)
            )

        return process

    def update_settings(self, url):
        with urllib.request.urlopen(url) as o_json:
            parsed = self.file(
                o_json.read()
            )

        user = self.file.load()["user"] if self.is_useful() else False

        if parsed is None:
            raise TypeError(f"Not able to parse {url}")

        parsed["user"].update(user) if user else None

        self.file.dump(parsed)

    def ensure_paths(self):
        None if os.path.exists(self.modules) else os.mkdir(self.modules)
        None if os.path.exists(self.general) else os.mkdir(self.general)
        None if os.path.exists(self.user) else os.mkdir(self.user)

    def download_module(self, name, from_, to):
        self.register_module(name, to) if os.path.exists(to) else None
        shutil.move(from_, to)

    def register_module(self, name, path):
        if not os.path.exists(path):
            raise FileNotFoundError

        parsed = self.file.load()

        print("uninstalling", name)
        self.unregister_module(parsed, name) if name in parsed["user"]["pth"] else None
        print("installing", name)

        parsed["user"]["pth"][name] = tuple(
            os.walk(path)
        )

        self.file.dump(parsed)

    def unregister_module(self, parsed, name):
        tree = parsed["user"]["pth"][name]
        dir_s = []

        for _ in tree:
            for __ in _[-1]:
                os.remove(
                    os.path.join(_[0], __)
                )

            dir_s.append(_[0])

        for _ in reversed(dir_s):
            os.rmdir(_)  # only empty ones will be deleted

        parsed["user"]["pth"].pop(name)

    def uninstall_module(self, name):
        parsed = self.file.load()

        if name in parsed["general"]["modules"]:
            return False

        self.unregister_module(
            parsed, name
        )

        parsed["user"]["modules"].pop(name)

        self.file.dump(parsed)

        return True


def ParentProcess():
    temp = PluginManager()
