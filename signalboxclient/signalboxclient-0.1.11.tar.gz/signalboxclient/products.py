from .client_functions import get, post
from .pagination import pageQuery, PaginatedResponse
from .exceptions import SignalBoxException


def create_product(access_token: str, base_url: str, name: str, product_id: str, description: str):
    json_params = {
        "name": name,
        "productId": product_id,
        "description": description,
    }
    r = post(f'{base_url}/api/products',
             json_params, access_token)
    if r.ok:
        return r.json()
    else:
        raise SignalBoxException(r.text)

def query_products(access_token: str, base_url: str, page: int = None):
    r = get(f'{base_url}/api/products?{pageQuery(page)}', access_token)
    if r.ok:
        return PaginatedResponse(**r.json())
    else:
        raise SignalBoxException(r.text)