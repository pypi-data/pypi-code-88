from _time import Time


class Options:
    """
    A class that is the choices that a voted on, contains an activity, time object, a boolean of chosen, and a list of
    votes that are a pair of users and the vote choice: 1,2,3,4 . . .
    """

    def __init__(self, activity, tim=Time(), chosen=False, votes=[]):
        self._activity = activity
        self._time = tim
        self._chosen = chosen
        self._votes = votes

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, activity):
        self._activity = activity

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, tim):
        self._time = tim

    @property
    def chosen(self):
        return self._chosen

    @chosen.setter
    def chosen(self, chosen):
        self._chosen = chosen

    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, votes):
        self._votes = votes
