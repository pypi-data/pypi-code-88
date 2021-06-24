import pytest

import re
import time
import itertools
import copy
from contextlib import closing

from amazondax import ClusterUtil
from amazondax.Router import ServiceEndpoint, EndpointRouter, EndpointBackend, Role, AddrPort
from amazondax.DaxClient import DaxClient
from amazondax.DaxError import DaxClientError, DaxServiceError

from tests.Util import _dummy_periodic_task

from pprint import pprint

DEFAULT_ENDPOINT = {
    'hostname': 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com',
    'address': '10.0.0.1',
    'az': 'us-west-2c',
    'leader_session_id': 1,
    'node': 1,
    'port': 8111,
    'role': 1
}

DEFAULT_ENDPOINTS = [{
    'hostname': 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com',
    'address': '10.0.0.1',
    'az': 'us-west-2c',
    'leader_session_id': 1,
    'node': 1,
    'port': 8111,
    'role': 1
}, {
    'hostname': 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com',
    'address': '10.0.0.2',
    'az': 'us-west-2a',
    'leader_session_id': 1,
    'node': 0,
    'port': 8111,
    'role': 2
}, {
    'hostname': 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com',
    'address': '10.0.0.3',
    'az': 'us-west-2b',
    'leader_session_id': 1,
    'node': 2,
    'port': 8111,
    'role': 2
}]

DEFAULT_ENDPOINT = DEFAULT_ENDPOINTS[0]
DEFAULT_ADDRESSES = frozenset(ep['address'] for ep in DEFAULT_ENDPOINTS)

DEFAULT_SEEDS = [('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', 8111)]

DEFAULT_DNS = {
    DEFAULT_SEEDS[0][1]: [(DEFAULT_SEEDS[0][1], (ep['address'], ep['port'])) for ep in DEFAULT_ENDPOINTS]
}

IP_RX = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')


def _mock_dns_result_impl(host, port, dns):
    try:
        return dns[host]
    except KeyError:
        if IP_RX.match(host):
            return [(host, port)]
        else:
            return []


def _custom_dns(dns):
    return lambda host, port: _mock_dns_result_impl(host, port, dns)


_mock_dns_result = _custom_dns(DEFAULT_DNS)


def test_EndpointBackend_up(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    endpoint = ServiceEndpoint.from_endpoint(DEFAULT_ENDPOINT)

    client = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    client_factory = mocker.Mock(return_value=client)
    on_up = mocker.Mock()
    on_down = mocker.Mock()

    with closing(EndpointBackend(endpoint, client_factory, 5.0, on_up, on_down)) as backend:
        backend.start()
        assert backend.leader
        assert backend.active
        assert backend.client is client

    assert backend._closed
    assert backend.client is None

    on_up.assert_called_once_with(backend)
    on_down.assert_called_once_with(backend)  # down is called on close


def test_EndpointBackend_down(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    endpoint = ServiceEndpoint.from_endpoint(DEFAULT_ENDPOINT)

    client = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    client_factory = mocker.Mock(return_value=client)
    on_up = mocker.Mock()
    on_down = mocker.Mock()

    with closing(EndpointBackend(endpoint, client_factory, 5.0, on_up, on_down)) as backend:
        backend.start()
        assert backend.leader
        assert backend.active
        backend.down()
        assert not backend.active

    assert backend._closed
    assert client.close.called
    assert backend.client is None

    on_down.assert_called_once_with(backend)
    on_up.assert_called_once_with(backend)


def test_EndpointBackend_health_check_fail(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    endpoint = ServiceEndpoint.from_endpoint(DEFAULT_ENDPOINT)

    client = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(side_effect=OSError))
    client_factory = mocker.Mock(return_value=client)
    on_up = mocker.Mock()
    on_down = mocker.Mock()

    with closing(EndpointBackend(endpoint, client_factory, 5.0, on_up, on_down)) as backend:
        backend.start()
        assert not backend.active


def test_EndpointBackend_background_health_check_pass(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    endpoint = ServiceEndpoint.from_endpoint(DEFAULT_ENDPOINT)

    client = mocker.Mock(spec=DaxClient,
                         endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS),
                         _tube_pool=mocker.Mock())
    client_factory = mocker.Mock(return_value=client)
    on_up = mocker.Mock()
    on_down = mocker.Mock()

    with closing(EndpointBackend(endpoint, client_factory, 0.1, on_up, on_down)) as backend:
        backend.up()
        time.sleep(0.2)
        assert backend.active


def test_EndpointBackend_background_health_check_fail(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    endpoint = ServiceEndpoint.from_endpoint(DEFAULT_ENDPOINT)

    client_factory = mocker.Mock()
    client = client_factory()
    # This will return the empty list on the first call to endpoints() (the
    # synchronous one in start()), then a StopIteration exception for the
    # calls from the background thread.
    client.endpoints.side_effect=[[]]

    on_up = mocker.Mock()
    on_down = mocker.Mock()

    with closing(EndpointBackend(endpoint, client_factory, 0.1, on_up, on_down)) as backend:
        backend.start()
        # wait long enough to start getting endpoints() failures
        time.sleep(0.2)
        assert not backend.active

    # this should only be called once, on health check failure, and not again on close
    on_down.assert_called_once_with(backend)


SERVICE_ENDPOINTS = [
    ServiceEndpoint(1, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.1', 8111, 1, 'us-west-2c', 1),
    ServiceEndpoint(0, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.2', 8111, 2, 'us-west-2a', 1),
    ServiceEndpoint(2, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.3', 8111, 2, 'us-west-2b', 1)
]


def test_EndpointRouter_update(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.3', 8111)}

    newaddrport1 = AddrPort('10.0.0.1', 8111)
    newaddrport2 = AddrPort('10.0.0.2', 8111)
    newaddrport3 = AddrPort('10.0.0.3', 8111)
    client_factory.assert_has_calls([
        mocker.call('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport1),
        mocker.call('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport2),
        mocker.call('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport3),
    ], any_order=True)


def test_EndpointRouter_close(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

    assert not router.backends


def test_EndpointRouter_update_no_change(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

        router.update(SERVICE_ENDPOINTS)

        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.3', 8111)}


def test_EndpointRouter_update_new_leader(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    new_service_endpoints = {
        ServiceEndpoint(1, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.1', 8111, 2, 'us-west-2c', 1),
        ServiceEndpoint(0, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.2', 8111, 1, 'us-west-2a', 1),
        ServiceEndpoint(2, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.3', 8111, 2, 'us-west-2b', 1)
    }

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

        router.update(new_service_endpoints)
        time.sleep(0.1)
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.2', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.1', 8111), ('10.0.0.3', 8111)}


def test_EndpointRouter_update_add_endpoint(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    new_service_endpoints = {
        ServiceEndpoint(1, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.1', 8111, 1, 'us-west-2c', 1),
        ServiceEndpoint(0, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.2', 8111, 2, 'us-west-2a', 1),
        ServiceEndpoint(2, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.3', 8111, 2, 'us-west-2b', 1),
        ServiceEndpoint(3, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.4', 8111, 2, 'us-west-2b', 1),
    }

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)
        newaddrport1 = AddrPort('10.0.0.1', 8111)
        newaddrport2 = AddrPort('10.0.0.2', 8111)
        newaddrport3 = AddrPort('10.0.0.3', 8111)

        client_factory.assert_has_calls([
            mocker.call('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport1),
            mocker.call('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport2),
            mocker.call('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport3),
        ], any_order=True)

        router.update(new_service_endpoints)
        time.sleep(0.1)
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.3', 8111), ('10.0.0.4', 8111)}

    newaddrport4 = AddrPort('10.0.0.4', 8111)
    client_factory.assert_called_with('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport4)


def test_EndpointRouter_update_remove_endpoint(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    new_service_endpoints = {
        ServiceEndpoint(1, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.1', 8111, 1, 'us-west-2c', 1),
        ServiceEndpoint(0, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.2', 8111, 2, 'us-west-2a', 1),
    }

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

        router.update(new_service_endpoints)
        time.sleep(0.1)
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111)}


def test_EndpointRouter_update_replace_replica(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    new_service_endpoints = {
        ServiceEndpoint(1, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.1', 8111, 1, 'us-west-2c', 1),
        ServiceEndpoint(0, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.2', 8111, 2, 'us-west-2a', 1),
        ServiceEndpoint(2, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.4', 8111, 2, 'us-west-2b', 1)
    }

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

        router.update(new_service_endpoints)
        time.sleep(0.1)
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.4', 8111)}

    newaddrport = AddrPort('10.0.0.4', 8111)
    client_factory.assert_called_with('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport)


def test_EndpointRouter_update_replace_leader(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    new_service_endpoints = {
        ServiceEndpoint(1, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.4', 8111, 1, 'us-west-2c', 1),
        ServiceEndpoint(0, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.2', 8111, 2, 'us-west-2a', 1),
        ServiceEndpoint(2, 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', '10.0.0.3', 8111, 2, 'us-west-2b', 1)
    }

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

        router.update(new_service_endpoints)
        time.sleep(0.1)
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.4', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.3', 8111)}

    newaddrport = AddrPort('10.0.0.4', 8111)
    client_factory.assert_called_with('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport)


def test_EndpointRouter_unhealthy_replica(mocker):
    client_factory = mocker.Mock()
    mock_clients = {}

    def client_factory(scheme, hostname, sockaddr):
        try:
            return mock_clients[(scheme, hostname, sockaddr)]
        except KeyError:
            client = mocker.Mock(spec=DaxClient,
                                 endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS),
                                 _tube_pool=mocker.Mock())
            return mock_clients.setdefault((scheme, hostname, sockaddr), client)

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 0.2, 0.1)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

        # Make 10.0.0.2 start failing health checks
        newaddrport = AddrPort('10.0.0.2', 8111)
        mock_clients[('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport)].endpoints.side_effect = OSError()

        # Let the health check fail and remove the backend
        time.sleep(0.2)

        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.3', 8111)}


def test_EndpointRouter_next_leader_empty(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        client = router.next_leader(None)
        assert client is None


def test_EndpointRouter_next_any_empty(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        client = router.next_any(None)
        assert client is None


def test_EndpointRouter_next_leader_one(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)

    leader_client = mocker.Mock()
    replica_client = mocker.Mock()
    newaddrport = AddrPort('10.0.0.1', 8111)
    client_factory = mocker.Mock(side_effect=lambda scheme, hostname, sockaddr: leader_client if (scheme, hostname, sockaddr) == ('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport) else replica_client)

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=0, leader_min=1)

        client = router.next_leader(None)
        assert client is leader_client


def test_EndpointRouter_next_any_one(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)

    leader_client = mocker.Mock()
    replica_client = mocker.Mock()
    newaddrport = AddrPort('10.0.0.1', 8111)
    client_factory = mocker.Mock(side_effect=lambda scheme, hostname, sockaddr: leader_client if (scheme, hostname, sockaddr) == ('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport) else replica_client)

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        # Force a no-leader situation to prevent selecting the leader
        router.update(SERVICE_ENDPOINTS[1:2])
        router.wait_for_routes(min_healthy=1, leader_min=0)

        client = router.next_any(None)
        assert client is replica_client


def test_EndpointRouter_next_any_multi(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock()

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=3, leader_min=1)

        client = router.next_any(None)

        # Don't care which, as long as we got one
        assert client is not None


def test_EndpointRouter_next_leader_one_previous(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock(side_effect=lambda scheme, hostname, sockaddr: mocker.Mock())

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=0, leader_min=1)

        client = router.next_leader(None)
        client2 = router.next_leader(client)

        # Only one leader, so it must be the same
        assert client2 is client


def test_EndpointRouter_next_any_previous(mocker):
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    client_factory = mocker.Mock(side_effect=lambda scheme, host, port: mocker.Mock())

    with closing(EndpointRouter(client_factory, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.update(SERVICE_ENDPOINTS)
        router.wait_for_routes(min_healthy=2, leader_min=1)

        client = router.next_any(None)
        for i in range(100):
            # Run it a lot to try and force a collision.
            # This is a hack, but dealing with random selection is a pain.
            client2 = router.next_any(client)

            # There are other options so it must not be the same
            assert client2 is not client

            client = client2


def test_EndpointRouter_bootstrap(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    _mock_client = mocker.Mock(spec=DaxClient,
                               endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _new_client = mocker.Mock(return_value=_mock_client)

    with closing(EndpointRouter(_new_client, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.start()
        router.wait_for_routes(min_healthy=3, leader_min=1, timeout=1.0)

        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.3', 8111)}


def test_EndpointRouter_bootstrap_bad_endpoints(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    _mock_client = mocker.Mock(spec=DaxClient,
                               endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _new_client = mocker.Mock(return_value=_mock_client)

    with closing(EndpointRouter(_new_client, [('dax', 'unknown-dns', 8111)], 10.0, 5.0)) as router:
        with pytest.raises(DaxClientError):
            router.start()


def test_EndpointRouter_bootstrap_bad_endpoint_auth(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    _mock_client = mocker.Mock(spec=DaxClient,
                               endpoints=mocker.Mock(side_effect=DaxServiceError('endpoints', 'Auth error', (4, 23, 31), None, None, None)))
    _new_client = mocker.Mock(return_value=_mock_client)

    with closing(EndpointRouter(_new_client, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        with pytest.raises(DaxServiceError):
            router.start()


def test_EndpointRouter_bootstrap_no_endpoints(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    _mock_client = mocker.Mock(spec=DaxClient,
                               endpoints=mocker.Mock(return_value=[]))
    _new_client = mocker.Mock(return_value=_mock_client)

    with closing(EndpointRouter(_new_client, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        with pytest.raises(DaxClientError):
            router.start()


def test_EndpointRouter_bootstrap_no_endpoints_errors(mocker):
    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_mock_dns_result)

    # Samples of error types to ensure it continues to try after failure
    _mock_client = mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS))
    _mock_clients = itertools.chain([
        OSError,
        mocker.Mock(spec=DaxClient, endpoints=mocker.Mock(side_effect=OSError)),
    ], itertools.repeat(_mock_client))
    _new_client = mocker.Mock(side_effect=_mock_clients)

    with closing(EndpointRouter(_new_client, DEFAULT_SEEDS, 10.0, 5.0)) as router:
        router.start()
        router.wait_for_routes(min_healthy=3, leader_min=1, timeout=1.0)

        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.3', 8111)}


def test_EndpointRouter_update_lost_leader(mocker):
    local_dns = DEFAULT_DNS
    disc_endpoint = DEFAULT_SEEDS[0][1]

    # For safety purposes
    create_connection = mocker.patch('socket.create_connection', side_effect=NotImplementedError)
    _resolve_dns = mocker.patch('amazondax.Router._resolve_dns', autospec=True, side_effect=_custom_dns(local_dns))

    _mock_clients = {}

    def _client_factory(scheme, hostname, sockaddr):
        try:
            return _mock_clients[(scheme, hostname, sockaddr)]
        except KeyError:
            client = mocker.Mock(spec=DaxClient,
                                 endpoints=mocker.Mock(return_value=DEFAULT_ENDPOINTS),
                                 _tube_pool=mocker.Mock())
            return _mock_clients.setdefault((scheme, hostname, sockaddr), client)

    with closing(EndpointRouter(_client_factory, DEFAULT_SEEDS, 0.02, 0.01)) as router:
        router.start()
        router.wait_for_routes(min_healthy=3, leader_min=1, timeout=1.0)

        # Make sure the initial setup is as expected
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.1', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.2', 8111), ('10.0.0.3', 8111)}

        # Change the DNS to remove the leader
        local_dns[disc_endpoint] = DEFAULT_DNS[disc_endpoint][1:]

        # Change the endpoints results, except for the leader
        for ip, mock_client in _mock_clients.items():
            if ip != '10.0.0.1':
                new_endpoints = copy.deepcopy(DEFAULT_ENDPOINTS[1:])
                new_endpoints[0]['role'] = 1
                mock_client.endpoints.return_value = new_endpoints

        # Make the leader fail its health checks
        newaddrport = AddrPort('10.0.0.1', 8111)
        _mock_clients[('dax', 'test.fnu483.clustercfg.dax.usw2.cache.amazonaws.com', newaddrport)].endpoints.side_effect = OSError()

        time.sleep(router._update_cluster_interval * 2)
        router.wait_for_routes(min_healthy=2, leader_min=1, timeout=1.0)

        # The only way to get here will be to refresh from DNS
        assert set(router.backends[Role.LEADER].keys()) == {('10.0.0.2', 8111)}
        assert set(router.backends[Role.REPLICA].keys()) == {('10.0.0.3', 8111)}
