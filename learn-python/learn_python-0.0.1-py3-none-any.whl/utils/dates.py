from datetime import datetime, timedelta


def days_ago(n, hour=0, minute=0, second=0, microsecond=0):
    """
    Get the datetime n days ago. By default time is set to midnight
    """
    today = datetime.utcnow()\
        .replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    return today - timedelta(days=n)
