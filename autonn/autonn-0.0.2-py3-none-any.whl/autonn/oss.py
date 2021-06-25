import os
import re
from typing import Dict, Tuple

import oss2

from .env import ENABLE_OSS_INTERNEL_ACCESS

access_key_id = os.environ["AIE_OSS_ACCESS_KEY_ID"]
access_key_secret = os.environ["AIE_OSS_ACCESS_KEY_SECRET"]
auth = oss2.Auth(access_key_id, access_key_secret)


def convert_ali_oss_endpoint_to_internal(endpoint: str) -> str:
    host, *rest = endpoint.split(".")
    return f"{host}-internal." + ".".join(rest)


def _parse_oss_url(url: str) -> Tuple[str, str, str]:
    """Get the bucket, endpoint, and object key from an OSS url,
    which is composed as follows,

    oss://{bucket}.{endpoint}/{key of the object}, e.g.,
    oss://aiexcelsior-shanghai-test.oss-cn-shanghai.aliyuncs.com/some_img.jpg

    Parameters
    ----------
    url : str
        an OSS url
    Returns
    -------
    Tuple[str, str, str]
        (bucket, endpoint, key)
    """
    url = url.lstrip("oss://")
    return re.search(r"^([^.]*)\.([^/]*)/(.*)$", url).groups()


class OSSConfig:
    """Manage OSS config"""

    def __init__(self):
        self.auth: oss2.Auth = auth
        self._buckets: Dict = {True: {}, False: {}}  # `True` for internal

    def __call__(self, url: str, internal: bool = ENABLE_OSS_INTERNEL_ACCESS):
        bucket_name, endpoint, obj_key = _parse_oss_url(url)
        if bucket_name not in self._buckets[internal]:
            if internal:
                endpoint = convert_ali_oss_endpoint_to_internal(endpoint)

            bucket = oss2.Bucket(self.auth, endpoint, bucket_name)
            self._buckets[internal][bucket_name] = bucket
        else:
            bucket = self._buckets[internal][bucket_name]
        return bucket, obj_key
