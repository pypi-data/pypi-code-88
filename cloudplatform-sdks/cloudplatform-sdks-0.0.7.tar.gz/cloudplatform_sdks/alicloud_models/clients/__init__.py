import importlib
from .cdn_client import CdnClient
from proxy_tools import proxy

prod_mapper = {
    'cdn': CdnClient
}


def get_current_client(prod):
    module = importlib.import_module('cloudplatform_auth')
    get_access_func = getattr(module, 'get_alicloud_access_info')
    access_key_id, access_key_secret, region = get_access_func()
    return prod_mapper[prod](access_key_id, access_key_secret, region)


@proxy
def cdn_client():
    return get_current_client('cdn')
