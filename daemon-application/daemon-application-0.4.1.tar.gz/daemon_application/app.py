import os
import sys
import time
import signal

import click
import yaml

from .base import daemon_start
from .base import daemon_stop


class DaemonApplication(object):
    config_name = "config"
    config_suffix = "yml"
    default_appname = None

    stop_signal = None          # config item: stop-signal
    default_pidfile = None      # config item: pidfile
    default_workspace = None    # config item: workspace
    default_config = {
        "stop-signal": signal.SIGINT,
        "daemon": True,
        "workspace": os.getcwd(),
    }

    def get_default_config_filepaths(self, appname, name=None, suffix=None):
        name = name or self.config_name
        suffix = suffix or self.config_suffix
        filepaths = []
        filenames = (
            "./{0}-{1}.{2}".format(appname, name, suffix),
            "./conf/{0}-{1}.{2}".format(appname, name, suffix),
            "./etc/{0}-{1}.{2}".format(appname, name, suffix),
            "~/.{0}/{1}.{2}".format(appname, name, suffix),
            "~/{0}/{1}.{2}".format(appname, name, suffix),
            "./{0}.{1}".format(name, suffix),
            "./conf/{0}.{1}".format(name, suffix),
            "./etc/{0}.{1}".format(name, suffix),
            "~/{0}.{1}".format(name, suffix),
            "~/.{0}.{1}".format(name, suffix),
            "{0}.{1}".format(name, suffix),
        )
        for filename in filenames:
            filepath = os.path.abspath(os.path.expandvars(os.path.expanduser(filename)))
            if not filepath in filepaths:
                filepaths.append(filepath)
        return filepaths

    def main(self):
        raise NotImplementedError()

    def get_appname(self):
        appname = getattr(self, "default_appname", None)
        if appname is None:
            appname = os.path.splitext(os.path.basename(os.sys.argv[0]))[0]
        return appname
    
    def get_config_file_path(self, config_file_path, appname):
        the_config_file_path = None
        for config_file_path in [config_file_path] + self.get_default_config_filepaths(appname):
            if config_file_path and os.path.exists(config_file_path):
                the_config_file_path = config_file_path
                break
        return the_config_file_path

    def get_default_config(self):
        config = {}
        config.update(getattr(self, "default_config", {}))
        if not self.default_pidfile is None:
            config["pidfile"] = self.default_pidfile
        if not self.default_workspace is None:
            config["workspace"] = self.default_workspace
        if not self.stop_signal is None:
            config["stop-signal"] = self.stop_signal
        return config

    def load_config_from_config_file(self, config_file):
        if not config_file:
            return {}
        if not os.path.exists(config_file):
            return {}
        with open(config_file, "rb") as fobj:
            return yaml.safe_load(fobj)

    def update_config_item(self, config, item_name, item_value):
        if not item_value is None:
            config[item_name] = item_value
        return config

    def fix_config_items(self, config):
        if config.get("pidfile", None) is None:
            config["pidfile"] = self.appname + ".pid"

    def get_main_options(self):
        option_pidfile = click.option("--pidfile", help="pidfile file path.")
        option_daemon = click.option("--daemon/--no-daemon", is_flag=True, default=None, help="Run application in background or in foreground.")
        option_workspace = click.option("--workspace", help="Set running folder")
        option_config = click.option("-c", "--config", help="Config file path. Application will search config file if this option is missing. Use sub-command show-config-fileapaths to get the searching tactics.")
        return [option_config, option_daemon, option_workspace, option_pidfile]

    def get_controller(self):
        main_options = self.get_main_options()
        def _main(config, **kwargs):
            print("kwags:", kwargs)
            self.appname = self.get_appname()
            self.config_file_path = self.get_config_file_path(config, self.appname)
            if self.config_file_path:
                print("Start application with config file: {}".format(self.config_file_path), file=sys.stderr)
            else:
                print("Start application without config file.", file=sys.stderr)
            self.config = self.get_default_config()
            self.config.update(self.load_config_from_config_file(self.config_file_path))
            for key, value in kwargs.items():
                self.update_config_item(self.config, key.replace("_", "-"), value)
            self.fix_config_items(self.config)
        main = _main
        for option in main_options:
            main = option(main)
        main = click.group()(main)
    
        @main.command()
        def start():
            """Start daemon application.
            """
            pidfile = self.config["pidfile"]
            daemon = self.config["daemon"]
            workspace = self.config["workspace"]
            daemon_start(self.main, pidfile=pidfile, daemon=daemon, workspace=workspace)

        @main.command()
        def stop(sig):
            """Stop daemon application.
            """
            pidfile = self.config["pidfile"]
            stop_signal = self.config["stop-signal"]
            daemon_stop(pidfile, sig=stop_signal)

        @main.command()
        @click.option("--sleep-seconds", type=int, default=0, help="Wait some seconds after old application stopped and before new application started.")
        def restart(sleep_seconds):
            """Restart Daemon application.
            """
            pidfile = self.config["pidfile"]
            stop_signal = self.config["stop-signal"]
            daemon_stop(pidfile, sig=stop_signal)
            if sleep_seconds:
                time.sleep(sleep_seconds)
            daemon = self.config["daemon"]
            workspace = self.config["workspace"]
            daemon_start(self.main, pidfile=pidfile, daemon=daemon, workspace=workspace)

        @main.command(name="show-config-filepaths")
        def show_config_filepaths():
            """Print out the config searching paths.
            """
            config_filepaths = self.get_default_config_filepaths(self.appname)
            print("Application will search config file from following paths. It will load the first exists file as the config file.")
            for filepath in config_filepaths:
                print("    ", filepath)

        return main
