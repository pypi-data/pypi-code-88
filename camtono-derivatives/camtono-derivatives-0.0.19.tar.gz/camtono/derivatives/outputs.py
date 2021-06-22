def generate_output_queries(definition_outputs, default_inputs, feature_map, input_features, feature_inputs):
    from camtono.derivatives.inputs import trim_feature_input
    output_queries = []
    column_features = set([i['feature_id'] for i in definition_outputs if 'feature_id' in i.keys()])
    output_features = {k: v for k, v in feature_map.items() if k not in input_features.keys() or k in column_features}
    for feature_id, feature in output_features.items():
        ast = trim_feature_input(
            feature=feature, set_inputs=dict(),
            default_inputs=default_inputs, feature_input=feature_inputs[feature_id]
        )
        # feature_id to ast map
        output_queries.append({"feature_id": feature_id, "ast": ast})
    return output_queries
