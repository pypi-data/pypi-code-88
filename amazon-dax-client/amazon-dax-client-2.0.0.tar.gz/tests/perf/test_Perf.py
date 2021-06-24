from __future__ import print_function

import string
import botocore
import os
import random
import boto3
import math
import time

import pytest

pytestmark = [pytest.mark.perf, pytest.mark.integ]

import sys; sys.path.append('tests')  # Relative to root directory
from tests.Util import random_str, random_bytes

from amazondax import AmazonDaxClient


def truthy(s):
    if not s:
        return False
    else:
        if s[0] in ('n', 'N', 'f', 'F', '0'):
            return False
        else:
            return True


# dax cluster config, cluster need to be set up before test.
ENDPOINT = os.environ.get('INTEG_TEST_DAX_ENDPOINT', 'dev-dsk-hardyj.aka.amazon.com:8111')
USE_DDB = truthy(os.environ.get('PERFTEST_DDB'))

client_name = 'DDB' if USE_DDB else 'DAX'

# only for putItem test. increase this value when write
# throughput is more than 2k. it's throughput * Unit/throughput
ESTIMATE_WRITE_THROUGHPUT = 3000

OPERATIONS = ['batch_get_item', 'get_item', 'scan', 'query']
ITEM_SIZES = [200, 2000, 50000]
# TODO Add concurrent calls
CONCURRENCY_LEVELS = {
    'DDB': [1, 8, 32],
    'DAX': [1, 2, 8]
}
TOTAL_ITEMS = 100
DURATION = 60


@pytest.fixture
def ddb():
    return boto3.client('dynamodb')


@pytest.fixture
def dax():
    if not ENDPOINT:
        raise Exception('INTEG_TEST_DAX_ENDPOINT must be specified')

    session = botocore.session.get_session()
    if USE_DDB:
        session.set_credentials('AKIAFOO', 'BARBARBAR')

    with AmazonDaxClient(session, endpoints=[ENDPOINT]) as dax:
        yield dax


@pytest.fixture
def client(ddb, dax):
    return ddb if USE_DDB else dax


@pytest.fixture
def create_table(ddb):
    tables = []

    def _table_maker(client_name, client, op, item_size, total_items, concurrency, _table_tracker=tables):
        table_name = '{client_name}_{op}_{item_size}_{total_items}_{concurrency}_{now}_py'.format(
            client_name=client_name,
            op=op,
            item_size=item_size,
            total_items=TOTAL_ITEMS,
            concurrency=1,
            now=int(time.time()))
        rcu = total_items * (1 + math.ceil(item_size / 4096)) * concurrency;
        wcu = ESTIMATE_WRITE_THROUGHPUT if op == 'put_item' else total_items * (1 + math.ceil(item_size / 1024)) * concurrency;
        schema = {
            'TableName': table_name,
            'AttributeDefinitions': [{'AttributeName': 'hk', 'AttributeType': 'S'}, {'AttributeName': 'rk', 'AttributeType': 'S'}],
            'KeySchema': [{'AttributeName': 'hk', 'KeyType': 'HASH'}, {'AttributeName': 'rk', 'KeyType': 'RANGE'}],
            'ProvisionedThroughput': {'ReadCapacityUnits': rcu, 'WriteCapacityUnits': wcu},
        }

        print('Creating table', table_name)
        ddb.create_table(**schema)
        ddb.get_waiter('table_exists').wait(TableName=table_name)

        _table_tracker.append(table_name)

        print('Loading table', table_name, 'with', total_items, 'items')
        items = [_mk_item(item_size, i) for i in range(total_items)]
        reqs = _prep_requests(table_name, 'put_item', items)
        for req in reqs:
            client.put_item(**req)

        return table_name, items

    yield _table_maker

    for table_name in tables:
        print('Deleting table', table_name)
        ddb.delete_table(TableName=table_name)
        ddb.get_waiter('table_not_exists').wait(TableName=table_name)


@pytest.mark.parametrize('op', OPERATIONS)
@pytest.mark.parametrize('item_size', ITEM_SIZES)
@pytest.mark.benchmark(min_rounds=100)
def test_benchmark(benchmark, client, create_table, op, item_size):
    random.seed(0)  # Use the same seed for consistency between runs
    table_name, items = create_table(client_name, client, op, item_size, TOTAL_ITEMS, 1)

    requests = list(_prep_requests(table_name, op, items))

    opfunc = getattr(client, op)
    benchmark(lambda: opfunc(**random.choice(requests)))


def _mk_item(size, i):
    return {
        'hk': {'S': 'hashkey' + str(i)},
        'rk': {'S': 'sortkey' + str(i)},
        'avS': {'S': random_str(int(size / 2))},
        'avB': {'B': random_bytes(int(size / 2))},
        'avN': {'N': str(random.randint(-1 << 30, 1 << 30))},
    }


def _prep_requests(table_name, op, items):
    for i, item in enumerate(items):
        if op == 'get_item':
            yield {
                'TableName': table_name,
                'Key': {'hk': item['hk'], 'rk': item['rk']}
            }
        elif op == 'batch_get_item':
            yield {
                'RequestItems': {
                    table_name: {
                        'Keys': [{'hk': item['hk'], 'rk': item['rk']} for item in items[i:i + TOTAL_ITEMS]],
                        'ProjectionExpression': "hk, rk, avS"
                    }
                }
            }
        elif op == 'put_item':
            yield {
                'TableName': table_name,
                'Item': item
            }
        elif op == 'query':
            yield {
                'TableName': table_name,
                'KeyConditionExpression': 'hk = :hk AND rk = :rk',
                'ExpressionAttributeValues': {
                    ':hk': item['hk'],
                    ':rk': item['rk'],
                },
            }
        elif op == 'scan':
            # for scan, it will scan entire table
            yield {
                'TableName': table_name,
            }
            break
        else:
            raise Exception('Unknown operation ' + op)
