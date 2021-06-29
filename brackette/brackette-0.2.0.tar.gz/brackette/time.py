from datetime import timezone
import datetime


def generateUTCTimestamp():
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp


def tsToHuman(ts):
    s = datetime.datetime.utcfromtimestamp(ts)
    s.replace(tzinfo=timezone.utc)
    # somehow it ignores the %Z argument...
    return s.strftime('%Y-%m-%d %H:%M:%S UTC')
