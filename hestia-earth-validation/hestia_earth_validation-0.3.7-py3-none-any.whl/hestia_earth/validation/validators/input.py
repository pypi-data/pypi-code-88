from hestia_earth.schema import TermTermType
from hestia_earth.utils.model import find_term_match
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.tools import non_empty_list

from hestia_earth.validation.utils import _filter_list_errors

MUST_INCLUDE_ID_COL = column_name('mustIncludeId')
MUST_INCLUDE_ID_TERM_TYPES = [
    TermTermType.INORGANICFERTILIZER.value
]


def validate_must_include_id(inputs: list):
    def missingRequiredIds(term: dict):
        term_id = term.get('@id')
        lookup = download_lookup(f"{term.get('termType')}.csv", True)
        other_term_ids = (get_table_value(lookup, 'termid', term_id, MUST_INCLUDE_ID_COL) or '').split(',')
        return non_empty_list([
            term_id for term_id in other_term_ids if find_term_match(inputs, term_id, None) is None
        ])

    def validate(values: tuple):
        index, input = values
        term = input.get('term', {})
        should_validate = term.get('termType') in MUST_INCLUDE_ID_TERM_TYPES
        missing_ids = missingRequiredIds(term) if should_validate else []
        return len(missing_ids) == 0 or {
            'level': 'error',
            'dataPath': f".inputs[{index}]",
            'message': f"should add missing inputs: {', '.join(missing_ids)}"
        }

    return _filter_list_errors(map(validate, enumerate(inputs)))
