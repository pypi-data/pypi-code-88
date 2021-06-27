import jellyfish
from loguru import logger

def get_closest_matched_field_in_dicts(search_result_list,
                                       search_string,
                                       key_field,
                                       minimal_comparison_score=0.0):
    """

    :param search_result_list: List of dicts to to add value to
    :param search_string: string to search
    :param key_field: field to compare against in dicts
    :return: best_matched_result - the dict that proved to have the best
            match to the search string, Just takes a max so
             if there are multiple 1.0 matches it is ignored
    """
    if len(search_result_list) > 0:
        for result in search_result_list:
            result['comparison_score'] = jellyfish.jaro_distance(
                search_string, result[key_field])

        if minimal_comparison_score != 0.0:
            if max(search_result_list,
                   key=lambda x: x['comparison_score'])["comparison_score"] < minimal_comparison_score:
                logger.error("Below minimum expected result")
                return

        # Implicit else with the return above
        best_matched_result = max(search_result_list,
                                  key=lambda x: x['comparison_score'])
        return best_matched_result
    else:
        logger.error("result list cannot be 0")
