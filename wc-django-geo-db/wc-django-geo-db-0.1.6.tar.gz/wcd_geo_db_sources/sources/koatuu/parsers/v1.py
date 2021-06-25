import json
from functools import reduce
from typing import Dict, Set, TYPE_CHECKING, TextIO, TypedDict, List, Optional
from enum import Enum
import tempfile

from wcd_geo_db.const import DivisionLevel, DivisionType
from wcd_geo_db_sources.modules.merger.dtos import DivisionItem

from ..code_seeker import KOATUU_SEEKER

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


class Category(str, Enum):
    CITY = chr(1052)
    CITY_DISTRICT = chr(1056)
    TOWN = chr(1058)
    VILLAGE = chr(1057)
    HAMLET = chr(1065)


CATEGORY_TYPES = {
    None: {},
    Category.CITY: {DivisionType.LOCALITY, DivisionType.CITY},
    Category.CITY_DISTRICT: {DivisionType.CITY_DISTRICT},
    Category.TOWN: {DivisionType.LOCALITY, DivisionType.TOWN},
    Category.VILLAGE: {DivisionType.LOCALITY, DivisionType.VILLAGE},
    Category.HAMLET: {DivisionType.LOCALITY,DivisionType.HAMLET},
}
CATEGORY_ALIASES = {
    chr(67): Category.VILLAGE,
}
CATEGORY_LEVELS = {
    Category.CITY: DivisionLevel.LOCALITY,
    Category.CITY_DISTRICT: DivisionLevel.SUBLOCALITY_LEVEL_1,
    Category.TOWN: DivisionLevel.LOCALITY,
    Category.VILLAGE: DivisionLevel.LOCALITY,
    Category.HAMLET: DivisionLevel.LOCALITY,
}
LEVELS_TYPES = {
    DivisionLevel.ADMINISTRATIVE_LEVEL_1: {DivisionType.REGION},
    DivisionLevel.ADMINISTRATIVE_LEVEL_2: {DivisionType.DISTRICT, DivisionType.MUNICIPALITY},
    DivisionLevel.ADMINISTRATIVE_LEVEL_3: {DivisionType.COMMUNE, DivisionType.COMMUNITY},
    DivisionLevel.LOCALITY: {DivisionType.LOCALITY},
    DivisionLevel.SUBLOCALITY_LEVEL_1: {DivisionType.CITY_DISTRICT},
}
HIERARCHY_LEVELS = {
    1: DivisionLevel.ADMINISTRATIVE_LEVEL_1,
    2: DivisionLevel.ADMINISTRATIVE_LEVEL_2,
    3: DivisionLevel.ADMINISTRATIVE_LEVEL_3,
    4: DivisionLevel.LOCALITY,
}
CODE_TYPES = {
    # міста обласного значення
    (3, 1): {DivisionType.LOCALITY},
    # райони Автономної Республіки Крим, області
    (3, 2): {DivisionType.REGION},
    # райони міст, що мають спеціальний статус
    (3, 3): {DivisionType.CITY_DISTRICT},

    # міста районного значення
    (6, 1): {DivisionType.LOCALITY, DivisionType.CITY},
    # is unused
    (6, 2): set(),
    # райони в містах обласного значення
    (6, 3): {DivisionType.CITY_DISTRICT},
    # селища міського типу, що входять до складу міськради
    (6, 4): {DivisionType.LOCALITY, DivisionType.TOWN},
    # селища міського типу, що входять до складу райради
    (6, 5): {DivisionType.LOCALITY, DivisionType.TOWN},
    # селища міського типу, що входять до складу райради в місті
    (6, 6): {DivisionType.LOCALITY, DivisionType.TOWN},
    # міста, що входять до складу міськради
    (6, 7): {DivisionType.LOCALITY, DivisionType.CITY},
    # сільради, що входять до складу райради
    (6, 8): {DivisionType.COMMUNE},
    # сільради, села, що входять до складу райради міста, міськради
    (6, 9): {DivisionType.COMMUNE},
}
TYPE_LEVELS = {
    DivisionType.CITY: DivisionLevel.LOCALITY,
    DivisionType.REGION: DivisionLevel.ADMINISTRATIVE_LEVEL_1,
    DivisionType.CITY_DISTRICT: DivisionLevel.SUBLOCALITY_LEVEL_1,
    DivisionType.MUNICIPALITY: DivisionLevel.ADMINISTRATIVE_LEVEL_2,
    DivisionType.DISTRICT: DivisionLevel.ADMINISTRATIVE_LEVEL_2,
    DivisionType.COMMUNE: DivisionLevel.ADMINISTRATIVE_LEVEL_3,
    DivisionType.COMMUNITY: DivisionLevel.ADMINISTRATIVE_LEVEL_3,
    DivisionType.TOWN: DivisionLevel.LOCALITY,
    DivisionType.LOCALITY: DivisionLevel.LOCALITY,
    DivisionType.VILLAGE: DivisionLevel.LOCALITY,
    DivisionType.HAMLET: DivisionLevel.LOCALITY,
}


class Geo(DivisionItem):
    category: Optional[Category]


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

    for code_type in code_types(geo['code'][1]):
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
        hierarchy_level = HIERARCHY_LEVELS[len(geo['path']) + 1]

        type_levels = {
            TYPE_LEVELS[t]
            for t in geo['types']
            if t in TYPE_LEVELS
        }

        level = min((hierarchy_level, *type_levels))

    return level


def create_geo(raw: dict) -> Geo:
    path = [(KOATUU_SEEKER.name, code) for code in get_path(raw)]
    geo: Geo = Geo(
        code=path[-1],
        path=path[:-1],
        name=raw.get(Field.TITLE) or None,
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

        for code, item in (geo['path'] + [geo['code']]):
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
        item['code'][1]: index
        for index, item in enumerate(items)
    }
    for item in items:
        if item['level'] != DivisionLevel.LOCALITY:
            for code in hierarchy.get(item['code'][1], []):
                # Fixing all cities with city districts inside that are marked in some other way.
                if items[index_map[code]]['level'] in {
                    DivisionLevel.SUBLOCALITY_LEVEL_1,
                    DivisionLevel.SUBLOCALITY_LEVEL_2,
                    DivisionLevel.SUBLOCALITY_LEVEL_3,
                }:
                    item['category'] = Category.CITY
                    item['level'] = DivisionLevel.LOCALITY
                    safe_remove(item['types'], DivisionType.REGION)
                    safe_remove(item['types'], DivisionType.DISTRICT)
                    safe_remove(item['types'], DivisionType.MUNICIPALITY)
                    safe_remove(item['types'], DivisionType.COMMUNE)
                    safe_remove(item['types'], DivisionType.COMMUNITY)
                    item['types'].add(DivisionType.LOCALITY)
                    item['types'].add(DivisionType.CITY)

    return items


def parse(runner: 'KOATUUImportRunner', file: TextIO):
    data = json.loads(file.read())
    items = list(sorted(map(create_geo, data), key=order_key))
    hierarchy = collect_hierarchy(items)
    items = postprocess_items(items, hierarchy)

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write(json.dumps(
            items,
            default=json_encoder
        ))

    return tmp.name
