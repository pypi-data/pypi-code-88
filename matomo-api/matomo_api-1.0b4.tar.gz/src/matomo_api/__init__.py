"""Python wrapper for the Matomo Reporting API."""

__all__ = [
    'MatomoApi',
    'idSite', 'date', 'period', 'col', 'format', 'language', 'segment',
    'hideColumns', 'showColumns', 'filter_limit', 'idSubtable', 'expanded',
    'flat', 'convertToUnicode', 'translateColumnNames', 'label', 'pivotBy',
    'pivotByColumn', 'pivotByColumnLimit', 'filter_offset', 'filter_truncate',
    'filter_pattern', 'filter_column', 'filter_sort_order',
    'filter_sort_column', 'filter_excludelowpop', 'filter_excludelowpop_value',
    'filter_column_recursive', 'filter_pattern_recursive',
    'disable_generic_filters', 'disable_queued_filters', 'pageUrl',
    'idCustomReport', 'idDashboard', 'copyToUser', 'login', 'userLogin',
    'dashboardName',
    'par_val'
]

from .module_methods import MatomoApi
from .parameter_specifications import *
