import pytest

from amazondax import Cluster
from amazondax.Router import Router
from amazondax.DaxClient import DaxClient
from amazondax.DaxError import DaxClientError

from botocore.credentials import Credentials

DEFAULT_DNS_RESULTS = [('10.0.0.1', 8111), ('10.0.0.2', 8111), ('10.0.0.3', 8111)]

DEFAULT_ENDPOINTS = [{
    'address': '10.0.0.1',
    'az': 'us-west-2c',
    'leader_session_id': 1,
    'node': 1,
    'port': 8111,
    'role': 1
}, {
    'address': '10.0.0.2',
    'az': 'us-west-2a',
    'leader_session_id': 1,
    'node': 0,
    'port': 8111,
    'role': 2
}, {
    'address': '10.0.0.3',
    'az': 'us-west-2b',
    'leader_session_id': 1,
    'node': 2,
    'port': 8111,
    'role': 2
}]

DEFAULT_CREDENTIALS = Credentials('FOO', 'BAR')
DEFAULT_REGION = 'us-west-2'

SEEDS = [('test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', 8111)]
SEEDS_STR = [':'.join(str(c) for c in s) for s in SEEDS]


def test_Cluster_parse_host_ports_with_port():
    hp = Cluster._parse_host_ports('test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com:8111')
    assert hp == ('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', 8111)


def test_Cluster_parse_host_ports_without_port():
    hp = Cluster._parse_host_ports('test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com')
    assert hp == ('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', 8111)


def test_Cluster_read_client(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)

    _mock_client1 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client2 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client3 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _new_client = mocker.Mock(side_effect=_mock_calls({
        ('10.0.0.1', 8111): _mock_client1,
        ('10.0.0.2', 8111): _mock_client2,
        ('10.0.0.3', 8111): _mock_client3,
    }))

    _mock_router = mocker.Mock(spec=Router, next_any=mocker.Mock(return_value=_mock_client2))
    _new_router = mocker.Mock(return_value=_mock_router)

    # Connect to the cluster
    cluster = Cluster.Cluster(DEFAULT_REGION, SEEDS_STR, DEFAULT_CREDENTIALS, router_factory=_new_router, client_factory=_new_client)
    cluster.start()

    client = cluster.read_client()

    assert client is _mock_client2


def test_Cluster_write_client(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)

    _mock_client1 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client2 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client3 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _new_client = mocker.Mock(side_effect=_mock_calls({
        ('10.0.0.1', 8111): _mock_client1,
        ('10.0.0.2', 8111): _mock_client2,
        ('10.0.0.3', 8111): _mock_client3,
    }))

    _mock_router = mocker.Mock(spec=Router, next_leader=mocker.Mock(return_value=_mock_client1))
    _new_router = mocker.Mock(return_value=_mock_router)

    # Connect to the cluster
    cluster = Cluster.Cluster(DEFAULT_REGION, SEEDS_STR, DEFAULT_CREDENTIALS, router_factory=_new_router, client_factory=_new_client)
    cluster.start()

    client = cluster.write_client()

    assert client is _mock_client1


def test_Cluster_read_client_missing(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)

    _mock_client1 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client2 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client3 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _new_client = mocker.Mock(side_effect=_mock_calls({
        ('10.0.0.1', 8111): _mock_client1,
        ('10.0.0.2', 8111): _mock_client2,
        ('10.0.0.3', 8111): _mock_client3,
    }))

    _mock_router = mocker.Mock(spec=Router, next_any=mocker.Mock(return_value=None))
    _new_router = mocker.Mock(return_value=_mock_router)

    # Connect to the cluster
    cluster = Cluster.Cluster(DEFAULT_REGION, SEEDS_STR, DEFAULT_CREDENTIALS, router_factory=_new_router, client_factory=_new_client)
    cluster.start()

    with pytest.raises(DaxClientError):
        client = cluster.read_client()


def test_Cluster_write_client_missing(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)

    _mock_client1 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client2 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_client3 = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _new_client = mocker.Mock(side_effect=_mock_calls({
        ('10.0.0.1', 8111): _mock_client1,
        ('10.0.0.2', 8111): _mock_client2,
        ('10.0.0.3', 8111): _mock_client3,
    }))

    _mock_router = mocker.Mock(spec=Router, next_leader=mocker.Mock(return_value=None))
    _new_router = mocker.Mock(return_value=_mock_router)

    # Connect to the cluster
    cluster = Cluster.Cluster(DEFAULT_REGION, SEEDS_STR, DEFAULT_CREDENTIALS, router_factory=_new_router, client_factory=_new_client)
    cluster.start()

    with pytest.raises(DaxClientError):
        client = cluster.write_client()


def _mock_calls(d):
    return lambda *x: d[x]
