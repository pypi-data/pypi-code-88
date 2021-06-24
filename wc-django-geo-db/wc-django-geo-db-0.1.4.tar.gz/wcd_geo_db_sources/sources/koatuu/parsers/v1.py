import json
from functools import reduce
from typing import Dict, Set, TYPE_CHECKING, TextIO, TypedDict, List, Optional
from enum import Enum
import tempfile

from wcd_geo_db.const import DivisionLevel

if TYPE_CHECKING:
    from ..process import KOATUUImportRunner


Hierarchy = Dict[str, Set[str]]


def json_encoder(e):
    if isinstance(e, set):
        return list(e)
    if isinstance(e, Enum):
        return str(e)
    else:
        raise TypeError(
            f'Object of type {e.__class__.__name__} is not serializable'
        )


class Field(str, Enum):
    LEVEL_1: str = 'Перший рівень'
    LEVEL_2: str = 'Другий рівень'
    LEVEL_3: str = 'Третій рівень'
    LEVEL_4: str = 'Четвертий рівень'
    CATEGORY: str = 'Категорія'
    TITLE: str = 'Назва об\'єкта українською мовою'


class EntityType(str, Enum):
    CITY = 'city'
    REGION = 'region'
    CITY_DISTRICT = 'city_district'
    MUNICIPALITY = 'municipality'
    COUNTY = 'county'
    TOWNSHIP = 'township'
    LOCALITY = 'locality'
    VILLAGE = 'village'
    HAMLET = 'hamlet'
    AGGREGATE = 'aggregate'


class Category(str, Enum):
    CITY = chr(1052)
    CITY_DISTRICT = chr(1056)
    TOWNSHIP = chr(1058)
    VILLAGE = chr(1057)
    HAMLET = chr(1065)


CATEGORY_TYPES = {
    None: {EntityType.AGGREGATE},
    Category.CITY: {EntityType.LOCALITY, EntityType.CITY},
    Category.CITY_DISTRICT: {EntityType.CITY_DISTRICT},
    Category.TOWNSHIP: {EntityType.LOCALITY, EntityType.TOWNSHIP},
    Category.VILLAGE: {EntityType.LOCALITY, EntityType.VILLAGE},
    Category.HAMLET: {EntityType.LOCALITY, EntityType.VILLAGE, EntityType.HAMLET},
}
CATEGORY_ALIASES = {
    chr(67): Category.VILLAGE,
}
CATEGORY_LEVELS = {
    Category.CITY: DivisionLevel.LOCALITY,
    Category.CITY_DISTRICT: DivisionLevel.SUBLOCALITY_LEVEL_1,
    Category.TOWNSHIP: DivisionLevel.LOCALITY,
    Category.VILLAGE: DivisionLevel.LOCALITY,
    Category.HAMLET: DivisionLevel.LOCALITY,
}
LEVELS_TYPES = {
    DivisionLevel.ADMINISTRATIVE_LEVEL_1: {EntityType.REGION},
    DivisionLevel.ADMINISTRATIVE_LEVEL_2: {EntityType.REGION, EntityType.MUNICIPALITY},
    DivisionLevel.ADMINISTRATIVE_LEVEL_3: {EntityType.COUNTY},
    DivisionLevel.LOCALITY: {EntityType.LOCALITY},
    DivisionLevel.SUBLOCALITY_LEVEL_1: {EntityType.CITY_DISTRICT},
}
HIERARCHY_LEVELS = {
    1: DivisionLevel.ADMINISTRATIVE_LEVEL_1,
    2: DivisionLevel.ADMINISTRATIVE_LEVEL_2,
    3: DivisionLevel.ADMINISTRATIVE_LEVEL_3,
    4: DivisionLevel.LOCALITY,
}
CODE_TYPES = {
    # міста обласного значення
    (3, 1): {EntityType.LOCALITY},
    # райони Автономної Республіки Крим, області
    (3, 2): {EntityType.REGION},
    # райони міст, що мають спеціальний статус
    (3, 3): {EntityType.CITY_DISTRICT},

    # міста районного значення
    (6, 1): {EntityType.LOCALITY, EntityType.CITY},
    # is unused
    (6, 2): set(),
    # райони в містах обласного значення
    (6, 3): {EntityType.CITY_DISTRICT},
    # селища міського типу, що входять до складу міськради
    (6, 4): {EntityType.LOCALITY, EntityType.TOWNSHIP},
    # селища міського типу, що входять до складу райради
    (6, 5): {EntityType.LOCALITY, EntityType.TOWNSHIP},
    # селища міського типу, що входять до складу райради в місті
    (6, 6): {EntityType.LOCALITY, EntityType.TOWNSHIP},
    # міста, що входять до складу міськради
    (6, 7): {EntityType.LOCALITY, EntityType.CITY},
    # сільради, що входять до складу райради
    (6, 8): {EntityType.COUNTY},
    # сільради, села, що входять до складу райради міста, міськради
    (6, 9): {EntityType.COUNTY},
}
TYPE_LEVELS = {
    EntityType.CITY: DivisionLevel.LOCALITY,
    EntityType.REGION: DivisionLevel.ADMINISTRATIVE_LEVEL_1,
    EntityType.CITY_DISTRICT: DivisionLevel.SUBLOCALITY_LEVEL_1,
    EntityType.MUNICIPALITY: DivisionLevel.ADMINISTRATIVE_LEVEL_2,
    EntityType.COUNTY: DivisionLevel.ADMINISTRATIVE_LEVEL_3,
    EntityType.TOWNSHIP: DivisionLevel.LOCALITY,
    EntityType.LOCALITY: DivisionLevel.LOCALITY,
    EntityType.VILLAGE: DivisionLevel.LOCALITY,
    EntityType.HAMLET: DivisionLevel.LOCALITY,
}


class Geo(TypedDict):
    code: str
    path: List[str]
    category: Optional[Category]
    title: Optional[str]
    types: List[EntityType]
    level: DivisionLevel


def get_path(raw: dict) -> List[str]:
    levels = [
        str(raw.get(x, '')) or None
        for x in (Field.LEVEL_1, Field.LEVEL_2, Field.LEVEL_3, Field.LEVEL_4)
    ]
    index, id = next(x for x in enumerate(reversed(levels)) if x[1] is not None)

    return levels[:len(levels) - index]


def get_category(c: str):
    if c in CATEGORY_ALIASES:
        c = CATEGORY_ALIASES[c]

    if c in Category._value2member_map_:
        return Category(c)

    return None


def code_types(code: str):
    return [(char, code[char-1]) for char in (2, 6)]


def get_types(geo: Geo):
    category = geo['category']
    types = set()

    if category:
        types |= CATEGORY_TYPES[category]

    for code_type in code_types(geo['code']):
        if code_type not in CODE_TYPES:
            continue

        types |= CODE_TYPES[code_type]

    return types


def get_level(geo: Geo):
    level = None
    category = geo['category']

    if category is not None:
        level = CATEGORY_LEVELS.get(category, None)

    if level is None:
        hierarchy_level = HIERARCHY_LEVELS[len(geo['path'])]

        type_levels = {
            TYPE_LEVELS[t]
            for t in geo['types']
            if t in TYPE_LEVELS
        }

        level = min((hierarchy_level, *type_levels))

    return level


def create_geo(raw: dict) -> Geo:
    path = get_path(raw)
    geo: Geo = Geo(
        code=path[-1],
        path=path,
        title=raw.get(Field.TITLE) or None,
        category=get_category(raw.get(Field.CATEGORY) or None),
    )
    geo['types'] = get_types(geo)
    geo['level'] = get_level(geo)

    if len(geo['types']) == 0:
        geo['types'] = set() | (LEVELS_TYPES.get(geo['level']) or set())

    return geo


def order_key(geo: Geo):
    return (len(geo['path']), geo['code'])


def collect_hierarchy(items: List[Geo]) -> Hierarchy:
    hierarchy: Hierarchy = {}

    for geo in items:
        parent = None

        for item in geo['path']:
            if parent is not None:
                hierarchy[parent] = hierarchy.get(parent) or set()
                hierarchy[parent].add(item)

            parent = item

    return hierarchy


def safe_remove(items: set, value) -> set:
    if value in items:
        items.remove(value)

    return items


def postprocess_items(items: List[Geo], hierarchy: Hierarchy) -> List[Geo]:
    index_map = {
        item['code']: index
        for index, item in enumerate(items)
    }
    for item in items:
        if item['level'] != DivisionLevel.LOCALITY:
            for code in hierarchy.get(item['code'], []):
                # Fixing all cities with city districts inside that are marked in some other way.
                if items[index_map[code]]['level'] in {
                    DivisionLevel.SUBLOCALITY_LEVEL_1,
                    DivisionLevel.SUBLOCALITY_LEVEL_2,
                    DivisionLevel.SUBLOCALITY_LEVEL_3,
                }:
                    item['category'] = Category.CITY
                    item['level'] = DivisionLevel.LOCALITY
                    safe_remove(item['types'], EntityType.REGION)
                    safe_remove(item['types'], EntityType.MUNICIPALITY)
                    safe_remove(item['types'], EntityType.COUNTY)
                    item['types'].add(EntityType.LOCALITY)
                    item['types'].add(EntityType.CITY)

    return items


def parse(runner: 'KOATUUImportRunner', file: TextIO):
    data = json.loads(file.read())
    items = list(sorted(map(create_geo, data), key=order_key))
    hierarchy = collect_hierarchy(items)
    items = postprocess_items(items, hierarchy)
    items_slice = items[20:50]
    zaliz = next(item for item in items if item['code'] == '0110136300')
    rr = hierarchy['1200000000']

    def reducer(acc, x):
        acc[x['category']] = acc.get(x['category'], 0)
        acc[x['category']] += 1

        return acc

    stats = reduce(reducer, items, {})
    total = sum(stats.values())

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write(json.dumps(
            {
                'items': items,
                'hierarchy': hierarchy,
            },
            default=json_encoder
        ))

    raise Exception()

    return tmp.name
