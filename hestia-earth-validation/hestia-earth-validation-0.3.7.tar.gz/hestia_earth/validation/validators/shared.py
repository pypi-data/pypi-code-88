from functools import reduce
import os
from typing import List
import re
from hestia_earth.utils.tools import flatten, non_empty_list, safe_parse_float, list_sum
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import find_term_match

from hestia_earth.validation.geojson import get_geojson_area
from hestia_earth.validation.gee import is_enabled, id_to_level, get_region_id
from hestia_earth.validation.utils import (
    update_error_path, _filter_list_errors, _next_error, _same_properties, _value_average,
    _find_linked_node, _is_before_today, run_model_from_node, run_model
)


def validate_properties_same_length(node: dict, list_key: str, prop_key: str, prop_keys: list):
    def validate(values: tuple):
        index, blank_node = values
        value_len = len(blank_node.get(prop_key, ''))
        invalid_prop_key = next((
            key for key in prop_keys if blank_node.get(key) and len(blank_node.get(key)) != value_len), None)
        return value_len == 0 or invalid_prop_key is None or {
            'level': 'error',
            'dataPath': f".{list_key}[{index}].{invalid_prop_key}",
            'message': f"must have the same length as {prop_key}"
        }

    return _filter_list_errors(flatten(map(validate, enumerate(node.get(list_key, [])))))


def validate_date_lt_today(node: dict, key: str):
    return node.get(key) is None or _is_before_today(node.get(key)) or {
        'level': 'error',
        'dataPath': f".{key}",
        'message': "must be lower than today's date"
    }


def validate_list_date_lt_today(node: dict, list_key: str, node_keys: list):
    def validate(values: tuple):
        index, value = values
        errors = list(map(lambda key: {'key': key, 'error': validate_date_lt_today(value, key)}, node_keys))
        return _filter_list_errors(
            [update_error_path(error['error'], list_key, index) for error in errors if error['error'] is not True]
        )

    return _filter_list_errors(flatten(map(validate, enumerate(node.get(list_key, [])))))


def validate_dates(node: dict):
    start = node.get('startDate')
    end = node.get('endDate')
    return start is None or end is None or (len(start) <= 7 and len(end) <= 7 and end >= start) or end > start


def validate_list_dates(node: dict, list_key: str):
    def validate(values: tuple):
        index, value = values
        return validate_dates(value) or {
            'level': 'error',
            'dataPath': f".{list_key}[{index}].endDate",
            'message': 'must be greater than startDate'
        }

    return _filter_list_errors(map(validate, enumerate(node.get(list_key, []))))


def validate_list_dates_format(node: dict, list_key: str):
    return validate_properties_same_length(node, list_key, 'endDate', ['startDate'])


def validate_list_dates_length(node: dict, list_key: str):
    def validate(values: tuple):
        index, blank_node = values
        value = blank_node.get('value')
        dates = blank_node.get('dates')
        return value is None or dates is None or len(dates) == len(value) or {
            'level': 'error',
            'dataPath': f".{list_key}[{index}].dates",
            'message': 'must contain ' + str(len(value)) + (' values' if len(value) > 1 else ' value')
        }

    return _filter_list_errors(map(validate, enumerate(node.get(list_key, []))))


def _compare_min_max(value1, value2): return value1 <= value2


def _compare_list_min_max(list1: list, list2: list):
    def compare_enum(index: int):
        valid = _compare_min_max(list1[index], list2[index])
        return True if valid is True else index

    return len(list1) != len(list2) or \
        next((x for x in list(map(compare_enum, range(len(list1)))) if x is not True), True)


def validate_list_min_max(node: dict, list_key: str):
    def validate(values: tuple):
        index, value = values
        min = value.get('min', 0)
        max = value.get('max', 0)
        skip_compare = (
            isinstance(min, list) and not isinstance(max, list)
        ) or (
            isinstance(max, list) and not isinstance(min, list)
        )
        compare_lists = isinstance(min, list) and isinstance(max, list)
        is_valid = True if skip_compare else \
            _compare_list_min_max(min, max) if compare_lists else _compare_min_max(min, max)
        return is_valid is True or {
            'level': 'error',
            'dataPath': f".{list_key}[{index}].max",
            'message': 'must be greater than min'
        }

    return _next_error(list(map(validate, enumerate(node.get(list_key, [])))))


def validate_list_duplicates(node: dict, list_key: str, props: List[str]):
    def validate(values: tuple):
        [index, value] = values
        values = node[list_key].copy()
        values.pop(index)
        duplicates = list(filter(_same_properties(value, props), values))
        return len(duplicates) == 0 or {
            'level': 'error',
            'dataPath': f".{list_key}[{index}]",
            'message': f"Duplicates found. Please make sure there is only one entry with the same {', '.join(props)}"
        }

    return _next_error(list(map(validate, enumerate(node.get(list_key, [])))))


def validate_list_term_percent(node: dict, list_key: str):
    def soft_validate(index: int, value): return 0 < value and value <= 1 and {
        'level': 'warning',
        'dataPath': f".{list_key}[{index}].value",
        'message': 'may be between 0 and 100'
    }

    def hard_validate(index: int, value): return (0 <= value and value <= 100) or {
        'level': 'error',
        'dataPath': f".{list_key}[{index}].value",
        'message': 'should be between 0 and 100 (percentage)'
    }

    def validate(values: tuple):
        index, value = values
        units = value.get('term', {}).get('units', '')
        value = _value_average(value, None)
        return units != '%' or value is None or type(value) == str or \
            soft_validate(index, value) or hard_validate(index, value)

    return _filter_list_errors(map(validate, enumerate(node.get(list_key, []))))


def validate_is_region(node: dict, region_key='region'):
    region_id = node.get(region_key, {}).get('@id', '')
    level = id_to_level(region_id)
    return level > 0 or {
        'level': 'error',
        'dataPath': f".{region_key}",
        'message': 'must not be a country'
    }


def validate_region_in_country(node: dict, region_key='region'):
    country = node.get('country', {})
    region_id = node.get(region_key, {}).get('@id', '')
    return region_id[0:8] == country.get('@id') or {
        'level': 'error',
        'dataPath': f".{region_key}",
        'message': 'must be within the country',
        'params': {
            'country': country.get('name')
        }
    }


def validate_country(node: dict):
    country_id = node.get('country', {}).get('@id', '')
    # handle additional regions used as country, like region-world
    is_region = country_id.startswith('region-')
    return is_region or bool(re.search(r'GADM-[A-Z]{3}$', country_id)) or {
        'level': 'error',
        'dataPath': '.country',
        'message': 'must be a country'
    }


def need_validate_coordinates(node: dict): return is_enabled() and 'latitude' in node and 'longitude' in node


def validate_coordinates(node: dict, region_key='region'):
    latitude = node.get('latitude')
    longitude = node.get('longitude')
    country = node.get('country', {})
    region = node.get(region_key)
    gadm_id = region.get('@id') if region else country.get('@id')
    id = get_region_id(gadm_id, latitude=latitude, longitude=longitude)
    return gadm_id == id or {
        'level': 'error',
        'dataPath': f".{region_key}" if region else '.country',
        'message': 'does not contain latitude and longitude',
        'params': {
            'gadmId': id
        }
    }


def need_validate_area(node: dict): return 'area' in node and 'boundary' in node


def validate_area(node: dict):
    try:
        area = get_geojson_area(node.get('boundary'))
        return area == round(node.get('area'), 1) or {
            'level': 'error',
            'dataPath': '.area',
            'message': f"must be equal to boundary (~{area})"
        }
    except KeyError:
        # if getting the geojson fails, the geojson format is invalid
        # and the schema validation step will detect it
        return True


N_A_VALUES = [
    '#n/a',
    '#na',
    'n/a',
    'na',
    'n.a',
    'nodata',
    'no data'
]


def validate_empty_fields(node: dict):
    keys = list(filter(lambda key: isinstance(node.get(key), str), node.keys()))

    def validate(key: str):
        return not node.get(key).lower() in N_A_VALUES or {
            'level': 'warning',
            'dataPath': f".{key}",
            'message': 'may not be empty'
        }

    return _filter_list_errors(map(validate, keys), False)


def validate_linked_source_privacy(node: dict, key: str, nodes: list):
    related_source = _find_linked_node(nodes, node.get(key, {}))
    node_privacy = node.get('dataPrivate')
    related_source_privacy = related_source.get('dataPrivate') if related_source else None
    return related_source_privacy is None or node_privacy == related_source_privacy or {
        'level': 'error',
        'dataPath': '.dataPrivate',
        'message': 'should have the same privacy as the related source',
        'params': {
            'dataPrivate': node_privacy,
            key: {
                'dataPrivate': related_source_privacy
            }
        }
    }


def _property_default_value(term_id: str, property_term_id: str):
    # load the term defaultProperties and find the matching property
    term = download_hestia(term_id)
    return safe_parse_float(find_term_match(term.get('defaultProperties', []), property_term_id).get('value'))


def _property_default_allowed_values(term_id: str):
    lookup = download_lookup('property.csv', True)
    allowed = get_table_value(lookup, 'termid', term_id, column_name('validationAllowedExceptions'))
    try:
        allowed_values = non_empty_list(allowed.split(';')) if allowed else []
        return [safe_parse_float(v) for v in allowed_values]
    # failure to split by `;` as single value allowed
    except AttributeError:
        return [safe_parse_float(allowed)]


def value_difference(value: float, expected_value: float):
    """
    Get the difference in percentage between a value and the expected value.

    Parameters
    ----------
    value : float
        The value to check.
    expected_value : float
        The expected value.

    Returns
    -------
    bool
        The difference in percentage between the value and the expected value.
    """
    return 0 if (isinstance(expected_value, list) and len(expected_value) == 0) or expected_value == 0 else (
        round(abs(value - expected_value) / expected_value, 4)
    )


def is_value_different(value: float, expected_value: float, delta: float = 0.05) -> bool:
    """
    Check the difference in percentage between a value and the expected value.

    Parameters
    ----------
    value : float
        The value to check.
    expected_value : float
        The value it should be close to.
    delta : float
        The accepted difference between the value and the expected one. Defaults to `5%`.

    Returns
    -------
    bool
        `True` if the value is within the percentage of the expected value, `False` otherwise.
    """
    return value_difference(value, expected_value) > delta


def validate_properties_default_value(node: dict, list_key: str, properties_key: str):
    def validate_properties(term_id: str, values: tuple):
        index, prop = values
        value = safe_parse_float(prop.get('value'))
        prop_term_id = prop.get('term', {}).get('@id')
        default_value = _property_default_value(term_id, prop_term_id)
        delta = value_difference(value, default_value)
        values_allowed = _property_default_allowed_values(prop_term_id)
        return delta < 0.25 or value in values_allowed or {
            'level': 'warning',
            'dataPath': f".{properties_key}[{index}].value",
            'message': 'should be within percentage of default value',
            'params': {
                'current': value,
                'default': default_value,
                'percentage': delta * 100
            }
        }

    def validate_nodes(values: tuple):
        index, value = values
        term_id = value.get('term', {}).get('@id')
        errors = _filter_list_errors(
            flatten(map(lambda v: validate_properties(term_id, v), enumerate(value.get(properties_key, [])))), False
        )
        return [update_error_path(error, list_key, index) for error in errors]

    return _filter_list_errors(flatten(map(validate_nodes, enumerate(node.get(list_key, [])))))


def _model_value_from_list(results: list, default_value: float):
    return results[0].get('value', [default_value]) if len(results) > 0 else default_value


def _model_value(result, default_value=0):
    return default_value if result is None else (
        _model_value_from_list(result, default_value) if isinstance(result, list) else (
            result.get('value', [default_value]) if isinstance(result, dict) else default_value
        )
    )


def _value_from_model(result):
    value = _model_value(result)
    return list_sum(value, value)


def _validate_list_model(node: dict, list_key: str):
    def validate(values: tuple):
        index, blank_node = values
        try:
            value = blank_node.get('value', [0])
            value = list_sum(value, value)
            expected_value = _value_from_model(run_model_from_node(blank_node, node))
            delta = value_difference(value, expected_value)
            return delta < 0.05 or {
                'level': 'error',
                'dataPath': f".{list_key}[{index}].value",
                'message': 'the value provided is not consistent with the model result',
                'params': {
                    'model': blank_node.get('methodModel', {}),
                    'term': blank_node.get('term', {}),
                    'current': value,
                    'expected': expected_value,
                    'delta': delta * 100
                }
            }
        except Exception:
            return True
    return validate


def validate_list_model(node: dict, list_key: str) -> list:
    """
    Validates a list using the engine models.
    This method will go through every element of the list and run the model that matches the
    `methodModel` and `term.@id` on the element.

    Parameters
    ----------
    node : dict
        The node containing the list to run.
    list_key : str
        The property of the node containing the list to run.

    Returns
    -------
    list
        List of errors from the models or `True` if no errors.
    """
    run = os.environ.get('VALIDATE_MODELS', 'true') == 'true'
    nodes = node.get(list_key, [])
    return _filter_list_errors(map(_validate_list_model(node, list_key), enumerate(nodes))) if run else []


def _reset_dataCompleteness(node: dict):
    dataCompleteness = node.get('dataCompleteness', {})
    dataCompleteness = reduce(lambda prev, curr: {**prev, curr: False}, dataCompleteness.keys(), dataCompleteness)
    return {**node, 'dataCompleteness': dataCompleteness}


def _validate_list_model_config(node: dict, list_key: str, conf: dict):
    def validate_model(term: dict, value: float, index: int, model_conf: dict):
        node_run = _reset_dataCompleteness(node) if model_conf.get('resetDataCompleteness', False) else node
        expected_result = run_model(model_conf['model'], term.get('@id'), node_run)
        expected_value = _value_from_model(expected_result)
        delta = value_difference(value, expected_value)
        return delta < model_conf['delta'] or {
            'level': model_conf.get('level', 'error'),
            'dataPath': f".{list_key}[{index}].value",
            'message': 'the value provided is not consistent with the model result',
            'params': {
                'model': expected_result[0].get('methodModel', {}),
                'term': term,
                'current': value,
                'expected': expected_value,
                'delta': delta * 100
            }
        }

    def validate(values: tuple):
        index, blank_node = values
        value = blank_node.get('value', [0])
        value = list_sum(value, value)
        term = blank_node.get('term', {})
        term_id = blank_node.get('term', {}).get('@id')
        # get the configuration for this element
        # if it does not exist, skip model
        term_conf = conf.get(term_id)
        return validate_model(term, value, index, term_conf) if term_conf else True

    return validate


def validate_list_model_config(node: dict, list_key: str, conf: dict):
    """
    Validates a list using the engine models.
    This method uses a configuration to determine which `term` in the elements should run.
    It does not use the `methodModel` that could be found on each element.

    Parameters
    ----------
    node : dict
        The node containing the list to run.
    list_key : str
        The property of the node containing the list to run.
    conf : dict
        The configuration to decide which models to run.

    Returns
    -------
    list
        List of errors from the models or `True` if no errors.
    """
    run = os.environ.get('VALIDATE_MODELS', 'true') == 'true'
    nodes = node.get(list_key, [])
    return _filter_list_errors(map(_validate_list_model_config(node, list_key, conf), enumerate(nodes))) if run else []
