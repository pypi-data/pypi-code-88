from typing import Any, Dict, Optional, Sequence
from itertools import chain
from pxd_postgres.ltree import LtreeValue
from wcd_geo_db.modules.bank.db import Division, DivisionCode, DivisionTranslation
from wcd_geo_db.modules.code_seeker import CodeSeekerRegistry

from .code_seeker import get_code_seeker_registry
from .code_mapper import CodeMapper
from .dtos import DivisionItem, DivisionTranslationItem
from .merger import MergeCommiter, inject_synonyms


__all__ = (
    'find_by_codes',
    'make_merge_division_code',
    'merge_divisions',
    'merge_division_translations',
)


def get_item_codes(item: DivisionItem):
    return [item['code']] + (item.get('codes') or [])


def find_by_codes(registry: CodeSeekerRegistry, items: Sequence[DivisionItem]) -> CodeMapper:
    codes = [
        (code, value)
        for item in items
        for code, value in (get_item_codes(item) + (item.get('path') or []))
    ]

    return CodeMapper(
        registry,
        Division.objects.seek_codes(registry=registry, codes=codes)
    )


def make_merge_division_code(seeker, code: Any):
    return seeker.name, code


def merge_divisions(items: Sequence[DivisionItem], change_path: bool = True):
    d = MergeCommiter(Division, update_fields=(
        ('name', 'types', 'level', 'synonyms',)
        +
        (('parent_id', 'path') if change_path else ())
    ))
    # dc = MergeCommiter(DivisionCode, update_fields=('code', 'value'))

    divisions = find_by_codes(get_code_seeker_registry(), items)

    for item in items:
        eqs = divisions.get_one(get_item_codes(item))
        path = [divisions.get_one([code]) for code in item['path']]

        if None in path and (change_path or eqs is None):
            d.fail(item, code='path_failure', path=path)
            continue

        path = [x.id for x in path]
        code, code_value = item['code']
        parent_id = path[-1] if len(path) > 0 else None

        if eqs is None:
            d.create(Division(
                name = item['name'],
                codes = {code: [code_value]},
                types = item['types'],
                level = item['level'],
                path = LtreeValue(path),
                parent_id=parent_id,
            ))
        else:
            eqs.path = LtreeValue(path + [eqs.id])
            eqs.codes[code] = set(eqs.codes.get(code) or [])
            eqs.codes[code].add(code_value)
            eqs.codes[code] = list(eqs.codes[code])
            eqs.parent_id = parent_id
            eqs.level = item['level']
            eqs.types = list(set((eqs.types or []) + item['types']))

            inject_synonyms(eqs, item['name'])

            d.update(eqs)

    results = d.commit()
    Division.objects.all().update_roughly_invalid_tree()
    Division.objects.filter(pk__in=[x.pk for x in results]).update_relations_from_json()

    d.clear()


def merge_division_translations(
    language: str,
    items: Sequence[DivisionTranslationItem]
):
    creations = []
    updates = []
    merge_failures = []
    entities_founded = find_by_codes(get_code_seeker_registry(), items)
    items_founded = DivisionTranslation.objects.filter(
        language=language, entity_id__in=[
            founded.id
            for founded in
            (entities_founded.get_one(get_item_codes(item)) for item in items)
            if founded is not None
        ]
    )
    map_founded = {item.entity_id: item for item in items_founded}

    for item in items:
        entity = entities_founded.get_one(get_item_codes(item))

        if entity is None:
            merge_failures.append(('no_entity', item))
            continue

        existing = map_founded.get(entity.id)

        if existing is None:
            creations.append(DivisionTranslation(
                language=language,
                name=item['name'],
                synonyms=item.get('synonyms') or '',
                entity_id=entity.id
            ))
        else:
            inject_synonyms(existing, item['name'], item.get('synonyms') or '')
            updates.append(existing)

    print(merge_failures)

    DivisionTranslation.objects.bulk_create(creations)
    DivisionTranslation.objects.bulk_update(
        updates, fields=('synonyms',)
    )
