"""Implements twitter."""

import argparse
import logging
import tweepy

from utils import timex

MAX_LEN_TWEET = 280
MAX_MEDIA_FILES = 4

log = logging.getLogger('twitter-wrapper')
logging.basicConfig(level=logging.INFO)


class Twitter:
    """Implements Twitter wrapper."""

    def __init__(
        self,
        twtr_api_key,
        twtr_api_secret_key,
        twtr_access_token,
        twtr_access_token_secret,
    ):
        """Construct Twitter."""
        if twtr_api_key:
            auth = tweepy.OAuthHandler(twtr_api_key, twtr_api_secret_key)
            auth.set_access_token(twtr_access_token, twtr_access_token_secret)
            self.api = tweepy.API(auth)
            api_me = self.api.me()
            log.info(
                'Created Twitter for @%s (%s).',
                api_me.screen_name,
                api_me.id_str
            )
        else:
            log.error(
                'Missing twitter API Key etc. Cannot create Twitter.',
            )
            self.api = None

    @staticmethod
    def from_args(description=''):
        """Construct Twitter from Args."""
        parser = argparse.ArgumentParser(
            description=description,
        )
        for twtr_arg_name in [
            'twtr_api_key',
            'twtr_api_secret_key',
            'twtr_access_token',
            'twtr_access_token_secret',
        ]:
            parser.add_argument(
                '--' + twtr_arg_name,
                type=str,
                required=False,
                default=None,
            )
        args = parser.parse_args()
        return Twitter(
            args.twtr_api_key,
            args.twtr_api_secret_key,
            args.twtr_access_token,
            args.twtr_access_token_secret,
        )

    def tweet(
        self,
        tweet_text,
        status_image_files=None,
        update_user_profile=False,
        profile_image_file=None,
        banner_image_file=None,
    ):
        """Tweet."""
        if status_image_files is None:
            status_image_files = []

        if not self.api:
            log.error('Missing API. Cannot tweet')
            return False

        if len(tweet_text) > MAX_LEN_TWEET:
            log.error('Tweet text is too long. Not tweeting.')
            return

        if len(status_image_files) > MAX_MEDIA_FILES:
            log.warning('Too many (%d) status image files. Truncating.')
            status_image_files = status_image_files[:MAX_MEDIA_FILES]

        media_ids = []
        for image_file in status_image_files:
            res = self.api.media_upload(image_file)
            media_id = res.media_id
            media_ids.append(media_id)
            log.info(
                'Uploaded status image %s to twitter as %s',
                image_file,
                media_id,
            )

        if media_ids:
            self.api.update_status(tweet_text, media_ids=media_ids)
        else:
            self.api.update_status(tweet_text)
        log.info('Updated status to: %s', tweet_text)

        if update_user_profile:
            date = timex.format_time(
                timex.get_unixtime(),
                '%B %d, %Y %H:%M%p',
            )
            timezone = timex.get_timezone()
            description = 'Automatically updated at {date} {timezone}'\
                .format(date=date, timezone=timezone)
            self.api.update_profile(description=description)
            log.info('Updated profile description to: %s', description)

        if profile_image_file:
            self.api.update_profile_image(profile_image_file)
            log.info(
                'Update profile image to %s',
                profile_image_file,
            )

        if banner_image_file:
            self.api.update_profile_banner(banner_image_file)
            log.info(
                'Update profile banner image to %s',
                banner_image_file,
            )
        return True


if __name__ == '__main__':
    twtr = Twitter.from_args()
    twtr.tweet('Test')
