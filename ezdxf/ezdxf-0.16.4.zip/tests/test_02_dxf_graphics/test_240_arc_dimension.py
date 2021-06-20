# Copyright (c) 2020, Manfred Moitzi
# License: MIT License

import pytest

import ezdxf
from ezdxf.entities.dimension import ArcDimension
from ezdxf.lldxf.const import DXF2013, DXF2010
from ezdxf.lldxf.tagwriter import TagCollector

ezdxf.options.preserve_proxy_graphics()


@pytest.fixture()
def arcdim():
    return ArcDimension.from_text(ARC_DIM)


def test_load_arc_dimension(arcdim):
    assert arcdim.proxy_graphic is not None
    assert len(arcdim.proxy_graphic) == 968


def test_export_arc_dimension_R2010(arcdim):
    tagwriter = TagCollector(dxfversion=DXF2010)
    arcdim.export_dxf(tagwriter)
    assert (92, 968) in tagwriter.tags, 'Expected group code 92 for proxy graphic length tag. (< DXF R2013)'


def test_export_arc_dimension_R2013(arcdim):
    tagwriter = TagCollector(dxfversion=DXF2013)
    arcdim.export_dxf(tagwriter)
    assert (160, 968) in tagwriter.tags, 'Expected group code 160 for proxy graphic length tag. (>= DXF R2013)'


ARC_DIM = """  0
ARC_DIMENSION
  5
95
102
{ACAD_REACTORS
330
97
102
}
102
{ACAD_XDICTIONARY
360
96
102
}
330
1F
100
AcDbEntity
  8
0
160
               968
310
C80300000D000000540000002000000002000000033E695D8B227240B00D3CF1FB7B5540000000000000000082C85BAC2FDE7240FB1040429FB05740000000000000000000000000000000000000000000000000000000000000F03F5400000020000000020000004AF9442AE7FA60405A2D686189715A4000000000000000
310
00C0DC003571AE5F40043422DDA4515D40000000000000000000000000000000000000000000000000000000000000F03F64000000040000001EA72DF9806A69402CE3B4E7B59D34400000000000000000770FBC9D50855E4000000000000000000000000000000000000000000000F03FB634003D352CE93FB1DDE561C5C1
310
E33F00000000000000000418DC3967E1F83F000000000C0000001200000000000000D0000000260000001F8BC5F8B8B46A40197732241FF06140000000000000000000000000000000000000000000000000000000000000F03F0943D77B25BDEF3F417457E0C451C0BF00000000000000003100370032002C003400320000
310
00000006000000010000000000000000000440000000000000F03F0000000000000000000000000000F03F00000000000000000000000000000000000000000000000000000000000000000000000041007200690061006C00000061007200690061006C002E007400740066000000000000000C00000012000000FF7F0000
310
6400000004000000813C33FBB3606A400278BF21B8F4614000000000000000009AEFA7C64B37034000000000000000000000000000000000000000000000F03F0943D77B25BDEF3F437457E0C451C0BF0000000000000000182D4454FB210940000000000C00000010000000010000000C0000001700000000000000540000
310
0020000000020000001EA72DF9806A69402CE3B4E7B59D344000000000000000001EA72DF9806A69402CE3B4E7B59D3440000000000000000000000000000000000000000000000000000000000000F03F540000002000000002000000B296839B8D1A724001000000F06355400000000000000000B296839B8D1A72400100
310
0000F0635540000000000000000000000000000000000000000000000000000000000000F03F540000002000000002000000632D073753076140FFFFFFFF2F525A400000000000000000632D073753076140FFFFFFFF2F525A40000000000000000000000000000000000000000000000000000000000000F03F5400000020
310
000000020000000960E446A3456F405AF2DBF448AB604000000000000000000960E446A3456F405AF2DBF448AB6040000000000000000000000000000000000000000000000000000000000000F03F
100
AcDbDimension
280
     0
  2
*D1
 10
250.17618126492
 20
133.352655820449
 30
0.0
 11
219.164356790492
 21
143.811700471017
 31
0.0
 70
    40
 71
     5
 42
172.418346780865
 73
     0
 74
     0
 75
     0
  3
ISO-25
100
AcDbArcDimension
 13
289.65957213785
 23
85.5615234375
 33
0.0
 14
136.22890807535
 24
105.2841796875
 34
0.0
 15
203.328243817487
 25
20.616056901609
 35
0.0
 70
     0
 40
0.0
 41
0.0
 71
     0
 16
0.0
 26
0.0
 36
0.0
 17
0.0
 27
0.0
 37
0.0
"""

if __name__ == '__main__':
    pytest.main([__file__])
