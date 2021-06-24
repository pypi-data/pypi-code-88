from amazondax import LexDecimal

import pytest

from decimal import Decimal, localcontext

from tests.Util import _idfn


def d(s):
    return LexDecimal.DYNAMODB_CONTEXT.create_decimal(s)


def b(s):
    return bytes(bytearray([int(i.strip(), 16) for i in s.split()]))


TEST_LEXDECIMAL = [
    (d('-9.9999999999999999999999999999999999999E+125'),
     b('01 7f ff ff 81 03 00 c0 30 0c 03 00 c0 30 0c 03 00 c0 30 0c 05 7f e0')),
    (d('-123.0'), b('3c de 3f 3f fc')),
    (d('-123'), b('3c de 3f d0')),
    (d('-90.01000'), b('3d 1b f8 ff cf ff')),
    (d('-90.0100'), b('3d 1b f8 ff f4')),
    (d('-90.010'), b('3d 1b f8 ff f8')),
    (d('-90.01'), b('3d 1b f8 ff fc')),
    (d('-11.000'), b('3d e1 7f 3f f8')),
    (d('-11.00'), b('3d e1 7f 3f fc')),
    (d('-11.0'), b('3d e1 7f d0')),
    (d('-11'), b('3d e1 7f e0')),
    (d('-10.100'), b('3d e3 bf 3f f8')),
    (d('-10.10'), b('3d e3 bf 3f fc')),
    (d('-10.1'), b('3d e3 bf d0')),
    (d('-10.010'), b('3d e3 f8 ff f8')),
    (d('-10.01'), b('3d e3 f8 ff fc')),
    (d('-10.001'), b('3d e3 fe 9f f8')),
    (d('-2'), b('3e ca ff f0')),
    (d('-1'), b('3e e3 ff f0')),
    (d('-0.1'), b('3f e3 ff f0')),
    (d('-0.01'), b('40 e3 ff f0')),
    (d('-0.001'), b('41 e3 ff f0')),
    (d('-0.0001'), b('42 e3 ff f0')),
    (d('-0.00001'), b('43 e3 ff f0')),
    (d('-1E-130'), b('7e 80 00 00 80 e3 ff f0')),
    (d('0'), b('80')),
    (d('1E-130'), b('81 7f ff ff 7f 1c 00 00')),
    (d('0.00001'), b('bc 1c 00 00')),
    (d('0.0001'), b('bd 1c 00 00')),
    (d('0.001'), b('be 1c 00 00')),
    (d('0.01'), b('bf 1c 00 00')),
    (d('0.1'), b('c0 1c 00 00')),
    (d('1'), b('c1 1c 00 00')),
    (d('2'), b('c1 35 00 00')),
    (d('3.141592653589793'), b('c1 51 8a b4 55 72 f7 d3 80 00')),
    (d('3.14159265358979'), b('c1 51 8a b4 55 72 f7 c0 20')),
    (d('10.001'), b('c2 1c 01 60 04')),
    (d('10.01'), b('c2 1c 07 00 00')),
    (d('10.010'), b('c2 1c 07 00 04')),
    (d('10.1'), b('c2 1c 40 20')),
    (d('10.10'), b('c2 1c 40 c0 00')),
    (d('10.100'), b('c2 1c 40 c0 04')),
    (d('11'), b('c2 1e 80 10')),
    (d('11.0'), b('c2 1e 80 20')),
    (d('11.00'), b('c2 1e 80 c0 00')),
    (d('11.000'), b('c2 1e 80 c0 04')),
    (d('90.01'), b('c2 e4 07 00 00')),
    (d('90.010'), b('c2 e4 07 00 04')),
    (d('90.0100'), b('c2 e4 07 00 08')),
    (d('90.01000'), b('c2 e4 07 00 30 00')),
    (d('123'), b('c3 21 c0 20')),
    (d('123.0'), b('c3 21 c0 c0 00')),
    (d('9.9999999999999999999999999999999999999E+125'),
     b('fe 80 00 00 7e fc ff 3f cf f3 fc ff 3f cf f3 fc ff 3f cf f3 fa 80 10')),
]


@pytest.mark.parametrize("val,expected", TEST_LEXDECIMAL, ids=_idfn)
def test_lexdecimal_encode(val, expected):
    print(val, val.as_tuple())
    result = LexDecimal.encode(val)

    assert result == expected


@pytest.mark.parametrize("expected,data", TEST_LEXDECIMAL, ids=_idfn)
def test_lexdecimal_decode(expected, data):
    result = LexDecimal.decode_all(data)

    assert result == expected

def test_lexdecimal_decode_all_wrong_type():
    with pytest.raises(TypeError):
        LexDecimal.decode_all(None)

def test_lexdecimal_decode_wrong_type():
    with pytest.raises(TypeError):
        LexDecimal.decode(None)

def test_regression_long():
    # Regression test for computing the size of the encoded byte array
    num = Decimal(
        '1.519043396057566434978347919110056828178617793420044845009095883102266197154983036170458159785045013168790194150005772171485123776663026225265083906941746679973910405487712226922360572160109286090827076840438099560139704109021077055039800992783574226209489067204747368646064279454016947109162015587773374645982363407385318610580528401964567546584779984692390257012118847492632253017295152938061049334216698639782484923671333852898253917484438297806515060144054619575586755908264584998428966635833900328448897013161311192041184225731248515188720354249594803044541017997943733673275617711293386746906471936186661605920860928968943328237982074083977888182412651483608535562031694297058289536988244754588375618162121230365495345691015255028957668241560658402002255378192112746401695967255968778246414510329530913582678929506142265708375720504712549814629448365993242613061373583046901281817825417384505249197569842907151879339231499054003148135601842677695751809087592596946507113528743471045104423997476282338624005970522081700127468869151380640131536800078172950172445606480673750541462894055397499420148923999103971546156968314898287319971866608744671525743690473528323942745338438886549298899754829284582718694198133239949986632293934118351261598803084928864575827542573948274062057885778247343717195523808009809686102995991858298705780338006833410164829798137972194669364972243958207138283628313248174819322874644154437406662833820122947930072048521034645768459084715771457149574679024406949597278639059408919395313400229796162612035343061223639450398459653735214907021029784343593875497348473060433594883367192096557118929922580718994140625E-707')
    expected = b(
        '81 7f ff fd 3e 28 f9 45 7e 69 c0 28 f7 f7 4e c8 f9 b0 46 b6 cf 76 9c 5d 62 4 1f 8 3 99 96 14 23 ba 77 b5 df e4 ee 75 e 73 bf 7a 4 80 54 8d ec 1f 6a c0 c9 34 e5 28 20 c6 16 a6 4e a7 a8 6a 8 64 ac 22 ea a7 fc 59 30 d2 30 c3 ce ab 0 f8 11 4e 40 5b ac 9b 45 eb 3e b8 d f3 5f 20 19 f5 9a 6e 48 77 b3 60 3f 80 6f 48 97 16 ca 78 f0 39 6b 71 e6 bb 36 c9 a9 b7 ef 59 db a d2 e8 d 58 eb 15 57 5d c9 88 f8 58 2e e8 7f 69 11 84 d 50 d0 75 2f ea 79 e9 fc 9e 13 ec 25 b2 4d fe 2 f9 44 ce d4 e6 e5 83 d3 1c c8 74 ec 5b 1a a7 6b f7 90 47 e1 7b 24 58 d4 b7 45 64 ef 87 1f 49 c6 29 78 18 1a 68 5d 9f 26 3a ab e5 ad 19 d6 7f f5 6e 32 a3 94 d9 20 b3 58 e1 6c 95 20 8f 20 cd 82 9 b2 92 48 8d 7e 12 dd 2 f6 d3 cb 7b 13 c7 48 71 ca f2 66 5 7b 54 e3 dc 3c 8d 57 aa ea fa 93 33 67 6a 98 ac 97 6 21 a3 8c e2 95 8d f 2a 36 da 46 67 20 cf 8f d4 54 a0 5d 36 18 e0 d7 2d 5b 9b 37 48 f1 6c 6d 11 e7 75 b5 18 f7 3c 38 8 70 c2 31 88 a4 51 c6 19 80 b8 bc 2b 44 2a 4 dd 50 d4 3b 62 5c fc df 47 a8 c2 d6 60 b8 66 d e7 44 a3 5c f0 b3 c5 19 d7 24 5f 88 f0 a7 23 ba 46 d4 64 80 f9 e3 42 be 17 6b bc d4 26 35 41 11 4f 89 55 c9 3c af 88 c3 7 1a 8a 6e e7 3a 18 e8 f0 f 91 2e b5 cc 7e c7 a7 28 79 56 71 46 ce 63 c3 11 17 c3 64 b3 3 98 c0 d0 fb a 96 b4 d6 cd d9 67 1d 20 a7 19 9b bd e8 3 d7 6a 67 26 11 0 dc 2d 81 8b db 82 e7 c9 61 30 19 29 6b 40 4f 3d 4c c1 d4 2 3c a5 4 f6 c 42 27 92 d6 86 27 be 7b a0 6b 88 66 f9 a6 64 a6 9c ec 4d 2d f5 d2 2e 7f c4 c6 a8 37 67 7c a4 92 97 d0 ed 6c d3 19 64 7a 21 d5 f8 4a 6b ad e1 7d b7 bb ac 75 91 bd c5 af ce 54 ff bb f2 a8 cf 16 55 a7 d3 c8 a2 af 7c 50 1f 8e 9 d5 94 af e4 35 96 d1 da 23 67 20 93 74 4b a9 7f b6 e3 46 23 2c f8 3d 49 b9 37 98 cc 5d 27 72 93 82 dc b2 b7 58 41 c7 bb df ce 72 93 9d de ed 1f d3 b1 97 d0 2d 5d 21 76 d2 d5 c f5 ed ec 12 b7 71 ab 71 ef a 99 27 62 81 84 cb 25 4 cd 8d 80 73 77 24 cd 67 98 78 e4 d2 76 d6 f2 5d fe 49 c4 b0 bc bb 8f 6b e5 7b 8e 1f b7 87 d6 0 8b df 9d 11 13 5e 22 4f 88 65 df bd c f5 9f 45 81 85 5f 6b 28 72 f7 9b e5 cd 8f 8c 6e ad 6d 3e d d7 37 d1 5c b6 cd da 6e d3 e2 3e c4 38 53 e3 da a1 2a 0 0 0')

    with localcontext() as ctx:
        ctx.prec = 2048
        result = LexDecimal.encode(num, context=ctx)

        assert result == expected
