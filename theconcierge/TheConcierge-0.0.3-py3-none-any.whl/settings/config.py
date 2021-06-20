from sys import argv
from os import path, getcwd
from json import loads


class Config:
    _settings_dir = "settings/"
    _settings_file = "settings.json"
    _handlers_dir = "handlers/"

    def _get_base_path():
        current_path = path.abspath(argv[0])
        basename_file = path.basename(argv[0])
        base_path = current_path.replace(basename_file, "")
        return base_path
    
    def _get_working_path(relative=True):
        if relative:
            return Config._get_base_path().replace(getcwd(), "")[1 : ]
        else:
            return getcwd()

    def _get_system_path():
        settings_path = Config._get_base_path() + Config._settings_dir
        return settings_path

    def _get_handlers_path():
        handlers_path = Config._get_working_path() + Config._handlers_dir
        return handlers_path

    def _read_file():
        settings_file = Config._get_system_path() + Config._settings_file
        with open(settings_file, "r") as settings:
            json_settings = loads(settings.read())
        return json_settings

    @staticmethod
    def get_value(value):
        json_settings = Config._read_file()
        return json_settings.get(value, None)

    @staticmethod
    def get_system(value):
        json_systems = Config.get_value("system")
        return json_systems.get(value, None)

    @staticmethod
    def get_app(value):
        json_apps = Config.get_value("app")
        return json_apps.get(value, None)

    @staticmethod
    def get_handlers(value=None):
        json_handlers = Config.get_value("handlers")
        if not value:
            return {Config._get_handlers_path() + key: values for key, values in json_handlers.items()}
        else:
            return {Config._get_handlers_path() + value: [values for values in json_handlers.get(value, [])]}
