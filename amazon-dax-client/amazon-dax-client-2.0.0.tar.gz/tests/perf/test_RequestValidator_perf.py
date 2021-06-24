from amazondax.RequestValidator import RequestValidator
from tests.integ.test_Integration import METHODS, _load_testcases
from tests.integ.IntegUtil import resolve_table_name
from botocore.session import get_session
from botocore.model import ServiceModel
from amazondax.Constants import PY_TO_OP_NAME

import pytest

pytestmark = pytest.mark.perf


def load_testcases(methods):
    testcases = list(_load_testcases(methods))
    testcases = filter(lambda x: x.values[2].get('response') is not None, testcases)
    return testcases


@pytest.mark.parametrize("method,_,testcase", load_testcases(METHODS))
def test_api_validation_perf(benchmark, method, _, testcase):
    benchmark(lambda: validate_request(method, testcase))

_SESSION = get_session()
_LOADER = _SESSION.get_component('data_loader')
_JSON_MODEL = _LOADER.load_service_model('dynamodb', 'service-2', api_version='2012-08-10')
_SERVICE_MODEL = ServiceModel(_JSON_MODEL, service_name='dynamodb')

def validate_request(method, testcase):
    request = testcase['request']
    if 'TransactItems' in request:
        pass
    elif 'RequestItems' not in request:
        request.setdefault('TableName', testcase.get('__default_table__', 'Movies'))
        request['TableName'] = resolve_table_name(request['TableName'])
    else:
        request['RequestItems'] = {
            resolve_table_name(tablename): requestinfo
            for tablename, requestinfo in request['RequestItems'].items()
        }
    operation_model = _SERVICE_MODEL.operation_model(PY_TO_OP_NAME.get(method))
    RequestValidator.validate_api_using_operation_model(operation_model, request)
