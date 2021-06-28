from datetime import timedelta, datetime, timezone


def format_timedelta(delta: timedelta) -> str:
    milliseconds = int(delta.total_seconds() * 1000)
    return str(milliseconds) + "ms"


def conv_to_rcf3339(dt: datetime):
    return dt.astimezone(timezone.utc).isoformat()
