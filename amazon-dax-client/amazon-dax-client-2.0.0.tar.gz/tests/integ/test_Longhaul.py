import sys
import os
import json
import gzip
import decimal
import random
import six
import time

from concurrent.futures import ThreadPoolExecutor, wait as future_wait

import pytest

pytestmark = [pytest.mark.integ, pytest.mark.longrunning]

import boto3
import botocore
import botocore.exceptions

from boto3.dynamodb.transform import TypeSerializer, ParameterTransformer

from amazondax import AmazonDaxClient

from tests.integ import IntegUtil
from tests.integ.IntegUtil import DDB_LOCAL

PRESERVE_TABLES = bool(os.environ.get('DAX_INTEG_PRESERVE_TABLES'))
DDB_ENDPOINT = os.environ.get('INTEG_TEST_DDB_ENDPOINT')
DAX_ENDPOINT = os.environ.get('INTEG_TEST_DAX_ENDPOINT')
OPERATIONS = int(os.environ.get('LONGHAUL_TEST_OPERATIONS', '1000'))
PARALLEL = int(os.environ.get('LONGHAUL_TEST_PARALLEL', '1'))

CHUNK_SIZE = OPERATIONS // 100


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
def movie_table(ddb):
    schema = _load_movieschema()
    table_name = IntegUtil.resolve_table_name('Movies')

    print('Refeshing tables...')
    _refresh_table(ddb, table_name, schema, [])

    yield table_name

    if not PRESERVE_TABLES:
        print('Deleting tables...')
        _delete_table(ddb, table_name)


@pytest.fixture(scope='module')
def movie_data():
    samples = _load_moviedata()
    return samples


@pytest.fixture(scope='module')
def dax():
    if not DAX_ENDPOINT:
        raise Exception('INTEG_TEST_DAX_ENDPOINT must be specified')

    session = botocore.session.get_session()
    if DDB_LOCAL:
        session.set_credentials('AKIAFOO', 'BARBARBAR')

    with AmazonDaxClient(session, endpoints=[DAX_ENDPOINT]) as dax:
        yield dax


def _create_segments():
    segment_size = OPERATIONS // 100

    for i in range(0, OPERATIONS, segment_size):
        r = range(i, i + segment_size)
        yield pytest.param(r, id="{}-{}".format(r[0], r[-1]))


_loaded_movies = {}


@pytest.mark.parametrize('segment', _create_segments())
def test_longhaul(dax, movie_table, movie_data, segment):
    print('Segment', '%s-%s' % (segment[0], segment[-1]))
    # Prime at least 1 item
    if movie_data:
        _do_put(dax, movie_table, movie_data, _loaded_movies)

    failed = 0
    failure_limit = max(len(segment) // 100, 2)
    start = time.monotonic()
    for _ in segment:
        if _ % CHUNK_SIZE == 0:
            end = time.monotonic()
            elapsed = end - start
            rps = CHUNK_SIZE / elapsed
            print('Iteration {}/{} ({:.2f}s/{:.2f} RPS)'.format(_, segment[-1], elapsed, rps))
            start = end

        op = random.randint(1, 10)
        try:
            if op == 1 and movie_data:
                _do_put(dax, movie_table, movie_data, _loaded_movies)
            else:
                _do_get(dax, movie_table, movie_data, _loaded_movies)
        except Exception as e:
            # Mark as failed, print the traceback, but continue
            failed += 1
            traceback.print_exc()

        if failed > failure_limit:
            # If the failure count exceeds 1%, stop 
            break

    assert failed == 0


def _do_put(dax, movie_table, movie_data, loaded_movies):
    key, movie = movie_data.popitem()
    # print('Putting', key)

    params = {
        'TableName': movie_table,
        'Item': movie
    }

    # Use the boto3 transformer bits to translate to AV types
    op_model = dax.meta.service_model.operation_model('PutItem')
    serializer = TypeSerializer()
    transformer = ParameterTransformer()
    transformer.transform(params, op_model.input_shape, serializer.serialize, 'AttributeValue')

    response = dax.put_item(**params)
    loaded_movies[key] = movie

    return response


def _do_get(dax, movie_table, movie_data, loaded_movies):
    # Get the value, and then load it back in
    keys = list(loaded_movies.keys())
    random.shuffle(keys)

    key = keys.pop()
    movie = loaded_movies[key]
    year, title = key
    # print('Fetching', year, title)

    key = {
        'year': {'N': str(year)},
        'title': {'S': str(title)}
    }
    response = dax.get_item(TableName=movie_table, Key=key)

    # Use the boto3 transformer bits to translate to AV types
    # TODO Make this work?
    # op_model = dax.meta.service_model.operation_model('GetItem')
    # serializer = TypeDeserializer()
    # transformer = ParameterTransformer()
    # transformer.transform(response, op_model.output_shape, serializer.deserialize, 'AttributeValue')

    # pprint(response)

    # assert response['Item'] == movie

    # TODO For now, assume no exception means it passed


def _load_moviedata():
    mode = 'r' if six.PY2 else 'rt'
    with gzip.open('tests/data/moviedata.json.gz', mode=mode) as fp:
        data = json.load(fp, parse_float=decimal.Decimal)

    return {(item['year'], item['title']): item for item in data}


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


def _main(args):
    ''' Run the test independent of the test runner. '''
    ops = int(args[0]) if len(args) > 0 else OPERATIONS

    _dax_g = dax()
    _dax = next(_dax_g)

    _movie_table_g = movie_table(ddb())
    _movie_table = next(_movie_table_g)
    _movie_data = movie_data()
    segment = range(ops)

    segment_size = ops // PARALLEL
    segments = [range(i, i + segment_size) for i in range(0, ops, segment_size)]
    assert len(segments) == PARALLEL

    opcount = sum(len(s) for s in segments)

    try:
        print('Running', opcount, 'operations on', PARALLEL, 'threads...')
        start = time.monotonic()
        if PARALLEL < 2:
            test_longhaul(_dax, _movie_table, _movie_data, segments[0])
        else:
            with ThreadPoolExecutor(max_workers=PARALLEL) as executor:
                results = [executor.submit(test_longhaul, _dax, _movie_table, _movie_data, segment) for segment in segments]
                print('Waiting for results...')
                future_wait(results)
        end = time.monotonic()
        elapsed = end - start

        print('Performed {} operations in {:.2f}s ({:.2f} RPS) on {} threads.'.format(opcount, elapsed, opcount / elapsed, PARALLEL))
    finally:
        try:
            next(_movie_table_g)
        except StopIteration:
            pass

        try:
            next(_dax_g)
        except StopIteration:
            pass


if __name__ == '__main__':
    sys.exit(_main(sys.argv[1:]))
