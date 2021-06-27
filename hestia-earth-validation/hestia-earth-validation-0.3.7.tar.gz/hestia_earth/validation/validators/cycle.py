from hestia_earth.schema import SchemaType, CycleFunctionalUnitMeasure, SiteSiteType, TermTermType
from hestia_earth.utils.tools import flatten
from hestia_earth.utils.date import diff_in_days, is_in_days
from hestia_earth.utils.api import find_node

from hestia_earth.validation.utils import _find_linked_node, _value_average, _list_sum_terms
from .shared import (
    validate_dates, validate_list_dates, validate_date_lt_today, validate_list_duplicates, validate_list_min_max,
    validate_list_term_percent, validate_linked_source_privacy, validate_list_dates_length, validate_list_date_lt_today,
    validate_properties_default_value, validate_list_model, validate_list_model_config, validate_list_dates_format
)
from .input import validate_must_include_id
from .practice import validate_cropResidueManagement, validate_longFallowPeriod
from .product import validate_economicValueShare, validate_value as validate_product_value
from .data_completeness import validate_dataCompleteness
from .transformation import validate_previous_transformation


SITE_TYPES_RESTRICTED = [
    SiteSiteType.CROPLAND.value,
    SiteSiteType.PERMANENT_PASTURE.value
]
PRODUCTS_MODEL_CONFIG = {
    'aboveGroundCropResidueTotal': {
        'level': 'warning',
        'model': 'ipcc2006',
        'delta': 0.5,
        'resetDataCompleteness': True
    }
}


def validate_cycle_dates(cycle: dict):
    return validate_dates(cycle) or {
        'level': 'error',
        'dataPath': '.endDate',
        'message': 'must be greater than startDate'
    }


def _should_validate_cycleDuration(cycle: dict):
    return 'cycleDuration' in cycle and is_in_days(cycle.get('startDate')) and is_in_days(cycle.get('endDate'))


def validate_cycleDuration(cycle: dict):
    duration = diff_in_days(cycle.get('startDate'), cycle.get('endDate'))
    return duration == round(cycle.get('cycleDuration'), 1) or {
        'level': 'error',
        'dataPath': '.cycleDuration',
        'message': f"must equal to endDate - startDate in days (~{duration})"
    }


def validate_functionalUnitMeasure(cycle: dict, site: dict):
    site_type = site.get('siteType')
    value = cycle.get('functionalUnitMeasure')
    expected = CycleFunctionalUnitMeasure._1_HA.value
    return site_type not in SITE_TYPES_RESTRICTED or value == expected or {
        'level': 'error',
        'dataPath': '.functionalUnitMeasure',
        'message': f"must equal to {expected}"
    }


def validate_sum_aboveGroundCropResidue(products: list):
    prefix = 'aboveGroundCropResidue'
    total_residue_index = next((n for n in range(len(products)) if 'Total' in products[n].get(
        'term', {}).get('@id') and products[n].get('term', {}).get('@id').startswith(prefix)), None)
    total_residue = None if total_residue_index is None else _value_average(products[total_residue_index])

    other_residues = list(filter(lambda n: n.get('term').get('@id').startswith(prefix)
                                 and 'Total' not in n.get('term').get('@id'), products))
    other_residues_ids = list(map(lambda n: n.get('term').get('@id'), other_residues))
    other_sum = sum([_value_average(node) for node in other_residues])

    return total_residue_index is None or len(other_residues) == 0 or (total_residue * 1.01) >= other_sum or {
        'level': 'error',
        'dataPath': f".products[{total_residue_index}].value",
        'message': f"must be more than or equal to ({' + '.join(other_residues_ids)})"
    }


def _crop_residue_terms():
    terms = find_node(SchemaType.TERM, {'termType': TermTermType.CROPRESIDUE.value})
    return [term.get('@id') for term in terms if term.get('@id')]


def validate_crop_residue_completeness(cycle: dict, site: dict):
    def validate_sum():
        products = cycle.get('products', [])
        terms = _crop_residue_terms()
        sum_above_ground = _list_sum_terms(products, list(filter(lambda term: term.startswith('above'), terms)))
        sum_below_ground = _list_sum_terms(products, list(filter(lambda term: term.startswith('below'), terms)))
        return all([sum_above_ground > 0, sum_below_ground > 0]) or {
            'level': 'error',
            'dataPath': '.products',
            'message': 'the sum of above ground crop residue and below ground crop residue must be greater than zero'
        }

    data_completeness = cycle.get('dataCompleteness', {}).get(TermTermType.CROPRESIDUE.value)
    site_type = site.get('siteType')
    return data_completeness is False or site_type not in SITE_TYPES_RESTRICTED or validate_sum()


def validate_cycle(cycle: dict, nodes=[]):
    """
    Validates a single `Cycle`.

    Parameters
    ----------
    cycle : dict
        The `Cycle` to validate.
    nodes : list
        The list of all nodes to do cross-validation.

    Returns
    -------
    List
        The list of errors for the `Cycle`, which can be empty if no errors detected.
    """
    site = _find_linked_node(nodes, cycle.get('site', {}))
    return flatten([
        validate_cycle_dates(cycle),
        validate_date_lt_today(cycle, 'startDate'),
        validate_date_lt_today(cycle, 'endDate'),
        validate_linked_source_privacy(cycle, 'defaultSource', nodes),
        validate_cycleDuration(cycle) if _should_validate_cycleDuration(cycle) else True,
        validate_dataCompleteness(cycle.get('dataCompleteness', {}), site) if 'dataCompleteness' in cycle else True
    ]) + flatten([
        validate_list_model(cycle, 'emissions'),
        validate_list_dates(cycle, 'emissions'),
        validate_list_dates_format(cycle, 'emissions'),
        validate_list_min_max(cycle, 'emissions'),
        validate_list_term_percent(cycle, 'emissions'),
        validate_list_dates_length(cycle, 'emissions'),
        validate_list_date_lt_today(cycle, 'emissions', ['startDate', 'endDate']),
        validate_list_duplicates(cycle, 'emissions', [
            'term.@id',
            'inputs.@id',
            'source.id',
            'methodModel.@id',
            'methodModelDescription',
            'startDate',
            'endDate',
            'dates'
        ]),
        validate_properties_default_value(cycle, 'emissions', 'properties')
    ] if len(cycle.get('emissions', [])) > 0 else []) + flatten([
        validate_list_dates(cycle, 'inputs'),
        validate_list_dates_format(cycle, 'inputs'),
        validate_list_dates_length(cycle, 'inputs'),
        validate_list_date_lt_today(cycle, 'inputs', ['startDate', 'endDate']),
        validate_list_min_max(cycle, 'inputs'),
        validate_list_term_percent(cycle, 'inputs'),
        validate_list_duplicates(cycle, 'inputs', [
            'term.@id',
            'source.id',
            'methodModelDescription',
            'operation',
            'startDate',
            'endDate',
            'dates'
        ]),
        validate_properties_default_value(cycle, 'inputs', 'properties'),
        validate_must_include_id(cycle['inputs'])
    ] if len(cycle.get('inputs', [])) > 0 else []) + flatten([
        validate_list_dates(cycle, 'products'),
        validate_list_dates_format(cycle, 'products'),
        validate_list_dates_length(cycle, 'products'),
        validate_list_date_lt_today(cycle, 'products', ['startDate', 'endDate']),
        validate_list_min_max(cycle, 'products'),
        validate_list_term_percent(cycle, 'products'),
        validate_economicValueShare(cycle.get('products')),
        validate_sum_aboveGroundCropResidue(cycle.get('products')),
        validate_product_value(cycle.get('products')),
        validate_properties_default_value(cycle, 'products', 'properties'),
        validate_crop_residue_completeness(cycle, site) if 'dataCompleteness' in cycle and site else True,
        validate_list_model_config(cycle, 'products', PRODUCTS_MODEL_CONFIG)
    ] if len(cycle.get('products', [])) > 0 else []) + flatten([
        validate_list_dates(cycle, 'practices'),
        validate_list_dates_format(cycle, 'practices'),
        validate_list_date_lt_today(cycle, 'practices', ['startDate', 'endDate']),
        validate_list_min_max(cycle, 'practices'),
        validate_list_term_percent(cycle, 'practices'),
        validate_cropResidueManagement(cycle.get('practices')),
        validate_longFallowPeriod(cycle.get('practices')),
        validate_properties_default_value(cycle, 'practices', 'properties')
    ] if len(cycle.get('practices', [])) > 0 else []) + flatten([
        validate_functionalUnitMeasure(cycle, site)
    ] if 'functionalUnitMeasure' in cycle and site else []) + flatten([
        validate_list_dates(cycle, 'transformations'),
        validate_list_dates_format(cycle, 'transformations'),
        validate_list_date_lt_today(cycle, 'transformations', ['startDate', 'endDate']),
        validate_previous_transformation(cycle.get('transformations')),
        validate_list_duplicates(cycle, 'transformations', [
            'term.@id'
        ])
    ] if len(cycle.get('transformations', [])) > 0 in cycle else [])
