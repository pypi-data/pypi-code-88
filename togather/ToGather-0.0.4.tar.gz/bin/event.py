class Event:
    """A class that contains a list of options, a description and is either"""
    "complete or incomplete, completes are in the calendar, both are in the group"

    def __init__(self, name, description, options, status=False):
        self._name = name
        self._description = description
        self._options = options
        self._status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        self._options = options

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

