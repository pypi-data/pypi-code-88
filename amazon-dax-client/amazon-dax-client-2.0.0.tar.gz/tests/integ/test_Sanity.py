import os
import json
import time
import six

from zipfile import ZipFile
from concurrent import futures

import pytest

pytestmark = [pytest.mark.integ, pytest.mark.longrunning]

import boto3
import botocore
import botocore.exceptions

from amazondax import AmazonDaxClient

from tests.integ import IntegUtil
from tests.integ.IntegUtil import DDB_LOCAL

DAX_METHODS = ['get_item', 'put_item', 'delete_item', 'update_item', 'query', 'scan', 'batch_get_item', 'batch_write_item',
               'transact_write_items', 'transact_get_items']
PRESERVE_TABLES = bool(os.environ.get('INTEG_PRESERVE_TABLES'))
USE_EXISTING_TABLES = bool(os.environ.get('SANITY_USE_EXISTING_TABLES'))
DDB_ENDPOINT = os.environ.get('INTEG_TEST_DDB_ENDPOINT')
DAX_ENDPOINT = os.environ.get('INTEG_TEST_DAX_ENDPOINT')

METHOD_MAP = {
    'GetItem': 'get_item',
    'PutItem': 'put_item',
    'UpdateItem': 'update_item',
    'DeleteItem': 'delete_item',
    'Query': 'query',
    'Scan': 'scan',
    'BatchGetItem': 'batch_get_item',
    'BatchWriteItem': 'batch_write_item',
    'TransactWriteItems': 'transact_write_items',
    'TransactGetItems': 'transact_get_items',
    'CreateTable': 'create_table',
    'DeleteTable': 'delete_table',
    'DescribeTable': 'describe_table'
}

SET_TYPES = {'SS', 'NS', 'BS'}

SKIPLIST = {
    '026_TransactGetItems_DataValidationTests_testGetItemWithNullAttributeName_Call_00313',  # not relevant in python environment
}

TEST_ZIPFILE = os.path.join('tests', 'data', 'client_test_data.zip')
TABLE_CREATOR_FILE_PREFIX = '001_HackTableCreator_v2_access'
MAX_PUT_RETRIES = 100


def _load_tests():
    with ZipFile(TEST_ZIPFILE) as tests:
        # Order the tests by file basename
        files = sorted(
            (os.path.basename(name), os.path.dirname(name)) for name in tests.namelist() if name.endswith('.json')
        )

        for name, path in files:
            if name.startswith(TABLE_CREATOR_FILE_PREFIX):
                # Special-case the core table loading
                continue

            # Windows joins path with '\' whereas, zip file is read with '/'. So the result is tests/data\\get.json
            # join the path explicitly
            test_path = path + '/' + name
            with tests.open(test_path) as fp:
                test_data = fp.read()
                if isinstance(test_data, six.binary_type):
                    # Python 3.5 json module requires str, not bytes
                    test_data = test_data.decode('utf8')
                test_suite = json.loads(test_data)
                for test in test_suite:
                    test_id = '{}_{}'.format(name[:-5], test['Id'])
                    kwargs = {}
                    if test_id in SKIPLIST:
                        kwargs['marks'] = pytest.mark.skip

                    # Only pass the test ID and path back to save memory
                    yield pytest.param(test['Id'], test_path, id=test_id, **kwargs)


def _load_testcases():
    return list(_load_tests())


def _gather_tables():
    tables = {}
    with ZipFile(TEST_ZIPFILE) as tests:
        create_list = [name for name in tests.namelist() if TABLE_CREATOR_FILE_PREFIX in name]
        for create_file_name in create_list:
            with tests.open(create_file_name) as create_file:
                # Load the file and convert to unicode/str for compatiblity with all versions
                create_data = create_file.read().decode('utf8')
                creates = json.loads(create_data)
                for create in creates:
                    if create['Operation'] != 'CreateTable':
                        continue

                    create_info = create['Request']
                    table_name = IntegUtil.resolve_table_name(create_info['TableName'])
                    if table_name not in tables:
                        create_info['TableName'] = table_name
                        create_info['BillingMode'] = 'PAY_PER_REQUEST'

                        # Remove any PT fields since we want on-demand
                        create_info.pop('ProvisionedThroughput', None)

                        # Remove PT fields from GSIs
                        for gsi in create_info.get('GlobalSecondaryIndexes', []):
                            gsi.pop('ProvisionedThroughput', None)

                        tables[table_name] = create_info

    return tables


def _wait_for_create(client, table_name):
    waiter = client.get_waiter('table_exists')
    print('Waiting for', table_name, 'to create')
    waiter.wait(TableName=table_name, WaiterConfig={'Delay': 2, 'MaxAttempts': 300})


def _wait_for_delete(client, table_name):
    waiter = client.get_waiter('table_not_exists')
    print('Waiting for', table_name, 'to delete')
    waiter.wait(TableName=table_name, WaiterConfig={'Delay': 2, 'MaxAttempts': 300})


def _create_table(client, table_name, table_info):
    print('Creating', table_name, 'with', table_info)
    while True:
        try:
            client.create_table(**table_info)
        except botocore.exceptions.ClientError as exc:
            if exc.response['Error']['Code'] == 'ResourceInUseException':
                if not USE_EXISTING_TABLES:
                    # Table exists, so delete & try again
                    print(table_name, 'already exists; deleting...')
                    _delete_table(client, table_name)
                else:
                    # Table exists, use it
                    print(table_name, 'already exists; re-using...')
                    break
            elif exc.response['Error']['Code'] == 'LimitExceededException':
                # Hit a parallel create limit, sleep & try again
                print('Table limit exceeded, sleeping for', table_name)
                time.sleep(2)
            else:
                raise
        else:
            break

        print('Retrying', table_name)

    _wait_for_create(client, table_name)
    print(table_name, 'is ready')


def _delete_table(client, table_name):
    print('Deleting', table_name)
    try:
        client.delete_table(TableName=table_name)
    except botocore.exceptions.ClientError as exc:
        if exc.response['Error']['Code'] == 'ResourceNotFoundException':
            # If it doesn't exist, no need to delete it
            print(table_name, 'does not exist')
            pass
        else:
            raise

    _wait_for_delete(client, table_name)


def _create_tables(client, tables):
    # Only 5 indexed tables can be create3d at a time, and that is the bottleneck
    with futures.ThreadPoolExecutor(max_workers=5) as pool:
        fs = [pool.submit(_create_table, client, table_name, table_info) for table_name, table_info in tables.items()]
        # Make sure any exceptions are re-raised; wait() doesn't check result()
        for f in futures.as_completed(fs):
            f.result()


def _delete_tables(client, table_names):
    with futures.ThreadPoolExecutor(max_workers=15) as pool:
        fs = [pool.submit(_delete_table, client, table_name) for table_name in table_names]
        # Make sure any exceptions are re-raised; wait() doesn't check result()
        for f in futures.as_completed(fs):
            f.result()


def _chunkiter(iterable, n):
    if n < 1:
        raise ValueError('n must be >= 1')

    chunk = []
    for i in iterable:
        if len(chunk) == n:
            yield chunk
            chunk = []

        chunk.append(i)

    yield chunk


@pytest.fixture(scope='module')
def tables(ddb_client):
    tables = _gather_tables()
    print('Creating', len(tables), 'tables')

    _create_tables(ddb_client, tables)

    yield tables.keys()

    if not PRESERVE_TABLES:
        # Delete existing tables
        _delete_tables(ddb_client, tables.keys())


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
def dax():
    if not DAX_ENDPOINT:
        raise Exception('INTEG_TEST_DAX_ENDPOINT must be specified')

    session = botocore.session.get_session()
    if DDB_LOCAL:
        session.set_credentials('AKIAFOO', 'BARBARBAR')

    dax = None
    n = 5
    while n >= 0:
        try:
            dax = AmazonDaxClient(session, endpoints=[DAX_ENDPOINT])
        except Exception as e:
            print("Connection failed:", e, ", retrying (" + str(n) + ")...")
            time.sleep(0.1)
            n -= 1
        else:
            break

    yield dax
    dax.close()


@pytest.mark.parametrize('test_id, test_path', _load_tests())
def test_sanity(dax, ddb_client, tables, test_id, test_path):
    testcase = _demand_load_testcase(test_id, test_path)
    method = METHOD_MAP[testcase['Operation']]

    client = dax if method in DAX_METHODS else ddb_client
    op = getattr(client, method)

    request = testcase['Request']
    expected_result = testcase['Result']
    expected_error = testcase['Error']

    attempts = 0
    if not expected_error:
        # Configure retries to avoid PTE/ThroughputExceeded errors
        # More interested in correctness than performance
        config = botocore.config.Config(retries={'max_attempts': 10})
        client._client_config=config
        raw_result = op(**request)

        if method == 'create_table':
            table_name = request['TableName']
            if table_name not in tables:
                _create_table(ddb_client, table_name, request)

            _wait_for_create(ddb_client, table_name)
            # Don't check result for creates
        elif method == 'delete_table':
            table_name = request['TableName']
            if table_name in tables:
                _wait_for_delete(ddb_client, table_name)
                # Don't check result for deletes
        elif method == 'describe_table':
            pass
        else:
            result = IntegUtil.fixup_response(raw_result)
            assert result == expected_result
    else:
        config = botocore.config.Config(retries={'max_attempts': 3})
        client._client_config = config
        with pytest.raises(botocore.exceptions.ClientError) as err:
            result = op(**request)
        expected_error_code = expected_error['Cause']['ErrorCode'] if expected_error.get('Cause') else expected_error['ErrorCode']
        assert err.value.response['Error']['Code'] == expected_error_code


_last_test_suite = None
_last_test_path = None


def _demand_load_testcase(test_id, test_path):
    # Load the tests on demand to reduce peak memory usage
    global _last_test_path, _last_test_suite
    fixup_ctx = {}
    if test_path != _last_test_path:
        # Files are processed in order, so this should be very fast
        with ZipFile(TEST_ZIPFILE) as tests:
            with tests.open(test_path) as fp:
                test_suite_data = json.load(fp, object_hook=lambda obj: IntegUtil.fixup_testcase(obj, fixup_ctx))
                # Map the tests by ID for faster lookup
                test_suite = {test['Id']: test for test in test_suite_data}

        _last_test_path = test_path
        _last_test_suite = test_suite
    else:
        test_suite = _last_test_suite

    return test_suite[test_id]
