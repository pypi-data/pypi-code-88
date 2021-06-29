# Changed filename so that default time class can be used in server.
class Time:
    """A simple time class that may be replaced"""

    def __init__(self, date="mm/dd/yy", hour=""):

        self._date = date
        self._hour = hour

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        self._hour = hour
