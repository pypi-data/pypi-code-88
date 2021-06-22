def generate_input_query_sets(flattened_inputs, features, default_inputs: dict, feature_inputs: dict):
    """

    :param flattened_filters:
    :param features:
    :return:
    """
    query_sets, input_features = [], dict()
    for idx, input_set in enumerate(flattened_inputs):
        set_features, skip = define_set_features(input_set=input_set)
        input_features.update(set_features)
        query_set = []
        for feature, filters in set_features.items():
            ast = trim_feature_input(
                feature=features[feature], set_inputs=set_features[feature],
                default_inputs=default_inputs, feature_input=feature_inputs.get(feature, dict())
            )
            # feature_id to ast map
            query_set.append({"feature_id": feature, "ast": ast})
        if not skip:
            query_sets.append(query_set)
    return query_sets, input_features


def flatten_inputs(inputs: dict) -> tuple:
    """

    :param inputs:
    :return:
    """
    list_string = 'inputs'
    if 'filters' in inputs.keys():
        list_string = 'filters'
    flattened_filters = flatten_input(inputs=inputs, list_string=list_string)
    return flattened_filters


def flatten_input(inputs, list_string='filters', operator_string='item'):
    """Flattens nested pyparser syntax into a single layer

    :param inputs:
    :param list_string:
    :param operator_string: string key of the pyparser operator
    :return: flatted list of lists of base operators
    """
    flattened_inputs = list()
    if operator_string in inputs.keys() and list_string in inputs.keys():
        operator = inputs[operator_string].lower()
        for idx, i in enumerate(inputs[list_string]):
            new_inputs = i
            if isinstance(i.get(list_string), list):
                new_inputs = flatten_input(inputs=i, list_string=list_string, operator_string=operator_string)
            if len(new_inputs) > 0:
                flattened_inputs = unify_sets(existing=flattened_inputs, new=new_inputs, operator=operator)
    return flattened_inputs


def unify_sets(existing, new, operator):
    """Join two sets of statements based on boolean operator

    :param existing: List of existing statements
    :param new: New statements to add to the set
    :param operator: boolean operator and, or, not
    :return: combined set of sets based on boolean operation
    """
    import itertools
    unified = []
    if isinstance(new, dict):
        new = [new]
    if not isinstance(new[0], list):
        new = [new]
    if not existing and operator in ['and', 'or']:
        unified = new
    elif operator == 'or':
        unified = existing + new
    elif operator == 'and':
        if existing:
            for a, b in itertools.product(existing, new):
                unified.append([*a, *b])
        else:
            unified.append(new)
    elif operator == 'not':
        for s in new:
            subset = []
            for x in s:
                x['not'] = bool(-x.get('not', False))
                subset = unify_sets(existing=subset, new=x, operator='or')
            unified = unify_sets(existing=unified, new=subset, operator='and')
    return unified


def define_set_features(input_set):
    """Processes flattened filter groups into a set of features

    :param filter_set: flattened list of filters
    :return: tuple of a dict of features and attributes and a flag to skip this particular filter group
    """
    features = dict()
    skip = False
    for f in input_set:
        if skip:
            continue
        if f['feature_id'] not in features.keys():
            features[f['feature_id']] = dict()
        if f['attribute'] not in features[f['feature_id']].keys():
            features[f['feature_id']][f['attribute']] = {'not': f.get('not', False), 'value': f['value']}
    return features, skip


def trim_feature_input(feature: dict, set_inputs: dict, default_inputs: dict, feature_input:dict):
    """Remove all unnecessary query input from the query_ast

    :param feature: feature dict
    :param set_inputs: dict of variables used for string formatting
    :param default_inputs:
    :param feature_input:
    :return: feature dict with cleaned query_ast
    """
    from copy import deepcopy
    ast = deepcopy(feature['query_ast'])

    for query_input in feature['inputs']:
        if all(query_input['name'] not in i.keys() for i in
               [set_inputs, default_inputs, feature_input]) and not query_input.get('default_value'):
            v = None
        elif query_input['name'] in set_inputs:
            v = set_inputs[query_input['name']]['value']
        elif query_input['name'] in feature_input:
            v = feature_input[query_input['name']]
        elif query_input.get('default_value'):
            v = query_input['default_value']
        else:
            v = default_inputs[query_input['name']]
        ast = update_feature_input(ast=ast, v=v, query_input=query_input)
    return ast


def update_feature_input(ast, v, query_input):
    new_val = v
    if query_input['is_literal']:
        if isinstance(v, str):
            new_val = {'literal': v}
        elif isinstance(v, list):
            new_val = [{'literal': i} for i in v]
    for i in query_input['locations']:
        if not query_input['is_literal'] and v is not None:
            val = get_tree_value(json=ast, locations=i['location']).replace("'{", '{').replace("}'", "}")
            new_val = val.replace('{' + query_input['name'] + '}', v)
        ast = set_tree_value(
            json=ast, locations=i['location'],
            val=new_val, target_index=i['level'] - 1 if i['is_wrapped_literal'] else i['level']
        )
    return ast


def set_value(val, **kwargs):
    """ Convenience function to set value for set_tree_value

    :param val: value to return
    :param kwargs: all other values
    :return: the value provided
    """
    return val


def get_tree_value(json, locations):
    if locations and (isinstance(json, dict) or isinstance(json, list)):
        for k, v in locations.items():
            if k.isdigit():
                k = int(k)
            v = get_tree_value(json=json[k], locations=v)
            return v
    else:
        return json


def set_tree_value(json, locations, target_index, current_index=0, replace_func=set_value, val=None):
    """ Set the

    :param json: dictionary
    :param locations: dictionary of the paths containing the location of a target value
    :param replace_func: function to apply when setting value receives val and json
    :param val: value to set
    :param target_index: location from the start of the tree where the replacement function should be applied
    :param current_index: current location in the tree
    :return: dictionary with the newly assigned values.
    """
    if locations and current_index < target_index and (isinstance(json, dict) or isinstance(json, list)):
        for k, v in locations.items():
            if k.isdigit():
                k = int(k)
            v = set_tree_value(json=json[k], locations=v, val=val, replace_func=replace_func,
                               target_index=target_index, current_index=current_index + 1)
            json[k] = v
        return json
    elif current_index == target_index:
        return val
    else:
        raise Exception("Invalid Location / Index")


def replace_string(json, old, new, **kwargs):
    return json.replace(old, new)
