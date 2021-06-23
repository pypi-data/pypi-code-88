from feeds.utils import update_feeds

from aleksis.core.celery import app


@app.task
def get_feeds():
    """Update RSS feeds through django-feeds."""
    return update_feeds(max_feeds=10)
