from flask_scenario_testing.support.Time import Time


class ScenarioConfig(object):
    def __init__(self, name, users_count: int, run_time: str, modifiers, options):
        self._users_count = users_count
        self._run_time = run_time
        self._modifiers = modifiers
        self._name = name
        self._options = options

    def users_count(self):
        return self._users_count

    def run_time(self) -> Time:
        return Time.from_string(self._run_time)

    def modifiers(self):
        return self._modifiers

    def name(self):
        return self._name

    def options(self):
        return self._options
