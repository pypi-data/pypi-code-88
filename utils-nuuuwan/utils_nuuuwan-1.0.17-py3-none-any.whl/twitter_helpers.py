"""Implements twitter helpers."""

import logging

from utils import timex

log = logging.getLogger('twitter-wrapper-helpers')
logging.basicConfig(level=logging.INFO)


def _update_status(api, tweet_text, media_ids):
    if len(media_ids) > 0:
        api.update_status(tweet_text, media_ids=media_ids)
    else:
        api.update_status(tweet_text)


def _upload_media(api, image_files):
    media_ids = []
    for image_file in image_files:
        media_id = api.media_upload(image_file).media_id
        media_ids.append(media_id)
        log.info(
            'Uploaded status image %s to twitter as %s',
            image_file,
            media_id,
        )
    return media_ids


def _update_profile_description(api):
    date_with_timezone = timex.format_current_date_with_timezone()
    description = 'Automatically updated at {date_with_timezone}'\
        .format(date_with_timezone=date_with_timezone)
    api.update_profile(description=description)
    log.info('Updated profile description to: %s', description)
