from datetime import datetime
from decimal import Decimal
from typing import Any, Callable, Dict, List, Tuple
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from zipfile import ZipFile

from sat.utils import get_attr

from ..cfdi import CFDI
from ..concepto import Concepto
from .cfdi_parser import CFDIParser, MissingData


class XML2CFDI(CFDIParser):
    root_elements: Dict[str, Callable] = {
        "Folio": str,
        "Serie": str,
        "NoCertificado": str,
        "Certificado": str,
        "TipoDeComprobante": str,
        "Fecha": datetime.fromisoformat,
        "LugarExpedicion": str,
        "FormaPago": str,
        "MetodoPago": str,
        "Moneda": str,
        "TipoCambio": Decimal,
        "SubTotal": Decimal,
        "Total": Decimal,
    }

    @classmethod
    def _get_root_data(cls, xml: Element) -> Dict[str, Any]:
        data = {
            field: caster(get_attr(xml, field))
            for field, caster in cls.root_elements.items()
            if get_attr(xml, field) is not None
        }
        return data

    @classmethod
    def _get_conceptos(cls, xml: Element) -> List[Concepto]:
        xml_conceptos = xml.find("{http://www.sat.gob.mx/cfd/3}Conceptos")
        if not xml_conceptos:
            return []
        conceptos = [
            Concepto(
                Descripcion=get_attr(concepto, "Descripcion"),
                Cantidad=float(get_attr(concepto, "Cantidad")),
                ValorUnitario=float(get_attr(concepto, "ValorUnitario")),
                Importe=float(get_attr(concepto, "Importe")),
            )
            for concepto in xml_conceptos.findall("{http://www.sat.gob.mx/cfd/3}Concepto")
        ]
        return conceptos

    @classmethod
    def parse(cls, xml: Element, xml_string: str = None) -> CFDI:
        data = cls._get_root_data(xml)
        complemento = xml.find("{http://www.sat.gob.mx/cfd/3}Complemento")
        if not complemento:
            raise MissingData("{http://www.sat.gob.mx/cfd/3}Complemento")
        uuid = get_attr(
            complemento.find("{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital"),
            "UUID",
        )
        data["UUID"] = uuid
        data["Conceptos"] = cls._get_conceptos(xml)
        data["xml"] = xml_string

        cfdi = CFDI(**data)
        return cfdi

    @classmethod
    def _get_xmls(cls, files: List[str]) -> List[Tuple[Element, str]]:
        xmls = [(ElementTree.fromstring(xml_file), xml_file) for xml_file in files]
        return xmls

    @classmethod
    def parse_zip(cls, zipfile: ZipFile) -> List["CFDI"]:
        xml_files = cls._get_files(zipfile)
        xmls = cls._get_xmls(xml_files)
        return [cls.parse(xml[0], xml[1]) for xml in xmls]
