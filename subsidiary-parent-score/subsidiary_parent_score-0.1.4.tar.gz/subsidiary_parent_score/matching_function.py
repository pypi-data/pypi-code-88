import pandas as pd

import unicodedata
import importlib.resources as pkg_resources

from company_name_matching import DefaultMatching


def subsidiary_parent_with_country(company_name1, company_name2):
    entity_matching = DefaultMatching()
    # 1st normalization
    lhs_normalized = u"".join([c for c in unicodedata.normalize('NFKD', company_name1.casefold()) if not unicodedata.combining(c)])
    rhs_normalized = u"".join([c for c in unicodedata.normalize('NFKD', company_name2.casefold()) if not unicodedata.combining(c)])
    characters = ['.', ',', '/', '\\', '\'', '(', ')', '’', '-']
    # remove special characters
    for character in characters:
        lhs = lhs_normalized.replace(character, ' ').replace("  "," ")
        rhs = rhs_normalized.replace(character, ' ').replace("  "," ")
    # check if there is a country name in one of the company names
    lhs_country = False
    rhs_country = False
    country_names_csv = pkg_resources.open_text('subsidiary_parent_score', 'countries_name.csv')
    country_names = [name.lower() for name in pd.read_csv(country_names_csv)["name"]]
    for country in country_names:
        if country in lhs:
            lhs_country = True
            lhs = lhs.replace(country, "").strip()
        if country in rhs:
            rhs_country = True
            rhs = rhs.replace(country, "").strip()
        if lhs_country and rhs_country:
            break
    if lhs_country == rhs_country:
        return None, 0
    if lhs_country:
        flag = "subsidiary"
    elif rhs_country:
        flag = "parent"
    return flag, entity_matching.match(lhs, rhs).score