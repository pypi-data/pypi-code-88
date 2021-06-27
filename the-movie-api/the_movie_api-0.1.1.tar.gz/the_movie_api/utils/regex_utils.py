import re

movie_group_pattern = r"(^.+)(194[1-9]|19[5-9][0-9]|200[0-9]|201[0-9]|202[0-9])"

def extract_year_and_movie_name(string_to_check):
    movie_comp = re.compile(movie_group_pattern, re.IGNORECASE | re.DOTALL)
    movie_match = movie_comp.match(string_to_check)
    if movie_match is not None:
        clean_movie_name = movie_match.group(1)
        year_released = movie_match.group(2)
        return clean_movie_name, year_released
    else:
        return None, None
