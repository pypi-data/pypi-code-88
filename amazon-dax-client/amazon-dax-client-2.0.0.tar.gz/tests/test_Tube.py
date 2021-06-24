from contextlib import closing

from amazondax.Tube import Tube, TubePool
from amazondax.CborEncoder import CborEncoder

from tests.Util import mktube


def seq_clock(seq):
    it = iter(seq)
    return lambda: next(it)


BASE_TIME = 1508524573  # in seconds


def cbor_bytes(s):
    return CborEncoder().append_string(s).as_bytes()


def test_tube_init():
    ''' Test connection initialization sequence is sent correctly. '''
    expected = b'gJ7yne5G\x00\xf6\xa1iUserAgent%s\x00' % cbor_bytes(Tube.DEFAULT_USER_AGENT)

    tube = mktube(b'')
    result = bytes(tube._socket.send_buf)

    assert result == expected


def test_tube_init_custom_ua():
    ''' Test connection initialization sequence is sent correctly. '''
    expected = b'gJ7yne5G\x00\xf6\xa1iUserAgent%s\x00' % cbor_bytes('FooBar')

    tube = mktube(b'', user_agent='FooBar')
    result = bytes(tube._socket.send_buf)

    assert result == expected


def test_tube_init_ua_extra():
    ''' Test connection initialization sequence is sent correctly. '''
    expected = b'gJ7yne5G\x00\xf6\xa1iUserAgent%s\x00' % cbor_bytes(Tube.DEFAULT_USER_AGENT + ' FooBar')

    tube = mktube(b'', user_agent_extra='FooBar')
    result = bytes(tube._socket.send_buf)

    assert result == expected


def test_tube_reauth_needed():
    expected = b'\x01\x1aX\xc23kgAKIAFOOx@c6b96fffdc32ac64adfcafb0459392fbc1929abd2000488eff9fa8f00cc100c4X\x81AWS4-HMAC-SHA256\n20171020T183613Z\n20171020/test/dax/aws4_request\nffdd4feb6735f017d005ec44564abbaf5b507b01ac3824d747bf8dfd4537154f\xf6%s' % cbor_bytes(
        Tube.DEFAULT_USER_AGENT)
    timings = [BASE_TIME]

    tube = mktube(b'', seq_clock(timings))
    del tube._socket.send_buf[:]  # Remove the init data
    tube.reauth()
    tube.flush()

    result = bytes(tube._socket.send_buf)
    assert result == expected


def test_tube_reauth_not_needed():
    expected = b''
    timings = [BASE_TIME + 100]

    tube = mktube(b'', seq_clock(timings))
    del tube._socket.send_buf[:]  # Remove the init data
    tube._auth_exp = BASE_TIME * 1000 + tube._auth_ttl_millis  # in millis
    tube._last_pool_auth = BASE_TIME * 1000  # in millis
    tube.reauth()
    tube.flush()

    result = bytes(tube._socket.send_buf)
    assert result == expected


class MockTubePool(TubePool):
    def _alloc(self):
        return mktube(b'', version=self._session_version)


def test_tube_pool():
    _pool = None
    init_version = None
    with closing(MockTubePool()) as pool:
        assert pool._head_tube is None

        _pool = pool
        init_version = pool._session_version

        _tube = None
        with pool.get() as tube:
            _tube = tube
            assert tube is not None
            assert tube._next_tube is None
            assert pool._head_tube is None

        assert pool._head_tube is _tube

    assert _pool._session_version != init_version


def test_tube_pool_many():
    with closing(MockTubePool()) as pool:
        _tube1 = _tube2 = None
        with pool.get() as tube1, pool.get() as tube2:
            _tube1 = tube1
            _tube2 = tube2
            assert tube1 is not None
            assert tube2 is not None

        assert pool._head_tube is _tube1
        assert _tube1._next_tube is _tube2
        assert _tube2._next_tube is None


def test_tube_pool_except():
    with closing(MockTubePool()) as pool:
        try:
            with pool.get() as tube:
                assert tube1 is not None
                raise Exception()
        except Exception:
            pass

        assert pool._head_tube is None
