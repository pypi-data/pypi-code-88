# def generate_single_query_skeleton(input_query_sets, output_queries, grain, selects, group_by):
#     from camtono.derivatives.selects import extract_select_output
#     from camtono.derivatives.generate import generate_table_query
#     with_, union = generate_filters(input_query_sets=input_query_sets, grain=grain, selects=selects, group_by=group_by)
#     output_queries = generate_output_column_queries(output_queries=output_queries, selects=selects)
#     if union:
#         base_query = union
#     else:
#         base_query = list(output_queries.values())[0]['query_ast']
#     final_query = {
#         "with": with_,
#         'select': extract_select_output(select=selects['final']),
#         'from': [
#             dict(value=base_query, name='base'),
#             *[
#                 dict(
#                     join=dict(
#                         value=i['query_ast'], name='f{}'.format(idx)
#                     ),
#                     on={"eq": ["base.{}".format(grain), "f{idx}.{grain}".format(idx=idx, grain=grain)]}
#                 ) for idx, i in enumerate(output_queries.values())
#             ]
#         ],
#         'groupby': group_by.get('final')
#     }
#     table_name, query_body = generate_table_query(select=selects['final'], ast=final_query, table_prefix=None)
#     return [[query_body]]
#
#
# def generate_filters(input_query_sets, grain, selects, group_by):
#     with_ = []
#     union = []
#     for idx, query_set in enumerate(input_query_sets):
#         sub_ast = generate_filter(input_query_set=query_set, grain=grain, selects=selects, group_by=group_by)
#         table_name = 'w{}'.format(idx)
#         with_.append({"value": sub_ast, "name": table_name})
#         union.append(
#             {"select": [dict(name=i['name'], value='{table_name}.{name}'.format(table_name=table_name, name=i['name']))
#                         for i in
#                         selects['filter']],
#              "from": [dict(value=table_name, name=table_name)]})
#     if len(union) == 1:
#         union = table_name
#     return with_, union
#
#
# def generate_output_column_queries(output_queries, selects):
#     from camtono.derivatives.generate import generate_table_query
#     queries = dict()
#     for idx, query in enumerate(output_queries):
#         table_name, query_body = generate_table_query(
#             select=selects[query['feature_id']],
#             ast=query['ast'],
#             table_prefix=None)
#         queries[table_name] = query_body
#     return queries
#
#
# def generate_filter(input_query_set, grain, selects, group_by):
#     from camtono.derivatives.selects import extract_select_output
#
#     sub_ast = {"from": [], "select": extract_select_output(select=selects['filter']),
#                "groupby": group_by.get('filter')}
#     for query_idx, query in enumerate(input_query_set):
#         table_name = 't{query_index}'.format(query_index=query_idx)
#         from_ = dict(
#             value=query['ast'],
#             name=table_name
#         )
#         if sub_ast['from']:
#             sub_ast['from'].append(dict(join=from_, on=dict(
#                 eq=['t0.{grain}'.format(grain=grain), 't{idx}.{grain}'.format(idx=query_idx, grain=grain)])))
#         else:
#             sub_ast['from'].append(from_)
#     return sub_ast
