"""JengaHQ helpers."""
from datetime import datetime, timedelta


def todaystr():
    """Return today date as string %Y-%m-%d."""
    return datetime.today().date().strftime("%Y-%m-%d")


def token_expired(last_auth):
    """Return true if last_auth is less than 3s from now."""
    if datetime.now() - last_auth > timedelta(seconds=3000):
        return True
    else:
        return False


def timenow():
    """Return now date."""
    return datetime.now()


# print(todaystr())
