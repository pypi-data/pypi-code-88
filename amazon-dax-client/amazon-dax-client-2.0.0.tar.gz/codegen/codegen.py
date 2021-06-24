#!/usr/bin/env python3

import sys
import json

from collections import namedtuple

from pathlib import Path

import jinja2

from jinja2 import contextfilter

ArgInfo = namedtuple('ArgInfo', 'name type')
ResponseField = namedtuple('ResponseField', 'name type')

def list_strformat_filter(objlist, fmt, objname='_'):
    return [fmt.format(**{objname: obj}) for obj in objlist]

@contextfilter
def call_macro_by_name(context, macro_name, *args, **kwargs):
    return context.vars[macro_name](*args, **kwargs)

class Shape:
    CustomShapeHandlers = {'ProjectionExpression', 'FilterExpression'}

    def __init__(self, name, shape_type, values=None):
        self.name = name
        self.type = shape_type
        self.values = sorted(values) if values else None

    @property
    def should_generate(self):
        return self.name not in Shape.CustomShapeHandlers

    @property
    def is_enum(self):
        return self.type == 'enum'

class Param:
    V1Params = {
            'AttributesToGet', 'AttributeUpdates', 'ConditionalOperator', 'Expected', 
            'ScanFilter', 'KeyConditions', 'QueryFilter'}

    ExpressionParams = {
            'ProjectionExpression', 'FilterExpression', 'ConditionalExpression',
            'UpdateExpression', 'KeyConditionExpression',
            'ExpressionAttributeNames', 'ExpressionAttributeValues'}

    def __init__(self, name, typeName, customEncoding, nullable):
        self.name = name
        self.type = typeName
        self.use_custom_encoding = customEncoding
        self.nullable = nullable

    @property
    def is_table_name(self):
        return self.name == 'tableName'

    @property
    def is_key(self):
        return self.name == 'key' or self.name == 'cborKey'

    @property
    def is_values(self):
        return self.name == 'cborValue'

    @property
    def is_kwargs(self):
        return self.name == 'kwargs'

    @property
    def is_keycond_expr(self):
        return self.name == 'keyConditionExpression'

    def __repr__(self):
        return "Param({}, {}, customEncoding={}, nullable={})".format(
                self.name,
                self.type,
                self.use_custom_encoding,
                self.nullable)

    def __str__(self):
        return "{}: {}{}{}".format(
                self.name,
                self.type,
                '?' if self.nullable else '',
                '*' if self.use_custom_encoding else '')

class Operation:
    def __init__(self, name, service_id, method_id, parameters, optional_args,
                 internalMethod, asynchronous, authMethod, customResponse,
                 responseFields, hasKey, customPrepare):
        self.name = name
        self.service_id = service_id
        self.method_id = method_id
        self.pretty_method_id = self.method_id.replace('-', 'N')
        self.is_asynchronous = asynchronous
        self.is_auth_method = authMethod
        self.is_internal = internalMethod

        self.parameters = parameters
        for p in self.parameters:
            p.op = self

        self.optional_args = optional_args
        self.optional_nonexpr_args = [a for a in optional_args if a.name not in Param.ExpressionParams]
        self._optional_expr_args = [a for a in optional_args if a.name in Param.ExpressionParams]
        self.has_custom_response = customResponse or internalMethod
        self.has_custom_prepare = customPrepare
        self.response_fields = responseFields
        self._has_key = hasKey

    @property
    def has_key(self):
        return self._has_key or any(p.is_key for p in self.parameters)

    @property
    def has_values(self):
        return any(p.is_values for p in self.parameters)

    @property
    def key_param(self):
        return 'Key' if self.name != 'putItem' else 'Item'

    @property
    def returns_attribute_values(self):
        return any(rf.name in ('Item', 'Items', 'Attributes') for rf in self.response_fields)

    @property
    def has_expression(self):
        return bool(self._optional_expr_args)

    @property
    def has_keycond_expression(self):
        return any(p.is_keycond_expr for p in self.parameters)

class Remote:
    def __init__(self, operations):
        self.operations = operations

def build_parameters(parameters):
    def _build():
        for paramName, paramInfo in parameters.items():
            yield Param(paramName,
                    paramInfo['typeName'],
                    paramInfo.get('customEncoding', False),
                    paramInfo.get('nullable', False))

    return list(_build())

def find_optional_args(methodInfo, ddbModel):
    lname = methodInfo['name'].lower()
    daxRequired = [p.lower() for p in methodInfo['parameters'] if p != 'kwargs']

    def _find():
        for op, opInfo in ddbModel['operations'].items():
            if op.lower() == lname:
                shapeName = opInfo['input']['shape']
                shape = ddbModel['shapes'][shapeName]
                if shape['type'] != 'structure':
                    raise Exception(shapeName + ' is not a structure.')

                required = set(shape['required'])
                for member, memberType in shape['members'].items():
                    if member not in required and member not in Param.V1Params \
                            and member.lower() not in daxRequired:
                        yield ArgInfo(member,
                                determine_shape_type(lname, member, ddbModel['shapes'][memberType['shape']]))

    return list(_find())

def find_response_fields(methodInfo, ddbModel):
    lname = methodInfo['name'].lower()

    def _find():
        for op, opInfo in ddbModel['operations'].items():
            if op.lower() == lname:
                shapeName = opInfo['output']['shape']
                shape = ddbModel['shapes'][shapeName]
                if shape['type'] != 'structure':
                    raise Exception(shapeName + ' is not a structure.')

                for member, memberType in shape['members'].items():
                    yield ResponseField(member, member)

    return list(_find())


def build_operation(methodInfo, ddbModel):
    op = Operation(methodInfo['name'],
            methodInfo['serviceId'],
            methodInfo['methodId'],
            build_parameters(methodInfo['parameters']),
            find_optional_args(methodInfo, ddbModel),
            methodInfo.get('internalMethod', False),
            methodInfo.get('asynchronous', False),
            methodInfo.get('authMethod', False),
            methodInfo.get('customResponse', False),
            find_response_fields(methodInfo, ddbModel),
            methodInfo.get('hasKey', False),
            methodInfo.get('customPrepare', False))

    return op

def determine_shape_type(opname, method_name, shapeInfo):
    t = shapeInfo['type']
    if 'enum' in shapeInfo:
        return 'enum'
    elif method_name in Shape.CustomShapeHandlers:
        return 'custom'
    elif opname in ('query', 'scan') and method_name in ('ConsistentRead', 'ScanIndexForward') and t == 'boolean':
        # Soooo ... These params should be sent as bools, but the server expects ints and fails if they're bools
        # We could fix it on the server but still have to workaround in the clients to deal with old versions
        return 'boolinteger'
    else:
        return t

def build_remote(daxModel, ddbModel):
    operations = [build_operation(methodInfo, ddbModel) \
            for method, methodInfo in daxModel['remoteMethods'].items() \
            if allowed(method)]

    return Remote(operations)

def load_models(model_path: Path):
    dax_model_path = model_path / 'DaxModel.json'
    with dax_model_path.open() as f:
        dax_model = json.load(f)

    dax_model_path = model_path / 'dynamodb-2012-08-10.api.json'
    with dax_model_path.open() as f:
        ddb_model = json.load(f)

    return dax_model, ddb_model

def allowed(methodName):
    allowed_methods = ['getItem',
        'putItem',
        'deleteItem',
        'updateItem',
        'scan',
        'query',
        'defineKeySchema',
        'defineAttributeList',
        'defineAttributeListId',
        'authorizeConnection',
        'endpoints',
        'batchGetItem',
        'batchWriteItem',
        'transactGetItems',
        'transactWriteItems'
    ]
    for method in allowed_methods:
        if method in methodName:
            return True

    return False

def render_templates(model: dict, templates: Path, dest: Path):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(templates)),
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='<<',
        variable_end_string='>>',
        comment_start_string='<#',
        comment_end_string='#>',
        trim_blocks=True,
        lstrip_blocks=False,
        keep_trailing_newline=False)
    env.filters['list_strformat'] = list_strformat_filter
    env.filters['macro'] = call_macro_by_name

    for tmpl_file in templates.glob('*.jinja'):
        # Ignore non-root template files (if any)
        if tmpl_file.name.startswith('_'):
            continue

        tmpl = env.get_template(tmpl_file.name)

        tmpl_dest = dest / tmpl_file.stem
        with tmpl_dest.open('w') as tmpl_fp:
            print(tmpl_file, '=>', tmpl_dest)
            tmpl_fp.write(tmpl.render(**model))

def main(args):
    models, templates, dest = args

    dax_model, ddb_model = load_models(Path(models))

    remote = build_remote(dax_model, ddb_model)
    render_templates({'remote': remote}, Path(templates), Path(dest))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


