def generate_derivative(definition: dict, feature_map: dict, desired_dialect, single_query: bool = False,
                        new_table_prefix: str = None):
    """Create a derived query ast based on a definition and map of all used features

    :param definition: camtono derivative definition
    :param feature_map: dictionary of feature_id: feature details that are referenced in the defintion
    :param single_query: generate a single query_ast or an ordered list of arrays that
    :param new_table_prefix: string used when referencing new tables in multiple
    :return:
    """
    from camtono.derivatives.inputs import flatten_inputs, generate_input_query_sets
    from camtono.derivatives.generate import generate_multi_query_skeleton
    from camtono.derivatives.selects import generate_select_mapping
    from camtono.derivatives.outputs import generate_output_queries

    inputs, default_inputs, feature_inputs = standardize_input_attributes(definition=definition)
    flattened_inputs = flatten_inputs(inputs=inputs)
    input_query_sets, input_features = generate_input_query_sets(
        flattened_inputs=flattened_inputs, features=feature_map,
        default_inputs=default_inputs, feature_inputs=feature_inputs
    )
    definition_outputs = definition.get('outputs', definition.get('output'))
    if not definition_outputs:
        definition_outputs = [dict(column_name=definition['grain'])]
    output_queries = generate_output_queries(definition_outputs=definition_outputs, default_inputs=default_inputs,
                                             feature_map=feature_map, input_features=input_features,
                                             feature_inputs=feature_inputs)
    selects, group_by = generate_select_mapping(
        input_features=input_features,
        default_inputs=default_inputs,
        definition_outputs=definition_outputs,
        input_query_sets=input_query_sets,
        feature_map=feature_map,
        grain=definition['grain'],
        output_queries=output_queries,definition_groupings=definition.get('group_by',[])
    )
    queries = generate_multi_query_skeleton(
        input_query_sets=input_query_sets, grain=definition['grain'],
        output_queries=output_queries, selects=selects,
        table_prefix=new_table_prefix, group_by=group_by, dialect_name=desired_dialect
    )
    return queries


def standardize_input_attributes(definition):
    inputs = definition['filters'] if 'filters' in definition.keys() else definition.get('inputs', dict())
    default_inputs = dict()
    if 'default_filters' in definition.keys():
        default_inputs = {i['attribute']: i['value'] for i in definition.get('default_filters', [])}
    elif 'default_inputs' in definition.keys():
        default_inputs = {i['attribute']: i['value'] for i in definition.get('default_inputs', [])}
    if 'grain' not in default_inputs.keys():
        default_inputs['grain'] = definition['grain']
    feature_inputs = {i['feature_id']: i.get('inputs', i.get('input', {})) for i in definition['features']}
    return inputs, default_inputs, feature_inputs
