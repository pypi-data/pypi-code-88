from typing import Any, Dict

from sat.cfdi import CFDI
from sat.cfdi.parsers import XML2CFDI, Metadata2CFDI


def test_xml2cfdi(zip_cfdi: bytes, cfdi_xml_example: CFDI):
    cfdis = XML2CFDI.from_binary(zip_cfdi)
    assert len(cfdis) == 9
    assert cfdis[0] == cfdi_xml_example


def test_metadata2cfdi(zip_metadata: bytes, cfdi_metadata_example: CFDI):
    cfdis = Metadata2CFDI.from_binary(zip_metadata)
    assert len(cfdis) == 9
    assert cfdis[3] == cfdi_metadata_example


def test_merge(cfdi_xml_example: CFDI, cfdi_metadata_example: CFDI, cfdi_merge_example: CFDI):
    cfdi_xml_example.merge(cfdi_metadata_example)
    assert cfdi_xml_example == cfdi_merge_example


def test_convert_to_dict(cfdi_merge_example: CFDI, cfdi_example_dict: Dict[str, Any]):
    dict_repr = cfdi_merge_example.to_dict()
    assert dict_repr == cfdi_example_dict
