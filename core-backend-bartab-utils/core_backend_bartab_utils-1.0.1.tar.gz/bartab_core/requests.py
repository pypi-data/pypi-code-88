def get_pk_from_url(request) -> str:
    return request.resolver_match.kwargs.get('pk')


def get_named_id_from_url(request, name: str, allow_pk: bool = False) -> str:
    value = request.resolver_match.kwargs.get(name)

    if value != None:
        return value

    id_posfix = '_id'
    if len(name) < len(id_posfix) or name[len(name) - len(id_posfix):] != id_posfix:
        name = f'{name}{id_posfix}'
        value = request.resolver_match.kwargs.get(name)

    if value != None or (value == None and not allow_pk):
        return value

    return request.resolver_match.kwargs.get('pk')


def get_id_from_obj(obj) -> str:
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, dict):
        if 'uuid' in obj:
            return obj['uuid']
        elif 'pk' in obj:
            return obj['pk']

    try:
        return obj.uuid
    except:
        return None
