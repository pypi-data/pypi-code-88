import json
import time
from datetime import datetime, timedelta

import requests
from elasticsearch6 import Elasticsearch
from requests.auth import HTTPBasicAuth

from shangqi_cloud_lib.context import config


def elasticsearch_connect():
    es_client = Elasticsearch(
        [{'host': "120.92.112.118", 'port': 9210}, ],
        http_auth=("elastic", "esTupu@2020"),
        sniff_on_start=False
    )

    return es_client


def send_es_get_scroll(bool_must_list=None, route_key="", param_list=None, scroll="5m"):
    find_condition = {
        "query": {
            "bool": {
                "must": bool_must_list
            }
        },
        "size": 10000,

    }
    if param_list:
        find_condition["_source"] = {"include": param_list}
    r = requests.post(
        "http://120.92.112.118:9210/{}/_search?scroll={}".format(route_key, scroll),
        data=json.dumps(find_condition),
        headers={'content-type': "application/json"},
        auth=HTTPBasicAuth('elastic', 'esTupu@2020')
    )
    res = r.json()
    return res


def send_es_by_scroll(scroll_id="", scroll="5m"):
    r = requests.post(
        "http://120.92.112.118:9210/_search/scroll",
        data=json.dumps({
            "scroll": scroll,
            "scroll_id": scroll_id}),
        headers={'content-type': "application/json"},
        auth=HTTPBasicAuth('elastic', 'esTupu@2020')
    )
    res = r.json()
    return res


def send_es_post(bool_must_list=None, param_list=None, route_key="", sort_list=None, size=10, offset=0,
                 track_total_hits=False):
    params = {
        "query": {
            "bool": {
                "must": bool_must_list
            }
        },
        "size": size,
        "from": offset,
    }
    if track_total_hits:
        params["track_total_hits"] = track_total_hits
    if param_list:
        params["_source"] = {"include": param_list}
    if sort_list:
        params["sort"] = sort_list

    r = requests.post(
        config.es_url.format(route_key),
        data=json.dumps(params),
        headers={'content-type': "application/json"},
        auth=HTTPBasicAuth('elastic', 'esTupu@2020')
    )
    res = r.json()
    return res["hits"]


def format_es_return(bool_must_list=None, param_list=None, route_key="", sort_list=None, size=10, offset=0,
                     track_total_hits=False, res=None):
    if not res:
        res = send_es_post(bool_must_list, param_list, route_key=route_key, sort_list=sort_list, size=size,
                           offset=offset,
                           track_total_hits=track_total_hits)

    result_list = []
    for r in res["hits"]:
        if param_list:
            result_dict = {}
            for key in param_list:
                key_list = key.split(".")
                value = r["_source"]
                for key in key_list:
                    if isinstance(value, list):
                        if value:
                            value = [v[key] for v in value]

                    elif isinstance(value, dict):
                        if value:
                            value = value.get(key, None)
                    else:
                        pass
                if result_dict.get(key) is None:
                    if value:
                        result_dict[key] = value

            result_dict["_id"] = r["_id"]
        else:
            result_dict = r["_source"]
            result_dict["_id"] = r["_id"]
        result_list.append(result_dict)
    result_dict = {
        "data_count": res["total"]["value"],
        "data_list": result_list
    }
    return result_dict


def es_condition_by_match_phrase(bool_list, column, param, slop=0):
    if param:
        if isinstance(param, list):
            bool_list.append({
                "match_phrase": {
                    column: {
                        "query": param[0],
                        "slop": slop
                    }
                }
            })
        if isinstance(param, str):
            bool_list.append({
                "match_phrase": {
                    column: {
                        "query": param,
                        "slop": slop
                    }
                }
            })


def es_condition_by_not_null(boo_must_list, column, param):
    if param:
        boo_must_list.append({
            "exists": {
                "field": column
            }
        })


def es_condition_by_range(bool_must_list, column, date_list, is_contain_end_date=False):
    if date_list:
        range_dict = {}
        if date_list[0]:
            range_dict["gte"] = date_list[0]
        if len(date_list) == 2 and date_list[1]:
            if "-" in str(date_list[1]) and is_contain_end_date:
                end_date = str((datetime.strptime(date_list[1], '%Y-%m-%d') + timedelta(days=1)).strftime("%Y-%m-%d"))
            else:
                end_date = date_list[1]
            range_dict["lt"] = end_date
        bool_must_list.append({
            "range": {
                column: range_dict
            }})


def es_condition_by_terms(bool_must_list, column, param_list):
    if param_list:
        bool_must_list.append({
            "terms": {
                column: param_list
            }})


def es_condition_by_exist(bool_must_list, param):
    if param:
        bool_must_list.append({
            "exists": {
                "field": param
            }})


def es_condition_by_not_in(bool_must_list: list = None, column="", param_list=None):
    if param_list:
        bool_must_list.append({
            "bool": {
                "must_not": {
                    "terms": {
                        column: param_list
                    }}
            }

        })


def format_bool_must_and_should(bool_must_list, bool_should_more_list):
    if bool_should_more_list:
        for bool_should in bool_should_more_list:
            bool_must_list.append({
                "bool": {
                    "should": bool_should
                }
            })


def format_bool_must_and_must_not(bool_must_list, bool_must_not_more_list):
    if bool_must_not_more_list:
        for bool_must_not in bool_must_not_more_list:
            bool_must_list.append({
                "bool": {
                    "must_not": bool_must_not
                }
            })


def parse_es_sort_list(column, order):
    if order == "asc":
        sort_list = [
            {
                column: {
                    "order": order,
                    "missing": "_first"
                }
            }
        ]
    else:
        sort_list = [
            {
                column: {
                    "order": order
                }
            }
        ]

    return sort_list
