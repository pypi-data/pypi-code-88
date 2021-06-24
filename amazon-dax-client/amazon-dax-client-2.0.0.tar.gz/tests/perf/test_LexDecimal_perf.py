from amazondax import LexDecimal

import pytest
pytestmark = pytest.mark.perf

def d(s):
    return LexDecimal.DYNAMODB_CONTEXT.create_decimal(s)

def b(s):
    return bytes(bytearray([int(i.strip(), 16) for i in s.split()]))

TEST_LEXDECIMAL = [ 
    ( d('-9.9999999999999999999999999999999999999E+125'), 
        b('01 7f ff ff 81 03 00 c0 30 0c 03 00 c0 30 0c 03 00 c0 30 0c 05 7f e0') ),
    ( d('-123.0'), b('3c de 3f 3f fc') ),
    ( d('-1'), b('3e e3 ff f0') ),
    ( d('-1E-130'), b('7e 80 00 00 80 e3 ff f0') ),
    ( d('0'), b('80') ),
    ( d('1E-130'), b('81 7f ff ff 7f 1c 00 00') ),
    ( d('1'), b('c1 1c 00 00') ),
    ( d('3.141592653589793'), b('c1 51 8a b4 55 72 f7 d3 80 00') ),
    ( d('123.0'), b('c3 21 c0 c0 00') ),
    ( d('9.9999999999999999999999999999999999999E+125'), 
        b('fe 80 00 00 7e fc ff 3f cf f3 fc ff 3f cf f3 fc ff 3f cf f3 fa 80 10') ),
]

@pytest.mark.parametrize('num,_', TEST_LEXDECIMAL)
def test_LexDecimal_encode_perf(benchmark, num, _):
    benchmark(lambda: LexDecimal.encode(num))

@pytest.mark.parametrize('_,data', TEST_LEXDECIMAL)
def test_LexDecimal_decode_perf(benchmark, _, data):
    benchmark(lambda: LexDecimal.decode_all(data))

