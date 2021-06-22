import json
from typing import Optional
import hmac
import hashlib
import criteo_marketing_transition as cm

from .exceptions import CriteoAccountLostAccessException



class CriteoClient:
    consent_url = "https://consent.criteo.com/request{query}&signature={signature}"

    def __init__(self, criteo_credentials_path: str, criteo_signing_path: Optional[str] = None) -> None:
        with open(criteo_credentials_path) as credentials:
            criteo_credentials = json.load(credentials)
        self._client_id = criteo_credentials.get('client_id')
        self._client_secret = criteo_credentials.get('client_secret')

        if criteo_signing_path is not None:
            with open(criteo_signing_path) as credentials:
                criteo_signing_credentials = json.load(credentials)
            self._signing_key_id = criteo_signing_credentials['signing_key_id']
            self._signing_key_secret = criteo_signing_credentials['signing_key_secret']

    def get_query(self, timestamp: float, state: str, redirect_uri: str):
        query = f"?key={self._signing_key_id}&timestamp={timestamp}&state={state}&redirect-uri={redirect_uri}"
        return query


    def get_consent_signature(self, timestamp: float, state: str, redirect_uri: str):
        query = self.get_query(timestamp, state, redirect_uri)
        m = hmac.new(self._signing_key_secret.encode(
            'utf-8'), digestmod=hashlib.sha512)
        m.update(query.encode('utf-8'))
        return m.hexdigest()


    def get_campaigns(self, advertiser_id: str):
        configuration = cm.Configuration(username=self._client_id,
                                      password=self._client_secret)
        request_ad_set_search = cm.RequestAdSetSearch(
            filters=cm.AdSetSearchFilter(advertiser_ids=[advertiser_id]))
        client = cm.ApiClient(configuration)
        campaign_api = cm.CampaignApi(client)
        resp = campaign_api.search_ad_sets(
            request_ad_set_search=request_ad_set_search)
        campaigns = resp.data
        return [
            {
                "id": campaign.id,
                "type": campaign.type,
                "name": campaign.attributes.name,
                "status": campaign.attributes.schedule.activation_status,
            } for campaign in campaigns]


    def check_access_account(self, adverstiser_id: str):
        "From client secret id and client secret, check if Arcane has access to it"
        configuration = cm.Configuration(username=self._client_id,
                                         password=self._client_secret)
        client = cm.ApiClient(configuration)
        api_instance = cm.AdvertiserApi(client)
        try:
            resp = api_instance.api_portfolio_get()
            next(advertiser for advertiser in resp.data if advertiser.id == adverstiser_id)
        except StopIteration:
            raise CriteoAccountLostAccessException(
                f'We do not have access to advertiser {adverstiser_id}')
