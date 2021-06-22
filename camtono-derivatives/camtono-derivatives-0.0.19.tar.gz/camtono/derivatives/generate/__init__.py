from .multi_query import generate_multi_query_skeleton
# from .single_query import generate_single_query_skeleton


def generate_table_name(data, prefix=None):
    import json
    import uuid
    import hashlib
    if prefix is None:
        prefix = ""
    hash_id =hashlib.md5(
            str(json.dumps(data, sort_keys=True)).encode('utf-8')
        ).hexdigest()
    return prefix + str(hash_id)


def generate_table_query(select, ast, table_prefix, dialect_name):
    from camtono.derivatives.selects import extract_select_schema
    from camtono.parser.clean import prune_ast
    ast = prune_ast(json=ast)
    if table_prefix is None:
        table_prefix = 'camtono_'
    table_name = generate_table_name(data=ast, prefix=table_prefix)
    body = dict(query_ast=ast, table_name=table_name,
                schema=extract_select_schema(select=select, dialect_name=dialect_name))
    return table_name, body
