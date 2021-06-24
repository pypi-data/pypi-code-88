class InteralServerError(Exception):
    def __init__(self):
        Exception.__init__(self,"Unexpected internal server error.")
        
        
class DatabaseError(Exception):
    def __init__(self):
        Exception.__init__(self,"Unable to connect to the database.")
        

class SummonerNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self,"Summoner is not on record.")


class NoRecentMMRError(Exception):
    def __init__(self):
        Exception.__init__(self,"No recent MMR data for summoner.")


class MissingQueryError(Exception):
    def __init__(self):
        Exception.__init__(self,"Missing 'name' query parameter.")


class RateLimitError(Exception):
    def __init__(self):
        Exception.__init__(self,"Too many requests.")

class InvalidRegionError(Exception):
    def __init__(self):
        Exception.__init__(self,"The Requested Region is not supported.")