import os
import json
import gzip
import decimal
import random
import string
import six
from collections import OrderedDict

from concurrent.futures import ThreadPoolExecutor, wait as future_wait

import pytest

pytestmark = pytest.mark.integ

import boto3
import botocore
import botocore.exceptions

from amazondax import AmazonDaxClient
from amazondax.DaxError import DaxServiceError

from tests.integ import IntegUtil
from tests.integ.IntegUtil import DDB_LOCAL
import objectpath

METHODS = ['get_item', 'put_item', 'delete_item', 'update_item', 'query', 'scan', 'batch_get_item', 'batch_write_item',
           'transact_write_items', 'transact_get_items']
AUTOCHECK_WRITE_METHODS = {'put_item', 'delete_item', 'batch_write_item', 'transact_write_items'}
PRESERVE_TABLES = bool(os.environ.get('DAX_INTEG_PRESERVE_TABLES'))
DDB_ENDPOINT = os.environ.get('INTEG_TEST_DDB_ENDPOINT')
DAX_ENDPOINT = os.environ.get('INTEG_TEST_DAX_ENDPOINT')


@pytest.fixture(scope='module')
def ddb():
    kwargs = dict(
        endpoint_url=DDB_ENDPOINT
    )

    if DDB_LOCAL:
        kwargs.update(dict(
            region_name='ddblocal',
            aws_access_key_id='AKIAFOO',
            aws_secret_access_key='BARBARBAR'
        ))

    return boto3.resource('dynamodb', **kwargs)


@pytest.fixture(scope='module')
def ddb_client():
    kwargs = dict(
        endpoint_url=DDB_ENDPOINT
    )

    if DDB_LOCAL:
        kwargs.update(dict(
            region_name='ddblocal',
            aws_access_key_id='AKIAFOO',
            aws_secret_access_key='BARBARBAR'
        ))

    return boto3.client('dynamodb', **kwargs)


@pytest.fixture(scope='module')
def tables(request, ddb):
    schema = _load_movieschema()
    samples = _load_moviedata()

    write_samples = list(_select_movies(samples,
                                        ("Apollo 13", 1995),
                                        ("This Is Spinal Tap", 1984),
                                        ("The Pink Panther", 2006),
                                        ("The Italian Job", 2003)))

    tables = [
        ('Movies', samples),
        ('FewMovies', samples[:2]),
        ('WriteMovies', write_samples),
        ('BatchUnprocessKeyTable', list(_batch_unprocessed_key_table_samples(samples))),
        ('BatchWriteTable', samples[:10]),
        ('BatchWriteTableTwo', samples[:10]),
        ('TxnWriteTable1', samples[:10]),
        ('TxnWriteTable2', samples[:10])
    ]

    with ThreadPoolExecutor(max_workers=4) as e:
        creators = [e.submit(_refresh_table, ddb, name, schema, data) for name, data in tables]
        future_wait(creators)

    yield

    if not PRESERVE_TABLES:
        with ThreadPoolExecutor(max_workers=4) as e:
            deleters = [e.submit(_delete_table, ddb, name) for name in set(t[0] for t in tables)]
            future_wait(deleters)


@pytest.fixture
def dax():
    if not DAX_ENDPOINT:
        raise Exception('INTEG_TEST_DAX_ENDPOINT must be specified')

    session = botocore.session.get_session()
    if DDB_LOCAL:
        session.set_credentials('AKIAFOO', 'BARBARBAR')

    with AmazonDaxClient(session, endpoints=[DAX_ENDPOINT]) as dax:
        yield dax


def _load_testcases(methods):
    for method in methods:
        suite = _load_testsuite(method)
        def_table = suite.get('__default_table__', 'Movies')

        for testname, testcase in suite.items():
            if testname.startswith('__'):
                continue
            param_id = testname

            # Push the suite-level default to each test case if not set
            testcase.setdefault('__default_table__', def_table)
            yield pytest.param(method, testname, testcase, id=param_id)


@pytest.mark.parametrize('method,testname,testcase', _load_testcases(METHODS))
def test_integration(dax, tables, method, testname, testcase):
    if '__skip__' in testcase:
        skip = testcase['__skip__']
        if skip == 'ddblocal' and DDB_LOCAL:
            pytest.skip("ddblocal")
        elif skip == True:
            pytest.skip()

    op = getattr(dax, method)

    calls = testcase.get('calls') or [testcase]
    for call in calls:
        request = call['request']
        if request.get('TransactItems') is not None:
            for transact_item in request.get('TransactItems'):
                if transact_item:
                    _, operation_detail = list(transact_item.items())[0]
                    operation_detail['TableName'] = IntegUtil.resolve_table_name(operation_detail['TableName'])
        elif 'RequestItems' not in request:
            request.setdefault('TableName', testcase.get('__default_table__', 'Movies'))
            request['TableName'] = IntegUtil.resolve_table_name(request['TableName'])
        else:
            request['RequestItems'] = {
                IntegUtil.resolve_table_name(tablename): requestinfo
                for tablename, requestinfo in request['RequestItems'].items()
            }

        expected_response = call.get('response')
        if expected_response:
            expected_response = IntegUtil.fixup_response(expected_response)
        if expected_response is not None:
            response = IntegUtil.fixup_response(op(**request))

            custom = CUSTOM_COMPARISONS.get(testname)
            if custom:
                custom(request, response, expected_response)
            else:
                assert response == expected_response

            if method in AUTOCHECK_WRITE_METHODS:
                autocheck(dax, request)
        else:
            expected_error = testcase['error']
            with pytest.raises(botocore.exceptions.ClientError) as err:
                response = op(**request)
            assert err.value.response['Error']['Code'].startswith(expected_error)


def test_empty_attribute(dax):
    table_name = IntegUtil.resolve_table_name('Movies')

    # empty string in SS
    transact_write_params =  {
        'TransactItems': [{
                'Put': {
                    'TableName': table_name,
                    'Item': {
                        'title': {'S': 'TransactWriteItems'},
                        'year': {'N': '2013'},
                        'actors': {'SS': ['De Niro', 'Brad Pitt', '']}
                    }
                }          
            }]
    }
    assert_request_with_empty_attribute(dax, 'transact_write_items', transact_write_params)

    # empty binary
    update_params = {
        'TableName': table_name,
        'Key': {
            'year': {'N': '1984'},
            'title': {'S': 'This Is Spinal Tap'},
        },
        'UpdateExpression': 'SET info.rating = :rating',
        'ExpressionAttributeValues': {
            ':rating': {'BS': [bytes()]}
        }
    }
    assert_request_with_empty_attribute(dax, 'update_item', update_params)


def assert_request_with_empty_attribute(dax, method, params):
    # For now, no exception means it passed
    op = getattr(dax, method)
    op(**params)


def autocheck(dax, request):
    keys = _extract_keys(request)

    for table_name, key, item in keys:
        result = dax.get_item(TableName=table_name, ConsistentRead=True, Key=key)

        if item is not None:
            assert result['Item'] == item
        else:
            assert not result.get('Item')


def _load_testsuite(method):
    testname = method.lower().replace('_', '')
    filename = os.path.join('tests', 'data', 'movietests_{}.json'.format(testname))
    fixup_ctx = {}
    with open(filename) as fp:
        # Preserve ordering of testcases using OrderedDict. Prior to 3.6 ordering was not preserved on load.
        return json.load(fp, object_pairs_hook=lambda obj: IntegUtil.fixup_testcase(OrderedDict(obj), fixup_ctx))


def _load_moviedata():
    mode = 'r' if six.PY2 else 'rt'
    with gzip.open('tests/data/moviedata.json.gz', mode=mode) as fp:
        return json.load(fp, parse_float=decimal.Decimal)


def _load_movieschema():
    with open('tests/data/movietable.json') as fp:
        return json.load(fp)


def _refresh_table(ddb, name, schema, data):
    schema = schema.copy()
    name = IntegUtil.resolve_table_name(name)
    schema['TableName'] = name

    # Create table (deleting if necessary)
    while True:
        try:
            table = ddb.create_table(**schema)
        except botocore.exceptions.ClientError as e:
            _delete_table(ddb, name)
        else:
            table.wait_until_exists()
            break

    # Load data
    with table.batch_writer() as batch:
        for item in data:
            batch.put_item(Item=item)


def _delete_table(ddb, name):
    table = ddb.Table(IntegUtil.resolve_table_name(name))
    table.delete()
    table.wait_until_not_exists()


def _select_movies(movies, *keys):
    movies_tree = objectpath.Tree(movies)
    titles = [x[0] for x in keys]
    years = [x[1] for x in keys]
    # returns iterator over found items
    return movies_tree.execute("$..*[@.title in {titles} and @.year in {years}]".format(titles=str(titles), years=str(years)))


_random_str_stuff = string.ascii_lowercase + string.digits


def random_str(size):
    return ''.join(random.choice(_random_str_stuff) for _ in range(size))


def _batch_unprocessed_key_table_samples(samples):
    for movie in samples[:100]:
        yield {
            'year': movie['year'],
            'title': movie['title'],
            'buf': random_str(200000)
        }


def compare_batchGetUnprocessedKeys(request, actual, expected):
    responses = actual.get('Responses')
    assert responses

    unprocessed_keys = actual.get('UnprocessedKeys')
    assert unprocessed_keys

    response_items = sum(len(table_responses) for table_name, table_responses in responses.items()) + \
                     sum(len(upks['Keys']) for table_name, upks in unprocessed_keys.items())

    request_items = sum(len(item['Keys']) for table_name, item in request['RequestItems'].items())

    assert response_items == request_items


CUSTOM_COMPARISONS = {
    'BatchGetItem UnprocessedKeys': compare_batchGetUnprocessedKeys,
}

_MOVIE_KEY_SCHEMA = None


def _extract_key(item, key_schema):
    key = {}
    for key_elem in key_schema:
        elem_name = key_elem['AttributeName']
        if elem_name in item:
            key[elem_name] = item[elem_name]

    return key


def _extract_keys(request, table_name=None):
    ''' Extract a key from a write request to use in a matching get request. 
    
    Does not handle UpdateItem, because no easy way to auto-check those.
    '''
    global _MOVIE_KEY_SCHEMA
    if not _MOVIE_KEY_SCHEMA:
        schema = _load_movieschema()
        _MOVIE_KEY_SCHEMA = schema['KeySchema']

    key_schema = _MOVIE_KEY_SCHEMA

    if 'UpdateExpression' in request or 'AttributeUpdates' in request:
        raise Exception('Cannot auto-check Updates.')

    # Delete
    if 'Key' in request:
        return [(table_name or request['TableName'], request['Key'], None)]

    # Put
    if 'Item' in request:
        item = request['Item']
        return [(table_name or request['TableName'], _extract_key(item, key_schema), item)]

    # BatchWrite
    keys = []
    if 'RequestItems' in request:
        for table_name, write_requests in request['RequestItems'].items():
            for write_request in write_requests:
                for write_type, write_info in write_request.items():
                    keys.extend(_extract_keys(write_info, table_name))
    return keys
