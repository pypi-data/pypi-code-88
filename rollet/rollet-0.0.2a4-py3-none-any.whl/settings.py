"""
Rollet settings and its methods
"""

__all__ = ["ABSTRACT"]

from rollet.extractor import *

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))


# CSS rules selectors for each field
ABSTRACT = (
    *[f':is(div,section)[{attr}*="{value}" i]' for attr in ('class', 'id')
    for value in ('-abstract', 'abstract')],
    'meta[name="dc.description" i]',
    'meta[property="og:description" i]',
    *[f'meta[name="{attr}" i]'
    for attr in ('description', 'twitter:description', 'citation_abstract')],
    *[f'div[{attr}*="article" i][{attr}*="body" i]'
    for attr in ('class', 'itemprop')],
    'div[class*=content i]',
    'script[type*="json" i]',
    *[f':is(div,section)[{attr}*="abs" i]' for attr in ('class', 'id')],
    *[f'div[class="{attr}" i]' for attr in ('desc', 'new-txt', 'contenuto')]
)

TITLE = (
    'meta[property="og:title" i]',
    *[f'meta[name="{attr}" i]'
    for attr in ('citation_title', 'dc.title', 'twitter:title', 'title')],
    'script[type*="json" i]',
    *[f':is(h1,h2,h3,div,span)[{attr}*=title i]'
    for attr in ('class', 'id', 'itemprop')],
    *[f':is(h1,h2,h3)[itemprop*=head i]'],
    'title'
)

# Domains types
types = {
    'article': [
        'agronews', 'ansa', 'berkeley', 'citrusindustry', 'europa', 'europafm',
        'europalibera', 'europapress', 'europatat', 'floraldaily',
        'freshfruitportal', 'freshplaza', 'groentennieuws', 'hortidaily',
        'hortweek', 'huffingtonpost', 'ica', 'mon-viti', 'nieuweoogst', 'nvwa',
        'oliveoiltimes', 'phytoma', 'phytoma-ldv', 'teatronaturale',
        'terrenature', 'theguardian', 'usda', 'vniikr'
    ],
    'paper': [
        'apsnet', 'biorxiv', 'chinapubmed', 'europepmc', 'mdpi', 'nature',
        'nih', 'nl', 'researchgate', 'sciencedirect', 'springer',
        'srpingeropen', 'wiley'
    ]
}
TYPES = dict(sum([[(i,k) for i in v] for k,v in types.items()], []))

# Types defaults keywords arguments for fetch
FETCH_KWARGS = {
    'default': {
        'abstract__which': 'max',
        'abstract__script_keys': [],
        'lang__attr': 'lang',
        'title__which': 'first',
        'title__script_keys': []
    },'article': {
        'abstract__which': 'max',
        'abstract__script_keys': ['abstract', 'summary'],
        'lang__attr': 'lang',
        'title__which': 'first',
        'title__script_keys': ['title', 'heading']
    },
    'paper': {
        'abstract__which': 'first',
        'abstract__script_keys': ['abstract', 'summary'],
        'lang__attr': 'lang',
        'title__which': 'first',
        'title__script_keys': ['title', 'heading', 'name']
    },
}

# Blacklisted domains
with open(os.path.join(dir_path, 'blacklist'), errors = 'ignore') as f:
    BLACKLIST = list(map(lambda x:x.strip(), f.readlines()))

# Custom domains extractors
# {domain: [(schema1, Extractor1), (schema2, Extractor2)]}
EXTRACTORS = {
    'default': [(r'.*', BaseExtractor),],
    'mdpi': [(r'.*', MdpiExtractor),],
    'nih': [(r'.*', NihExtractor),],
    'sciencedirect': [(r'.*', ScienceDirectExtractor),],
}

# Methods

def add_types(dict_types):
    """
    Add new type domains
    dict_types: dict, {type: [domain1, domain2, ...],}
    :return: None
    """
    global TYPES
    news = dict(sum([[(i,k) for i in v] for k,v in dict_types.items()], []))
    TYPES = {**TYPES, **news}


def add_fetch_kwargs(dict_types):
    """
    Add new fetch kwargs for type domains
    dict_types: dict, {type: {kwargs1:value1, kwargs2:value2,},}
    :return: None
    """
    global FETCH_KWARGS
    news = FETCH_KWARGS.copy()
    for d_type, key_args in dict_types.items():
        news[d_type] = {**news.get(d_type, news['default']), **key_args}
    FETCH_KWARGS = news.copy()