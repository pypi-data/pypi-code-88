from .client import TencentClient
from tencentcloud.cdn.v20180606 import cdn_client as tencent_cdn_client
from tencentcloud.cdn.v20180606 import models


class CdnClient(TencentClient):
    def __init__(self, *args, **kwargs):
        super(CdnClient, self).__init__(*args, **kwargs)
        self.httpProfile.endpoint = "cdn.tencentcloudapi.com"
        self.clientProfile.httpProfile = self.httpProfile
        self.client = tencent_cdn_client.CdnClient(self.cred, self.region, self.clientProfile)

    def refresh_urls_cache(self, **kwargs):
        req = models.PurgeUrlsCacheRequest()
        self.do_sync_request(self.client.PurgeUrlsCache, req, **kwargs)

    def refresh_path_cache(self, **kwargs):
        req = models.PurgePathCacheRequest()
        self.do_sync_request(self.client.PurgePathCache, req, **kwargs)

    def push_urls_cache(self, **kwargs):
        req = models.PushUrlsCacheRequest()
        self.do_sync_request(self.client.PushUrlsCache, req, **kwargs)

    def list_domains(self, **kwargs):
        req = models.ListScdnDomainsRequest()
        return self.do_request(self.client.ListScdnDomains, req, **kwargs)

