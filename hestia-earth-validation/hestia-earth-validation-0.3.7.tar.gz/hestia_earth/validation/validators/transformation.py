from hestia_earth.validation.utils import _filter_list_errors


def validate_previous_transformation(transformations: list):
    indexes = range(len(transformations))

    def _term_index(term_id: str, max_index: int):
        return next((i for i in indexes if transformations[i].get('term', {}).get('@id') == term_id), max_index)

    def validate(index: int):
        term_id = transformations[index].get('previousTransformationTerm', {}).get('@id')
        return term_id is None or _term_index(term_id, index) < index or {
            'level': 'error',
            'dataPath': f".transformations[{index}].previousTransformationTerm",
            'message': 'must point to a previous transformation in the list'
        }

    return _filter_list_errors(map(validate, indexes))
