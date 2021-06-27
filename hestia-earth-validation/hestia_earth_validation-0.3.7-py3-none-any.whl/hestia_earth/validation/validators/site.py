from hestia_earth.schema import SiteSiteType
from hestia_earth.utils.tools import flatten

from hestia_earth.validation.gee import fetch_data
from .shared import (
    validate_dates, validate_list_dates, validate_list_dates_format, validate_list_duplicates, validate_list_min_max,
    validate_region_in_country, validate_country, validate_is_region, validate_coordinates, need_validate_coordinates,
    validate_area, need_validate_area, validate_list_term_percent, validate_linked_source_privacy,
    validate_list_date_lt_today, validate_date_lt_today, validate_properties_default_value
)
from .infrastructure import validate_lifespan
from .measurement import validate_soilTexture, validate_depths, validate_value_min_max, validate_term_unique
from .practice import validate_cropResidueManagement, validate_longFallowPeriod


INLAND_TYPES = [
    SiteSiteType.CROPLAND.value,
    SiteSiteType.PERMANENT_PASTURE.value,
    SiteSiteType.POND.value,
    SiteSiteType.ANIMAL_HOUSING.value,
    SiteSiteType.FACTORY.value,
    SiteSiteType.FOREST.value,
    SiteSiteType.OTHER_NATURAL_VEGETATION.value
]

SITE_TYPES_VALID_VALUES = {
    SiteSiteType.CROPLAND.value: [25, 35, 36],
    SiteSiteType.FOREST.value: [10, 20, 25]
}


def validate_site_dates(site: dict):
    return validate_dates(site) or {
        'level': 'error',
        'dataPath': '.endDate',
        'message': 'must be greater than startDate'
    }


def validate_site_coordinates(site: dict):
    return need_validate_coordinates(site) and site.get('siteType') in INLAND_TYPES


def validate_siteType(site: dict):
    site_type = site.get('siteType')
    values = SITE_TYPES_VALID_VALUES.get(site_type, [])
    values_str = ', '.join(map(lambda v: str(v), values))

    def validate():
        value = fetch_data(collection='MODIS/006/MCD12Q1',
                           ee_type='raster_by_period',
                           band_name='LC_Prop2',
                           year='2019',
                           latitude=site.get('latitude'),
                           longitude=site.get('longitude')).get('mean')
        return value in values

    return len(values) == 0 or validate() or {
        'level': 'warning',
        'dataPath': '.siteType',
        'message': ' '.join([
            'The coordinates you have provided are not in a known',
            site_type,
            f"area according to the MODIS Land Cover classification (MCD12Q1.006, LCCS2, bands {values_str})."
        ])
    }


def validate_site(site: dict, nodes=[]):
    """
    Validates a single `Site`.

    Parameters
    ----------
    site : dict
        The `Site` to validate.
    nodes : list
        The list of all nodes to do cross-validation.

    Returns
    -------
    List
        The list of errors for the `Site`, which can be empty if no errors detected.
    """
    return [
        validate_site_dates(site),
        validate_date_lt_today(site, 'startDate'),
        validate_date_lt_today(site, 'endDate'),
        validate_linked_source_privacy(site, 'defaultSource', nodes),
        validate_siteType(site) if need_validate_coordinates(site) else True,
        validate_country(site) if 'country' in site else True,
        validate_is_region(site) if 'region' in site else True,
        validate_region_in_country(site) if 'region' in site else True,
        validate_coordinates(site) if validate_site_coordinates(site) else True,
        validate_area(site) if need_validate_area(site) else True
    ] + flatten([
        validate_list_dates(site, 'measurements'),
        validate_list_dates_format(site, 'measurements'),
        validate_list_date_lt_today(site, 'measurements', ['startDate', 'endDate']),
        validate_list_min_max(site, 'measurements'),
        validate_list_term_percent(site, 'measurements'),
        validate_soilTexture(site.get('measurements')),
        validate_depths(site.get('measurements')),
        validate_value_min_max(site.get('measurements')),
        validate_list_duplicates(site, 'measurements', [
            'term.@id',
            'methodModel.@id',
            'methodModelDescription',
            'startDate',
            'endDate',
            'depthUpper',
            'depthLower'
        ]),
        validate_term_unique(site.get('measurements')),
        validate_properties_default_value(site, 'measurements', 'properties')
    ] if 'measurements' in site else []) + flatten([
        validate_list_dates(site, 'infrastructure'),
        validate_list_dates_format(site, 'infrastructure'),
        validate_list_date_lt_today(site, 'infrastructure', ['startDate', 'endDate']),
        validate_lifespan(site.get('infrastructure'))
    ] if 'infrastructure' in site else []) + flatten([
        validate_list_dates(site, 'practices'),
        validate_list_dates_format(site, 'practices'),
        validate_list_date_lt_today(site, 'practices', ['startDate', 'endDate']),
        validate_list_min_max(site, 'practices'),
        validate_list_term_percent(site, 'practices'),
        validate_cropResidueManagement(site.get('practices')),
        validate_longFallowPeriod(site.get('practices')),
        validate_properties_default_value(site, 'practices', 'properties')
    ] if 'practices' in site else [])
