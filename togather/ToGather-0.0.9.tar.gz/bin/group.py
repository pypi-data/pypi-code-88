class Group:
    "the group class contains a list of users, a list of events and a calendar"
    def __init__(self, name, calendar="", users=[], events=[]):
        self._name = name
        self._calendar = calendar
        self._users = users
        self._events = events

    @property
    def calendar(self):
        return self._calendar

    @calendar.setter
    def calendar(self, calendar):
        self._calendar = calendar

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users):
        self._users = users

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, events):
        self._events = events

