import importlib
from proxy_tools import proxy
from .clb_client import ClbClient
from .cdn_client import CdnClient
from .cfs_client import CfsClient

prod_mapper = {
    'clb': ClbClient,
    'cdn': CdnClient,
    'cfs': CfsClient
}


def get_current_client(prod):
    module = importlib.import_module('cloudplatform_auth')
    get_access_func = getattr(module, 'get_tencentcloud_access_info')
    access_key_id, access_key_secret, region = get_access_func()
    return prod_mapper[prod](access_key_id, access_key_secret, region)


@proxy
def clb_client():
    return get_current_client('clb')


@proxy
def cdn_client():
    return get_current_client('cdn')


@proxy
def cfs_client():
    return get_current_client('cfs')
