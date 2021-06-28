import time
import requests
from .. import config
from . import log
from . import uri
from . import utils

STATUS_OK = "Ok"
STATUS_UNKNOWN = "Unknown"

def safe_GET(url, sleep_time=config.sleep_time, as_json=True, max_tries=5):
    """ requests handler. (status, data) where:
        status can be "Ok" or Exception message
        data """
    while max_tries > 0:    
        max_tries -= 1
        try:
            response = requests.get(url)
            # if status code was ok (200)
            if response.status_code == 200:
                if as_json:
                    return (STATUS_OK, response.json())
                return (STATUS_OK, response)
            else:
                raise Exception( "[D] >>> error 287596: {}".format(response) )
        except Exception as e:
            result = ( e, None )
            print('[D] >>> exception occured at 38754. Tries left = {} \n\t Exception: {}'.format(max_tries, e))
        # if call was unsuccessful, sleep for a litle before trying again
        if max_tries > 0:
            time.sleep(sleep_time)
    return (None, None)

def get_market_data(min_mcap, sleep_time=config.sleep_time, only_solana_ecosystem=False):
    """ gets market information for all tokens with more than 
        specified market cap. Sorted by market cap 
        param: sleep_time is sleep time between calls
        
        returns: tokens list with market data in the following format:
        (status, data). If the status is not "Ok", data may be corrupted or empty.

        example link: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1&page=1&sparkline=false&price_change_percentage=24h
        
        example return:
        [
            {
                "id": "bitcoin",
                "symbol": "btc",
                "name": "Bitcoin",
                "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579",
                "current_price": 32823,
                "market_cap": 615470220154,
                "market_cap_rank": 1,
                "fully_diluted_valuation": 689559037163,
                "total_volume": 30706913939,
                "high_24h": 33599,
                "low_24h": 31071,
                "price_change_24h": 1751.74,
                "price_change_percentage_24h": 5.63777,
                "market_cap_change_24h": 33644018114,
                "market_cap_change_percentage_24h": 5.78249,
                "circulating_supply": 18743681,
                "total_supply": 21000000,
                "max_supply": 21000000,
                "ath": 64805,
                "ath_change_percentage": -49.33063,
                "ath_date": "2021-04-14T11:54:46.763Z",
                "atl": 67.81,
                "atl_change_percentage": 48324.46375,
                "atl_date": "2013-07-06T00:00:00.000Z",
                "roi": null,
                "last_updated": "2021-06-27T21:20:28.855Z",
                "price_change_percentage_24h_in_currency": 5.637773796603842
            }
        ]
    """
    tokens = []
    success = False
    request_page = 1
    # make api calls until we get all required data
    while not success:
        # request data
        if only_solana_ecosystem:
            url = uri.URI_SOLANA_ECOSYSTEM_MARKET_DATA.format(request_page)
        else:
            url = uri.URI_MARKET_DATA.format(request_page)

        status, data = safe_GET(url, sleep_time)

        # if we got status ok but no more data was returned
        if status == STATUS_OK and len(data) == 0:
            print("[D] >>> 7436: returning {} tokens".format(len(tokens)))
            return (STATUS_OK, tokens)

        # if could not obtain correct data, return
        if status is not STATUS_OK:
            print("[D] >>> 45638543: error occured when getting market data at page {}. Data may be corrupted. Returning tokens anyway \n\tData received {}".format(request_page, data))
            return (STATUS_UNKNOWN, tokens)
        # append the data to tokens
        try:
            tokens.extend(data)
        except Exception as e:
            print("[D] >>> 4758343: {} \n\t returning tokens but data may be corrupted".format(e))
            return (STATUS_UNKNOWN, tokens)

        # see if this call already has smaller market caps than specified
        try:
            # if market cap of last element is less the min_mcap parameter
            if tokens[-1]['market_cap'] is not None and tokens[-1]['market_cap'] < min_mcap:
                print("[D] >>> 9837: returning {} tokens".format(len(tokens)))
                return (STATUS_OK, tokens)
        except Exception as e:
            print(tokens[-1]['market_cap'])
            print(min_mcap)
            print("[D] >>> 438956 something went wrong when checking market cap data. Returning the list but may be corrupted. \n\tError {}".format(e))
            return (STATUS_UNKNOWN, tokens)

        # increment the request page
        request_page += 1

        # sleep for a little to not overload api
        time.sleep(sleep_time)

def get_complete_data(coin_id):
    """ makes /coins/{id} call to CoinGecko, gets all data 
        example link: 
        https://api.coingecko.com/api/v3/coins/solana?tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true
    """
    # generate url
    url = uri.URI_ALL_DATA.format(coin_id)
    # make GET request
    status, data = safe_GET(url,)
    # if successful, return the data
    if status == STATUS_OK:
        print("[D] >>> get_complete_data('{}') -> success ! ".format(coin_id))
        return (status, data)
    
    print("[D] >>> could not successfully retrieve data for '{}'".format(coin_id))
    return (status, data)

def get_historical_data(coin_id, num_days="max"):
    """ param num_days: options are: 1, 2, ... any & 'max' 
        granularity is the following:
            for 1 day       : 5 minutes
            up to 90 days   : 1 hour
            90+ days        : 1 day 
            'max'           : 1 day 
        example link:
        "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1"

        returns:
        {
            "prices" :          [ {'time': unix_timestamp, 'value': value}, ... ]
            "market_caps" :     [ {'time': unix_timestamp, 'value': value}, ... ]
            "total_volumes" :   [ {'time': unix_timestamp, 'value': value}, ... ]
        }
        returns list of tuples: [(timestamp, price), ... ] """
    result = { "prices" : [], "market_caps" : [], "total_volumes" : [] }
    # generate url
    url = uri.URI_HISTORICAL.format(coin_id, num_days)
    # make GET request
    status, data = safe_GET(url)
    # if unsuccessful, just return empty data
    if status != STATUS_OK:
        print("[D] >>> get_historical_data('{}','{}') --> fail. Returning empty ".format(coin_id, num_days))
        return (status, result)
    
    # if status is Ok, then we convert the data in our format
    def safe_add_element(result_dict_object, timestamp, value):
        try:
            result_dict_object.append({'time' : timestamp, 'value' : value} )
        except Exception as e:
            print("[D] >>> error 7328648 when formatting historical data\n{}\nReturning partial result".format(e))
            return (e, result)
    try:
        # append prices
        for data_point in data['prices']: safe_add_element(result['prices'], data_point[0], data_point[1])
        # append market caps
        for data_point in data['market_caps']: safe_add_element(result['market_caps'], data_point[0], data_point[1])
        # append total volumes
        for data_point in data['total_volumes']: safe_add_element(result['total_volumes'], data_point[0], data_point[1])
    except Exception as e:
        print("[D] >>> error 425323 when formatting historical data\n{}\nReturning partial result".format(e))
        return (e, result)

    # if we got here everything should be fine, so we return the result
    print("[D] >>> success for get_historical_data(coin_id='{}', num_days={})".format(coin_id, num_days))
    return (STATUS_OK, result)

# test function (called from __init__.py)
def foo():
    pass
    sleep_time = config.sleep_time

    # testing all markets
    # status, markets = get_market_data(1000000, sleep_time)
    # log.log( log.prettify_list(markets), "market_data.txt")

    # testing solana markets
    # status, markets = get_market_data(50000000, sleep_time, 
    #         only_solana_ecosystem=True)
    # log.log( log.prettify_list(markets), "solana_market_data.txt")

    # getting complete data
    # status, data = get_complete_data("bitcoin")
    # log.log(data, "bitcoin.txt")

    # getting historical data
    status, data = get_historical_data(coin_id="solana", num_days=config.MAX_DAYS_FOR_1D_DATA_INTERVAL)
    log.log(data, "solana_historical.txt")
    print(status)