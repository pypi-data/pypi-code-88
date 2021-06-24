import json
from typing import List, Optional, Union
import hmac
import hashlib
import criteo_marketing_transition as cm
from datetime import date, datetime, timedelta

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
        return self.get_hashed_value(query.encode('utf-8'))

    def get_hashed_value(self, content_to_hash: bytes):
        m = hmac.new(
            self._signing_key_secret.encode('utf-8'),
            digestmod=hashlib.sha512
        )
        m.update(content_to_hash)
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

    def get_advertisers(self):
        configuration = cm.Configuration(username=self._client_id,
                                         password=self._client_secret)
        client = cm.ApiClient(configuration)
        api_instance = cm.AdvertiserApi(client)
        resp = api_instance.api_portfolio_get()
        return [{"id": advertiser.id, "name": advertiser.attributes.advertiser_name}
                for advertiser in resp.data]

    def check_access_account(self, adverstiser_id: str):
        "From client secret id and client secret, check if Arcane has access to it"
        advertisers = self.get_advertisers()
        try:
            next(
                advertiser for advertiser in advertisers if advertiser['id'] == adverstiser_id)
        except StopIteration:
            raise CriteoAccountLostAccessException(
                f'We do not have access to advertiser {adverstiser_id}')

    def get_report(self,
                   account_id: str, *,
                   start_date: Union[datetime, date],
                   dimensions: Optional[List] = None,
                   metrics: Optional[List] = None,
                   end_date: Optional[Union[datetime, date]] = None
                   ) -> str:
        """Download a statistics report from Criteo API
        See more info on the official documentation https://developers.criteo.com/marketing-solutions/docs/analytics

        Args:
            account_id (str): The id of the account targeted
            start_date (Union[datetime, date]): the first date of the report
            dimensions (Optional[List], optional): Dimensions allow you to specify the aggregation level suited to your needs. Defaults to None.
            metrics (Optional[List], optional): Metrics refer to measurements such as clicks, revenue, or cost per visit. Defaults to None.
            end_date (Optional[Union[datetime, date]], optional): the last date of the report. Defaults to None.

        Returns:
            [str]: a CSV string containing all the requested data
        """
        if dimensions is None:
            dimensions = ["AdvertiserId", "Advertiser", "AdsetId", "Adset", "Day"]
        if metrics is None:
            metrics = [
                "Clicks", "Displays", "AdvertiserCost", "SalesPc30d",
                "ConversionRatePc30d", "ClickThroughRate", "ECosPc30d", "Cpc",
                "RoasPc30d"
            ]
        if end_date is None:
            end_date = datetime.today().date() - timedelta(days=1)

        configuration = cm.Configuration(username=self._client_id,
                                         password=self._client_secret)
        client = cm.ApiClient(configuration)
        analytics_api = cm.AnalyticsApi(client)
        stats_query_message = cm.StatisticsReportQueryMessage(
            advertiser_ids=account_id,
            dimensions=dimensions,
            metrics=metrics,
            start_date=start_date.strftime('%Y-%m-%d'),
            end_date=end_date.strftime('%Y-%m-%d'),
            currency="EUR",
            format="Csv")

        [response_content, _, _] = analytics_api.get_adset_report_with_http_info(
            statistics_report_query_message=stats_query_message)
        return response_content
