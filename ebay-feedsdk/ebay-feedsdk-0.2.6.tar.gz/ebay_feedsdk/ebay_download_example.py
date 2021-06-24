import logging

from ebay_feedsdk.errors.custom_exceptions import DownloadError
from ebay_feedsdk.feed import Feed
from ebay_feedsdk.filter.feed_filter import GetFeedResponse
from ebay_feedsdk.oauthclient.credentialutil import Credentialutil
from ebay_feedsdk.oauthclient.model.model import Environment, OauthToken, EnvType
from ebay_feedsdk.oauthclient.oauth2api import Oauth2api

class EbayDownloadExample:
    app_scopes = ["https://api.ebay.com/oauth/api_scope", "https://api.ebay.com/oauth/api_scope/buy.item.feed"]
    config_file = 'ebay-config.yaml'

    def __init__(self, market_place: str, env: EnvType, feed_scope, download_location: str):
        self.env = env
        self.feed_scope = feed_scope
        self.market_place = market_place
        self.download_location = download_location

    def download(self, category_id: str) -> GetFeedResponse:
        logging.info(
            f'Downloading category {category_id} for {self.market_place} with scope {self.feed_scope}'
            f'to {self.download_location}')

        token = self.get_token()

        feed_obj = Feed(feed_type='item', feed_scope=self.feed_scope, category_id=category_id,
                        marketplace_id=self.market_place,
                        token=token.access_token, environment=self.env.name, download_location=self.download_location)

        feed_response: GetFeedResponse = feed_obj.get()

        if feed_response.status_code != 0:
            raise DownloadError(f'Download failed see: {feed_response.message}')

        logging.info(f'File was downloaded under {feed_response.file_path}')

        return feed_response

    def get_token(self) -> OauthToken:
        Credentialutil.load(self.config_file)
        oauth2api = Oauth2api()

        token = oauth2api.get_application_token(self.env, self.app_scopes)
        if not token.access_token:
            raise DownloadError(f'Got no token, check: {token.error}')

        return token


if __name__ == "__main__":
    market_place = 'EBAY_DE'
    feed_scope = 'ALL_ACTIVE'
    download_location = '/tmp/feed'
    category_id = '2984'  # string ..
    ebay_download = EbayDownloadExample(market_place, Environment.PRODUCTION, feed_scope, download_location)
    feed_response = ebay_download.download(category_id)
    print(feed_response)

