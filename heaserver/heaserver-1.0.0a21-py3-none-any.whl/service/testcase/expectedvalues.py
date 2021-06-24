"""
Functions for automatically generating expected values for unit and integration tests of HEA services.
"""
import copy
import logging
from typing import Dict, Any, List, Optional
from heaserver.service import wstl
from yarl import URL
from dataclasses import dataclass
import uritemplate


@dataclass
class ActionSpec:
    name: str
    rel: Optional[List[str]] = None
    url: Optional[str] = None


def body_post(fixtures: Dict[str, List[Dict[str, Any]]], coll: str) -> Dict[str, Dict[str, Any]]:
    """
    Create a Collection+JSON template from a data test fixture.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :return: a Collection+JSON template as a dict using the first object in the given mongodb collection. Replaces the
    object's name and display_name attribute values with 'tritimus' and 'Tritimus', respectively.
    """
    return {'template': {'data': [{'name': x, 'value': y} for x, y in {
        **fixtures[coll][0],
        **{'name': 'tritimus', 'display_name': 'Tritimus'}}.items() if x != 'id']}}


def body_put(fixtures: Dict[str, List[Dict[str, Any]]], coll: str) -> Dict[str, Dict[str, Any]]:
    """
    Create a Collection+JSON template from a data test fixture.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :return: a Collection+JSON template as a dict using the first object in the given mongodb collection. Replaces the
    object's description attribute value with 'A description'.
    """
    data = []
    for x, y in {**fixtures[coll][1], **{'description': 'A description'}}.items():
        if isinstance(y, dict):
            for xprime, yprime in y.items():
                data.append({'name': xprime, 'value': yprime, 'section': x})
        else:
            data.append({'name': x, 'value': y})

    return {'template': {'data': data}}


def expected_one_wstl(fixtures: Dict[str, List[Dict[str, Any]]],
                      coll: str,
                      wstl_builder: wstl.RuntimeWeSTLDocumentBuilder,
                      include_root=False,
                      get_actions: Optional[List[ActionSpec]] = None) -> List[Dict[str, Any]]:
    """
    Create a run-time WeSTL document from a data test fixture. The document will contain the first HEAObject dict in
    the given collection, and will contain a single action.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :param wstl_builder: a runtime WeSTL document builder object. Required.
    :param open_action_name: the name of the service's document open action. Required.
    :param open_action_rel: list of rel strings. Optional.
    :param include_root: whether to use absolute URLs or just paths.
    :return: a run-time WeSTL document as a dict.
    """
    if get_actions is None:
        get_actions = []
    actions = []
    href_ = wstl_builder.href if wstl_builder.href else ''
    for action, action_name, action_rel, action_url in ((wstl_builder.find_action(a.name), a.name, a.rel, a.url) for a
                                                        in get_actions):
        if action is None:
            raise ValueError(f'Action {action_name} does not exist')
        action = {**action,
                  'href': action_url if action_url else (
                      f'{URL(href_) / ""}{{id}}' if include_root else f'{(URL(href_) / "").path}{{id}}'),
                  'rel': action_rel if action_rel else []}
        actions.append(action)
    return [{
        'wstl': {
            'data': [fixtures[coll][0]],
            'hci': {'href': str(URL(href_) / fixtures[coll][0]['id'])},
            'actions': actions,
            'title': 'Registry components'}}]


def expected_one(fixtures: Dict[str, List[Dict[str, Any]]], coll: str, wstl_builder: wstl.RuntimeWeSTLDocumentBuilder,
                 include_root=False,
                 get_actions: Optional[List[ActionSpec]] = None) -> List[Dict[str, Any]]:
    """
    Create a Collection+JSON document with the first HEAObject from a mongodb collection in the given data test fixture.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :param include_root: whether to use absolute URLs or just paths.
    :return: a list containing Collection+JSON template as a dict using the first object in the given mongodb collection.
    Replaces the object's description attribute value with 'A description'.
    """
    id_ = fixtures[coll][0]['id']
    href = URL(wstl_builder.href if wstl_builder.href else '') / id_
    get_actions_ = get_actions or []

    def item_links() -> List[Dict[str, Any]]:
        links = []
        for action, action_name, rel, url in ((wstl_builder.find_action(a.name), a.name, a.rel or [], a.url) for a in
                                              get_actions_):
            if action is None:
                raise ValueError(f'Invalid action name {action_name}')
            targets = action.get('target', '').split()
            if 'item' in targets and 'read' in targets and 'cj' in targets:
                links.append({
                    'prompt': action['prompt'],
                    'href': uritemplate.expand(url, {'id': id_}) if url else str(href),
                    'rel': ' '.join(rel)
                })
        return links

    def item_link() -> Dict[str, Any]:
        for action, action_name, rel, url in ((wstl_builder.find_action(a.name), a.name, a.rel or [], a.url) for a in
                                              get_actions_):
            if action is None:
                raise ValueError(f'Invalid action name {action_name}')
            targets = action.get('target', '').split()
            if 'item' in targets and 'href' in targets and 'cj' in targets:
                return {
                    'prompt': action['prompt'],
                    'href': uritemplate.expand(url, {'id': id_}) if url else (
                        str(href) if include_root else str(href.path)),
                    'rel': ' '.join(rel),
                    'readOnly': 'true'
                }
        return {}

    def top_level_links() -> List[Dict[str, Any]]:
        links = []
        for action, action_name, rel, url in ((wstl_builder.find_action(a.name), a.name, a.rel or [], a.url) for a in
                                              get_actions_):
            if action is None:
                raise ValueError(f'Invalid action name {action_name} in get_actions')
            targets = action.get('target', '').split()
            if action['type'] == 'safe' and 'app' in targets and 'cj' in targets and (
                    'inputs' not in action or not action['inputs']):
                links.append({
                    'prompt': action['prompt'],
                    'href': uritemplate.expand(url, {'id': id_}) if url else (
                        str(href) if include_root else str(href.path)),
                    'rel': ' '.join(rel)
                })
        return links

    def queries() -> List[Dict[str, Any]]:
        queries = []
        for action, action_name, rel in ((wstl_builder.find_action(a.name), a.name, a.rel) for a in get_actions_):
            if action is None:
                raise ValueError(f'Invalid action name {action_name} in get_actions')
            targets = action.get('target', '').split()
            if 'inputs' in action and action['type'] == 'safe' and 'list' in targets and 'cj' in targets:
                q = {'rel': ' '.join(action['rel']),
                     'href': action['href'],
                     'prompt': action.get('prompt', ''),
                     'data': []}
                inputs_ = action['inputs']
                for i in range(len(inputs_)):
                    d = inputs_[i]
                    nm = d.get('name', 'input' + str(i))
                    q['data'].append({
                        'name': nm,
                        'value': d.get('value', None),
                        'prompt': d.get('prompt', nm),
                        'required': d.get('required', False),
                        'readOnly': d.get('readOnly', False),
                        'pattern': d.get('pattern', '')
                    })
                queries.append(q)
        return queries

    item_link_ = item_link()

    data_ = []
    for x, y in fixtures[coll][0].items():
        if x != 'type':
            if isinstance(y, dict):
                for xprime, yprime in y.items():
                    if xprime != 'type':
                        data_.append({
                            'display': False if xprime == 'id' else True,
                            'name': xprime,
                            'prompt': xprime,
                            'value': yprime,
                            'section': x
                        })
            else:
                data_.append({
                    'display': False if x == 'id' else True,
                    'name': x,
                    'prompt': x,
                    'value': y
                })
    collection = {
        'collection': {
            'href': str(href),
            'items': [{'data': data_,
                'links': item_links()}],
            'version': '1.0'}}
    if item_link_:
        if 'rel' in item_link_:
            collection['collection']['items'][0]['rel'] = item_link_['rel']
        collection['collection']['items'][0]['href'] = item_link_['href']
    top_level_links_ = top_level_links()
    if top_level_links_:
        collection['collection']['links'] = top_level_links_
    queries_ = queries()
    if queries_:
        collection['collection']['queries'] = queries_
    for action, action_name, rel in ((wstl_builder.find_action(a.name), a.name, a.rel) for a in get_actions):
        if action is None:
            raise ValueError(f'Invalid action name in get_all_actions {action_name}')
        targets = action['target'].split()
        if 'cj-template' in targets:
            template = {'data': [{'name': i['name'],
                                  'value': i['value'] if 'add' in targets else (
                                      fixtures[coll][0].get(i['name'], None) if i['name'] not in ('meta', 'type') else None),
                                  'prompt': i.get('prompt', ''),
                                  'required': i.get('required', False),
                                  'pattern': i.get('pattern', ''),
                                  'readOnly': i.get('readOnly', False)
                                  } for i in action['inputs']],
                        'prompt': action.get('prompt', action['name']),
                        'rel': ' '.join(rel) if rel is not None else ''}
            collection['collection']['template'] = template
    return [collection]


def expected_one_duplicate_form(fixtures: Dict[str, List[Dict[str, Any]]],
                                coll: str,
                                wstl_builder: wstl.RuntimeWeSTLDocumentBuilder,
                                duplicate_action_name: str,
                                duplicate_action_rel: Optional[List[str]] = None,
                                include_root=False) -> List[Dict[str, Any]]:
    """
    Create a Collection+JSON document with the first HEAObject from the given mongodb collection in the given data test
    fixture. The returned Collection+JSON document will contain the HEAObject in the data section and a template
    for duplicating the HEAObject.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :param wstl_builder: a runtime WeSTL document builder object. Required.
    :param duplicate_action_name: the name of the service's duplicator action. Required.
    :param duplicate_action_rel: list of rel strings for the action. Optional.
    :param include_root: whether to use absolute URLs or just paths.
    :return: a list of Collection+JSON templates as dicts.
    """
    return _expected_one_form(fixtures, coll, wstl_builder, duplicate_action_name,
                              duplicate_action_rel, include_root, '/duplicator')


def _expected_one_form(fixtures: Dict[str, List[Dict[str, Any]]],
                       coll: str,
                       wstl_builder: wstl.RuntimeWeSTLDocumentBuilder,
                       action_name: str,
                       action_rel: Optional[List[str]] = None,
                       include_root: bool = False,
                       suffix: str = None) -> List[Dict[str, Any]]:
    """
    Create a Collection+JSON document with the first HEAObject from the given mongodb collection in the given data test
    fixture. The returned Collection+JSON document will contain the HEAObject in the data section and a template
    containing that HEAObject's values.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :param wstl_builder: a runtime WeSTL document builder object. Required.
    :param action_name: the name of the action that causes creation of the template. Required.
    :param action_rel: list of rel strings for the action. Optional.
    :param include_root: whether to use absolute URLs or just paths.
    :return: a list of Collection+JSON templates as dicts.
    """
    action = wstl_builder.find_action(action_name)
    if action is None:
        raise ValueError(f'Action {action_name} does not exist')
    id_ = fixtures[coll][0]['id']
    href = URL(wstl_builder.href if wstl_builder.href else '') / (id_ + (suffix if suffix else ''))
    data_ = []
    for x, y in fixtures[coll][0].items():
        if x != 'type':
            if isinstance(y, dict):
                for xprime, yprime in y.items():
                    if xprime != 'type':
                        data_.append({
                            'display': False if xprime == 'id' else True,
                            'name': xprime,
                            'prompt': xprime,
                            'value': yprime,
                            'section': x
                        })
            else:
                data_.append({
                    'display': False if x == 'id' else True,
                    'name': x,
                    'prompt': x,
                    'value': y
                })
    return [{
        'collection': {
            'version': '1.0',
            'href': str(href) if include_root else str(href.path),
            'items': [
                {
                    'data': data_,
                    'links': []}],
            'template': {
                'prompt': action.get('prompt', None),
                'rel': ' '.join(action_rel if action_rel else []),
                'data': [
                    {'name': d['name'],
                     'pattern': d.get('pattern', ''),
                     'prompt': d.get('prompt', None),
                     'readOnly': d.get('readOnly', False),
                     'required': d.get('required', False),
                     'value': fixtures[coll][0].get(d['name'], None)} for d in action['inputs']
                ]}
        }}]


def expected_all_wstl(fixtures: Dict[str, List[Dict[str, Any]]],
                      coll: str,
                      wstl_builder: wstl.RuntimeWeSTLDocumentBuilder,
                      include_root: bool = False,
                      get_all_actions: Optional[List[ActionSpec]] = None) -> List[Dict[str, Any]]:
    """
    Create a run-time WeSTL document from a data test fixture. The document will contain all HEAObject dicts in
    the given collection, and it will contain a single action.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :param wstl_builder: a runtime WeSTL document builder object. Required.
    :param include_root: whether to use absolute URLs or just paths.
    :return: a run-time WeSTL document as a dict.
    """
    if get_all_actions is None:
        get_all_actions = []

    href_ = wstl_builder.href if wstl_builder.href else ''

    def runtime_actions():
        result = []
        for action, action_name, action_rel, action_url in ((wstl_builder.find_action(a.name), a.name, a.rel, a.url) for
                                                            a in get_all_actions):
            if action is None:
                raise ValueError(f'Action {action_name} does not exist')
            targets = action.get('target', '').split()
            if ('href' in targets and 'cj' in targets) or 'cj-template' in targets:
                if 'item' in targets:
                    href = action_url if action_url else (
                        str(URL(href_) / '') + '{id}' if include_root else
                            (URL(href_) / '').path + '{id}')
                else:
                    href = action_url if action_url else (
                        str(URL(href_) / '') if include_root else (URL(href_) / '').path)
                action['href'] = href
            action['rel'] = action_rel if action_rel else []
            result.append(action)
        return result

    return [{
        'wstl': {
            'data': fixtures[coll],
            'actions': runtime_actions(),
            'title': wstl_builder.design_time_document['wstl']['title'],
            'hci': {'href': href_ if href_ else '#'}
        }
    }]


def expected_all(fixtures: Dict[str, List[Dict[str, Any]]], coll: str, wstl_builder: wstl.RuntimeWeSTLDocumentBuilder,
                 include_root=False, get_all_actions: Optional[List[ActionSpec]] = None) -> List[Dict[str, Any]]:
    """
    Create a list of Collection+JSON documents with all HEAObjects from a mongodb collection in the given data test fixture.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :param wstl_builder: a runtime WeSTL document builder object. Required.
    :param include_root: whether to use absolute URLs or just paths.
    :return: a list of Collection+JSON dicts.
    """
    if get_all_actions is None:
        get_all_actions = []

    href_ = wstl_builder.href if wstl_builder.href else ''

    def item_links(id_):
        links = []
        for action, rel, url in ((wstl_builder.find_action(a.name), a.rel or [], a.url) for a in get_all_actions):
            targets = action.get('target', '').split()
            if 'item' in targets and 'read' in targets and 'cj' in targets:
                links.append({
                    'prompt': action['prompt'],
                    'href': uritemplate.expand(url, {'id': id_}) if url else (
                        str(URL(href_) / id_) if include_root else str((URL(href_) / id_).path)),
                    'rel': ' '.join(rel)
                })
        return links

    def item_link(id_):
        for action, rel, url in ((wstl_builder.find_action(a.name), a.rel or [], a.url) for a in get_all_actions):
            targets = action.get('target', '').split()
            if 'item' in targets and 'href' in targets and 'cj' in targets:
                return {
                    'prompt': action['prompt'],
                    'href': uritemplate.expand(url, {'id': id_}) if url else (
                        str(URL(href_) / id_) if include_root else str((URL(href_) / id_).path)),
                    'rel': ' '.join(rel),
                    'readOnly': 'true'
                }
        return {}

    def top_level_links():
        links = []
        for action, rel, url in ((wstl_builder.find_action(a.name), a.rel or [], a.url) for a in get_all_actions):
            targets = action.get('target', '').split()
            if action['type'] == 'safe' and 'app' in targets and 'cj' in targets and (
                    'inputs' not in action or not action['inputs']):
                links.append({
                    'prompt': action['prompt'],
                    'href': url if url else (
                        str(URL(href_) / '') if include_root else str((URL(href_) / '').path)),
                    'rel': ' '.join(rel)
                })
        return links

    items = []
    for f in fixtures[coll]:
        data_ = []
        id_ = f['id']
        item_link_ = item_link(id_)
        for x, y in f.items():
            if x != 'type':
                if isinstance(y, dict):
                    for xprime, yprime in y.items():
                        if xprime != 'type':
                            data_.append({
                                'display': False if xprime == 'id' else True,
                                'name': xprime,
                                'prompt': xprime,
                                'value': yprime,
                                'section': x
                            })
                else:
                    data_.append({
                        'display': False if x == 'id' else True,
                        'name': x,
                        'prompt': x,
                        'value': y
                    })
        item = {'data': data_,
        'links': item_links(id_)}
        if item_link_:
            if 'rel' in item_link_:
                item['rel'] = item_link_['rel']
            item['href'] = item_link_['href']
        items.append(item)

    collection_doc = {'collection': {'href': str(wstl_builder.href if wstl_builder.href else '#'),
                                     'items': items,
                                     'version': '1.0'}}
    for action, action_name, rel in ((wstl_builder.find_action(a.name), a.name, a.rel) for a in get_all_actions):
        if action is None:
            raise ValueError(f'Invalid action name in get_all_actions {action_name}')
        targets = action['target'].split()
        if 'cj-template' in targets:
            template = {'data': [{'name': i['name'],
                                  'value': i['value'] if 'add' in targets else (f.get(i['name'], None) if i['name'] not in ('meta', 'type') and len(fixtures[coll]) == 1 else None),
                                  'prompt': i.get('prompt', ''),
                                  'required': i.get('required', False),
                                  'pattern': i.get('pattern', ''),
                                  'readOnly': i.get('readOnly', False)
                                  } for i in action['inputs']],
                        'prompt': action.get('prompt', action['name']),
                        'rel': ' '.join(rel) if rel else ''}
            collection_doc['collection']['template'] = template
    top_level_links_ = top_level_links()
    if top_level_links_:
        collection_doc['collection']['links'] = top_level_links_
    return [collection_doc]


def expected_values(fixtures: Dict[str, List[Dict[str, Any]]],
                    coll: str,
                    wstl_builder: wstl.RuntimeWeSTLDocumentBuilder,
                    duplicate_action_name: str,
                    resource_path: str = None,
                    include_root=False,
                    get_actions: Optional[List[ActionSpec]] = None,
                    get_all_actions: Optional[List[ActionSpec]] = None) -> Dict[str, Any]:
    """
    Generate a dict of all of the expected values for passing into the mongotestcase and mockmongotestcase
    get_test_case_cls function.

    :param fixtures: mongodb collection name -> list of HEAObject dicts. Required.
    :param coll: the mongodb collection name to use. Required.
    :param wstl_builder: a runtime WeSTL document builder object. Required.
    :param open_action_name: the name of the service's open action. Required.
    :param duplicate_action_name: the name of the service's duplicator action. Required.
    :param resource_path: the resource path. Optional. If None, then /{coll} is used as the resource_path.
    :param include_root: whether to use absolute URLs or just paths.
    :return: a dict of keyword argument name -> Collection+JSON dict or WeSTL document dict, where the keyword arguments
    match those of the mongotestcase and mockmongotestcase get_test_case_cls functions.
    """
    wstl_builder_ = copy.deepcopy(wstl_builder)
    wstl_builder_.href = _href(resource_path if resource_path else f'/{coll}/')
    return {
        'body_post': body_post(fixtures, coll),
        'body_put': body_put(fixtures, coll),
        'expected_one_wstl': expected_one_wstl(fixtures, coll, wstl_builder_, get_actions=get_actions,
                                               include_root=include_root),
        'expected_one': expected_one(fixtures, coll, wstl_builder_,
                                     include_root=include_root, get_actions=get_actions),
        'expected_one_duplicate_form': expected_one_duplicate_form(fixtures, coll, wstl_builder_,
                                                                   duplicate_action_name,
                                                                   include_root=include_root),
        'expected_all_wstl': expected_all_wstl(fixtures, coll, wstl_builder_, get_all_actions=get_all_actions,
                                               include_root=include_root),
        'expected_all': expected_all(fixtures, coll, wstl_builder_,
                                     include_root=include_root, get_all_actions=get_all_actions)
    }


def _href(resource_path: str, id_=None) -> URL:
    url = URL('http://localhost:8080').with_path(resource_path)
    return url / id_ if id_ else url
