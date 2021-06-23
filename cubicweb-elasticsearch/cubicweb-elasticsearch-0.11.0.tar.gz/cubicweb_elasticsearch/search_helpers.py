# -*- coding: utf-8 -*-
# copyright 2016-2021 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import re

from elasticsearch_dsl import Q, query as dsl_query

SIMPLE_QUERY_OPERATORS = '|+-"()*~'
SIMPLE_QUERY_OPERATORS_RE = r"[\|\+\-\"\(\)\*\~]"


def is_simple_query_string(query):
    """
    Define if the query contains any of operators supported by simple_query_string

    query:
        text of the query to be composed (can contain quotes)

    In ES the simple_query_string query supports the following operators:

    + signifies AND operation
    | signifies OR operation
    - negates a single token
    " wraps a number of tokens to signify a phrase for searching
    * at the end of a term signifies a prefix query
    ( and ) signify precedence
    ~N after a word signifies edit distance (fuzziness)
    ~N after a phrase signifies slop amount

    https://www.elastic.co/guide/en/elasticsearch/reference/7.9/query-dsl-simple-query-string-query.html"""  # noqa
    # for all operators except "-", if it appears, then we assume it is a simple query
    for operator in SIMPLE_QUERY_OPERATORS.replace("-", ""):
        if operator in query:
            return True

    # in the case of the "-" operator, we accept it only if it is at the beginning of the query
    # or after a space or an operator
    # queries like "mont-saint-michel" should not be regarded as simple_query_string
    if query.startswith("-"):
        return True

    if " -" in query:
        return True

    return False


def compose_search(
    search, query=None, fields=(), fuzzy=False, phrase=True, common=True
):
    """
    Compose a elasticsearch-dsl query from queries :

    * simple term
    * simple terms (OR)
    * negation (add - in front of a term)
    * explicit OR
    * quoted terms (AND)

    search:
        search object (used to set doc_type and index_name outside of
        compose_search)
    query:
        text of the query to be composed (can contain quotes)
    fields:
        restrict and boost search on certain fields eg. ('title^2', 'alltext')
    fuzzy:
        add a fuzzy search element to part of the query generated
        https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html
    """
    must = []
    must_not = []
    should = []

    if is_simple_query_string(query):
        query_string = Q(
            "simple_query_string", query=query, fields=fields, default_operator="and"
        )
        should.append(query_string)

    else:
        if not phrase and not common:  # invalid combination
            phrase = common = True
        if phrase:
            phrase_query = Q(
                "multi_match", query=query, type="phrase", slop=50, fields=fields
            )
            should.append(phrase_query)
        # highfrequency/lowfrequency query
        # https://www.elastic.co/blog/stop-stopping-stop-words-a-look-at-common-terms-query
        if common:
            common_query = dsl_query.Common(
                alltext={
                    "query": query,
                    "cutoff_frequency": 0.001,
                    "low_freq_operator": "and",
                    "minimum_should_match": {"high_freq": "70%"},
                }
            )
            should.append(common_query)

    if fuzzy:
        elements = re.sub(SIMPLE_QUERY_OPERATORS_RE, " ", query).split()
        for element in elements:
            if fuzzy:
                should.append(dsl_query.Fuzzy(alltext=element.replace('"', "")))
    bool_query = dsl_query.Bool(
        must=must,
        must_not=must_not,
        should=should,
        minimum_should_match=1,
    )
    search.query = bool_query
    return search
