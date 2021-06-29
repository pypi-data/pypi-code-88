from .client import HuaweiClient
from huaweicloudsdkeip.v2 import EipClient
from huaweicloudsdkeip.v2.region.eip_region import EipRegion


class HuaweiEipClient(HuaweiClient):
    def __init__(self, *args, **kwargs):
        super(HuaweiEipClient, self).__init__(*args, **kwargs)

    @property
    def eip_client(self):
        return self.generate_client(EipClient, EipRegion)
