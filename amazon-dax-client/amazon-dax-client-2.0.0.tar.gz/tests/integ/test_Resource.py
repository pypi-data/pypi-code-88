import os
import json
import gzip
import decimal
import six

import pytest

pytestmark = pytest.mark.integ

import boto3
import botocore
import botocore.exceptions
from boto3.dynamodb.conditions import Key, Attr

from amazondax import AmazonDaxClient

from tests.integ import IntegUtil
from tests.integ.IntegUtil import DDB_LOCAL

PRESERVE_TABLES = bool(os.environ.get('DAX_INTEG_PRESERVE_TABLES'))
DDB_ENDPOINT = os.environ.get('INTEG_TEST_DDB_ENDPOINT')
DAX_ENDPOINT = os.environ.get('INTEG_TEST_DAX_ENDPOINT')

RESOURCE_TABLE = 'ResourceMovies'


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
def sample_table(request, ddb):
    schema = _load_movieschema()
    samples = _load_moviedata()

    res_samples = list(_select_movies(samples,
                                      ("Apollo 13", 1995),  # get, batch_get, query, scan
                                      ("Toy Story", 1995),  # get, batch_get, query
                                      ("Toy Story 2", 1999),  # delete
                                      ("Jurassic Park", 1993),  # batch_get, scan
                                      ("Armageddon", 1998),  # batch_write
                                      ("The Shawshank Redemption", 1994),  # batch_writer
                                      ("This Is Spinal Tap", 1984)))  # update

    table = _refresh_table(ddb, RESOURCE_TABLE, schema, res_samples)

    yield table

    if not PRESERVE_TABLES:
        _delete_table(ddb, RESOURCE_TABLE)


@pytest.fixture
def dax():
    if not DAX_ENDPOINT:
        raise Exception('INTEG_TEST_DAX_ENDPOINT must be specified')

    session = botocore.session.get_session()
    if DDB_LOCAL:
        session.set_credentials('AKIAFOO', 'BARBARBAR')

    res = AmazonDaxClient.resource(session, endpoints=[DAX_ENDPOINT])
    # import pdb; pdb.set_trace()
    with res as dax:
        yield dax


def test_resource_get(dax, sample_table):
    table = dax.Table(sample_table.name)
    get_params = {
        'Key': {
            'year': 1995,
            'title': 'Apollo 13'
        }
    }

    result = table.get_item(**get_params)

    assert result['Item']['year'] == 1995
    assert result['Item']['title'] == 'Apollo 13'
    assert result['Item']['info']['running_time_secs'] == 8400


def test_resource_batch_get(dax, sample_table):
    batch_get_params = {
        'RequestItems': {
            sample_table.name: {
                'Keys': [{
                    'year': 1995,
                    'title': 'Apollo 13'
                }, {
                    'year': 1993,
                    'title': 'Jurassic Park'
                }]
            }
        }
    }

    result = dax.batch_get_item(**batch_get_params)

    resps = len(result['Responses'][sample_table.name])
    upks = len(result['UnprocessedKeys'][sample_table.name]['Keys']) if result['UnprocessedKeys'] else 0

    assert resps + upks == 2


def test_resource_put(dax, sample_table):
    table = dax.Table(sample_table.name)
    put_params = {
        'Item': {
            'year': 2020,
            'title': 'Untitled',
            'info': {
            }
        }
    }

    result = table.put_item(**put_params)
    check_result = table.get_item(Key={'year': 2020, 'title': 'Untitled'}, ConsistentRead=True)

    assert check_result['Item']['year'] == 2020
    assert check_result['Item']['title'] == 'Untitled'
    assert check_result['Item']['info'] == {}


def test_resource_update(dax, sample_table):
    table = dax.Table(sample_table.name)
    update_params = {
        'Key': {
            "year": 1984,
            "title": "This Is Spinal Tap",
        },
        'ConditionExpression': 'attribute_exists(year)',
        'UpdateExpression': 'SET info.rating = :rating',
        'ExpressionAttributeValues': {
            ':rating': 11
        }
    }

    result = table.update_item(**update_params)
    check_result = table.get_item(Key={'year': 1984, 'title': "This Is Spinal Tap"}, ConsistentRead=True)

    assert check_result['Item']['year'] == 1984
    assert check_result['Item']['title'] == "This Is Spinal Tap"
    assert check_result['Item']['info']['rating'] == 11


def test_resource_delete(dax, sample_table):
    table = dax.Table(sample_table.name)
    delete_params = {
        'Key': {
            'year': 1998,
            'title': 'Toy Story 2'
        }
    }

    result = table.delete_item(**delete_params)
    check_result = table.get_item(Key={'year': 1998, 'title': 'Toy Story 2'}, ConsistentRead=True)

    assert check_result == {}


def test_resource_query(dax, sample_table):
    table = dax.Table(sample_table.name)
    query_params = {
        'KeyConditionExpression': Key('year').eq(1995)
    }

    result = table.query(**query_params)

    assert result['Count'] == 2
    assert len(result['Items']) == 2


def test_resource_scan(dax, sample_table):
    table = dax.Table(sample_table.name)
    scan_params = {
        'FilterExpression': Attr('title').begins_with('Jurassic')
    }

    result = table.scan(**scan_params)

    assert result['Count'] == 1
    assert len(result['Items']) == 1
    assert result['Items'][0]['title'] == 'Jurassic Park'


def test_resource_batch_write(dax, sample_table):
    batch_write_params = {
        'RequestItems': {
            sample_table.name: [{
                'PutRequest': {
                    'Item': {
                        'year': 2021,
                        'title': 'Untitled',
                        'info': {}
                    }
                },
                'DeleteRequest': {
                    'Key': {
                        'year': 1998,
                        'title': 'Armageddon',
                    }
                }
            }]
        }
    }

    result = dax.batch_write_item(**batch_write_params)

    table = dax.Table(sample_table.name)
    check_result = table.get_item(Key={'year': 2021, 'title': 'Untitled'}, ConsistentRead=True)

    assert check_result['Item']['year'] == 2021
    assert check_result['Item']['title'] == 'Untitled'
    assert check_result['Item']['info'] == {}

    check_result = table.get_item(Key={'year': 1998, 'title': 'Armageddon'}, ConsistentRead=True)

    assert check_result == {}


def test_resource_batch_writer(dax, sample_table):
    table = dax.Table(sample_table.name)

    put_params = {
        'Item': {
            'year': 2022,
            'title': 'Untitled',
            'info': {}
        }
    }

    delete_params = {
        'Key': {
            'year': 1994,
            'title': 'The Shawshank Redemption',
        }
    }

    with table.batch_writer() as batch:
        batch.put_item(**put_params)
        batch.delete_item(**delete_params)

    check_result = table.get_item(Key={'year': 2022, 'title': 'Untitled'}, ConsistentRead=True)
    assert check_result['Item']['year'] == 2022
    assert check_result['Item']['title'] == 'Untitled'
    assert check_result['Item']['info'] == {}

    check_result = table.get_item(Key={'year': 1994, 'title': 'The Shawshank Redemption'}, ConsistentRead=True)

    assert check_result == {}


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

    return table


def _delete_table(ddb, name):
    table = ddb.Table(IntegUtil.resolve_table_name(name))
    table.delete()
    table.wait_until_not_exists()


def _select_movies(movies, *keys):
    for movie in movies:
        for title, year in keys:
            if movie['year'] == year and movie['title'] == title:
                yield movie
