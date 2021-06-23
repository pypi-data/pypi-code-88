# pylint: disable=redefined-outer-name
import random
from datetime import datetime, timedelta
from decimal import Decimal
from importlib import resources
from typing import Any, Dict, List

import pytest

from sat.certificate_handler import CertificateHandler
from sat.cfdi import CFDI, Concepto
from sat.enums import DownloadType, RequestType
from sat.package import Package
from sat.query import Query
from sat.sat_connector import SATConnector
from sat.sat_login_handler import SATLoginHandler

from . import real_fiel

cert = resources.read_binary(real_fiel, "NAPM9608096N8.cer")
key = resources.read_binary(real_fiel, "NAPM9608096N8.key")
password = resources.read_text(real_fiel, "NAPM9608096N8.txt").encode("utf-8")


@pytest.fixture
def certificate_handler():
    new_certificate_handler = CertificateHandler(cert, key, password)
    return new_certificate_handler


@pytest.fixture
def login_handler(certificate_handler):
    _login_handler = SATLoginHandler(certificate_handler)
    return _login_handler


@pytest.fixture
def sat_connector():
    sat_obj = SATConnector(cert, key, password)
    return sat_obj


query_scenarios = [  # TODO make flexible
    (DownloadType.ISSUED, RequestType.CFDI),
    (DownloadType.RECEIVED, RequestType.CFDI),
    (DownloadType.ISSUED, RequestType.METADATA),
    (DownloadType.RECEIVED, RequestType.METADATA),
]


@pytest.fixture(params=query_scenarios)
def query(sat_connector: SATConnector, request):
    if sat_connector.rfc == "EKU9003173C9":
        pytest.skip("Can not connect with demo credentials")
    start = datetime.fromisoformat("2021-01-01T00:00:00")
    end = datetime.fromisoformat("2021-05-01T00:00:00") + timedelta(
        seconds=random.randint(1, 10000)
    )
    query = Query(request.param[0], request.param[1], start, end)
    query.send(sat_connector)
    return query


@pytest.fixture
def packages(sat_connector: SATConnector, query: Query) -> List[Package]:
    packages = query.get_packages(sat_connector)
    return packages


@pytest.fixture
def zip_cfdi() -> bytes:
    with open("tests/downloads/B2A5BB69-D460-4FAD-8482-6E5E2E81843A_01.zip", "rb") as zipfile:
        content = zipfile.read()
        return content


@pytest.fixture
def zip_metadata() -> bytes:
    with open("tests/downloads/195B748C-0091-4558-8DE8-9A37CBA3F42A_01.zip", "rb") as zipfile:
        content = zipfile.read()
        return content


@pytest.fixture
def cfdi_xml_example() -> CFDI:
    cfdi_example = CFDI(
        UUID="FB657B83-4C66-4B45-A352-97BBCA9C1130",
        Folio="1",
        Serie="RINV/2021/",
        NoCertificado="00001000000503989239",
        Certificado="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",
        TipoDeComprobante="E",
        Fecha=datetime(2021, 2, 23, 15, 51, 25),
        LugarExpedicion="44259",
        FormaPago="03",
        MetodoPago="PUE",
        Moneda="MXN",
        SubTotal=Decimal("25000.00"),
        Total=Decimal("29000.00"),
        TipoCambio=None,  # TODO
        Conceptos=[
            Concepto(
                Descripcion="Desarrollo de Software - Plataforma EzBill",
                Cantidad=1,
                ValorUnitario=25000,
                Importe=25000,
            )
        ],
        xml='\ufeff<?xml version="1.0" encoding="UTF-8"?>\n<cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd" Version="3.3" Sello="fAixaFxS9Y7snLVXzC39FdjLqy7vuLHEsuBPTPxT/aLdaXoHPy2UdAoNgSc4X6MBjmNCCIXmpyPrMG7e2aQgymUs2IyuHIBPciwTA6vjRN6P/W0OUzFtM7hXI5l+96JmYa23rizE0Gn49Hhc4CbP8M0l1atzNVzTRkO8MZ1bIRfB09S025l+OzO3XEa4k1JXVPLmq+2yaktcThIbX4IR/4d8L+ic9I4NhjGIN8lm7cQ6qsNGChHXNQcnBey/58w+ePmYV4/pHQMHPFYR6sjAplVBu1nGrEdMOqkHgF9m98dvenTI/vPkxBFA21g7rUvOO/kz5dVn4Rl6tsXxLHIrRA==" Fecha="2021-02-23T15:51:25" Folio="1" Serie="RINV/2021/" FormaPago="03" NoCertificado="00001000000503989239" Certificado="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" SubTotal="25000.00" Moneda="MXN" Total="29000.00" TipoDeComprobante="E" MetodoPago="PUE" LugarExpedicion="44259"><cfdi:CfdiRelacionados TipoRelacion="01"><cfdi:CfdiRelacionado UUID="2BBAD813-2ADE-4F2C-B171-7F0EAEFBEFA9" /></cfdi:CfdiRelacionados><cfdi:Emisor Rfc="NAPM9608096N8" Nombre="Navarro Presas Moisés Alejandro" RegimenFiscal="621" /><cfdi:Receptor Rfc="PGD1009214W0" Nombre="PLATAFORMA GDL S  DE RL DE CV" UsoCFDI="G03" /><cfdi:Conceptos><cfdi:Concepto ClaveProdServ="81111507" Cantidad="1.000000" ClaveUnidad="H87" Unidad="Unidades" Descripcion="Desarrollo de Software - Plataforma EzBill" ValorUnitario="25000.00" Importe="25000.00"><cfdi:Impuestos><cfdi:Traslados><cfdi:Traslado Base="25000.00" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" Importe="4000.00" /></cfdi:Traslados></cfdi:Impuestos></cfdi:Concepto></cfdi:Conceptos><cfdi:Impuestos TotalImpuestosTrasladados="4000.00"><cfdi:Traslados><cfdi:Traslado Importe="4000.00" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" /></cfdi:Traslados></cfdi:Impuestos><cfdi:Complemento><tfd:TimbreFiscalDigital xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" xsi:schemaLocation="http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd" Version="1.1" SelloCFD="fAixaFxS9Y7snLVXzC39FdjLqy7vuLHEsuBPTPxT/aLdaXoHPy2UdAoNgSc4X6MBjmNCCIXmpyPrMG7e2aQgymUs2IyuHIBPciwTA6vjRN6P/W0OUzFtM7hXI5l+96JmYa23rizE0Gn49Hhc4CbP8M0l1atzNVzTRkO8MZ1bIRfB09S025l+OzO3XEa4k1JXVPLmq+2yaktcThIbX4IR/4d8L+ic9I4NhjGIN8lm7cQ6qsNGChHXNQcnBey/58w+ePmYV4/pHQMHPFYR6sjAplVBu1nGrEdMOqkHgF9m98dvenTI/vPkxBFA21g7rUvOO/kz5dVn4Rl6tsXxLHIrRA==" NoCertificadoSAT="00001000000504204441" RfcProvCertif="CVD110412TF6" UUID="FB657B83-4C66-4B45-A352-97BBCA9C1130" FechaTimbrado="2021-02-23T15:51:27" SelloSAT="yx37Ne1EqLmQOT2D0ox9OUhqeBVo0Sr+ew5uIVKQemKT1xgI6TH00EBx14CrcX/871qKCEs17hBD+3E3Vl5v/0SF+nDh0KWHqsc2sGKP0XRDuenEK738DJjaQ2p6JfK3T5v7oOlxqvSMPGOKU9jcO2ZyiiywctoTyuUylzNRxUY9DIcwv0NfCwlKyFoTMvO73M2PAoRmSvPsvUKKwBXMktzGCYozBMn5CrxN2912YUQ8f9dbM/p2JhTcwD+g5c+ekePRaFPjbZS92K80UvT8CXTRSZXcyOPrVcQFOHy4ISve0CZh1XdCt3tzvyv0ChI6zsM1zbapSAojJJ2/Fk6Drw==" /></cfdi:Complemento></cfdi:Comprobante>',
    )
    return cfdi_example


@pytest.fixture
def cfdi_metadata_example() -> CFDI:
    cfdi_example = CFDI(
        UUID="FB657B83-4C66-4B45-A352-97BBCA9C1130",
        Fecha=datetime(2021, 2, 23, 15, 51, 25),
        Total=Decimal("29000"),
        RfcEmisor="NAPM9608096N8",
        NombreEmisor="Navarro Presas Moisés Alejandro",
        RfcReceptor="PGD1009214W0",
        NombreReceptor="PLATAFORMA GDL S  DE RL DE CV",
        RfcPac="CVD110412TF6",
        FechaCertificacionSat=datetime(2021, 2, 23, 15, 51, 27),
        EfectoComprobante="E",
        Estatus="0",
        FechaCancelacion=datetime(2021, 2, 24, 21, 4, 42),
    )
    return cfdi_example


@pytest.fixture
def cfdi_merge_example() -> CFDI:
    cfdi_example = CFDI(
        UUID="FB657B83-4C66-4B45-A352-97BBCA9C1130",
        Folio="1",
        Serie="RINV/2021/",
        NoCertificado="00001000000503989239",
        Certificado="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",
        TipoDeComprobante="E",
        Fecha=datetime(2021, 2, 23, 15, 51, 25),
        LugarExpedicion="44259",
        FormaPago="03",
        MetodoPago="PUE",
        Moneda="MXN",
        SubTotal=Decimal("25000.00"),
        Total=Decimal("29000.00"),
        RfcEmisor="NAPM9608096N8",
        NombreEmisor="Navarro Presas Moisés Alejandro",
        RfcReceptor="PGD1009214W0",
        NombreReceptor="PLATAFORMA GDL S  DE RL DE CV",
        RfcPac="CVD110412TF6",
        FechaCertificacionSat=datetime(2021, 2, 23, 15, 51, 27),
        EfectoComprobante="E",
        Estatus="0",
        FechaCancelacion=datetime(2021, 2, 24, 21, 4, 42),
        TipoCambio=None,  # TODO
        Conceptos=[
            Concepto(
                Descripcion="Desarrollo de Software - Plataforma EzBill",
                Cantidad=1,
                ValorUnitario=25000,
                Importe=25000,
            ),
        ],
        xml='\ufeff<?xml version="1.0" encoding="UTF-8"?>\n<cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd" Version="3.3" Sello="fAixaFxS9Y7snLVXzC39FdjLqy7vuLHEsuBPTPxT/aLdaXoHPy2UdAoNgSc4X6MBjmNCCIXmpyPrMG7e2aQgymUs2IyuHIBPciwTA6vjRN6P/W0OUzFtM7hXI5l+96JmYa23rizE0Gn49Hhc4CbP8M0l1atzNVzTRkO8MZ1bIRfB09S025l+OzO3XEa4k1JXVPLmq+2yaktcThIbX4IR/4d8L+ic9I4NhjGIN8lm7cQ6qsNGChHXNQcnBey/58w+ePmYV4/pHQMHPFYR6sjAplVBu1nGrEdMOqkHgF9m98dvenTI/vPkxBFA21g7rUvOO/kz5dVn4Rl6tsXxLHIrRA==" Fecha="2021-02-23T15:51:25" Folio="1" Serie="RINV/2021/" FormaPago="03" NoCertificado="00001000000503989239" Certificado="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" SubTotal="25000.00" Moneda="MXN" Total="29000.00" TipoDeComprobante="E" MetodoPago="PUE" LugarExpedicion="44259"><cfdi:CfdiRelacionados TipoRelacion="01"><cfdi:CfdiRelacionado UUID="2BBAD813-2ADE-4F2C-B171-7F0EAEFBEFA9" /></cfdi:CfdiRelacionados><cfdi:Emisor Rfc="NAPM9608096N8" Nombre="Navarro Presas Moisés Alejandro" RegimenFiscal="621" /><cfdi:Receptor Rfc="PGD1009214W0" Nombre="PLATAFORMA GDL S  DE RL DE CV" UsoCFDI="G03" /><cfdi:Conceptos><cfdi:Concepto ClaveProdServ="81111507" Cantidad="1.000000" ClaveUnidad="H87" Unidad="Unidades" Descripcion="Desarrollo de Software - Plataforma EzBill" ValorUnitario="25000.00" Importe="25000.00"><cfdi:Impuestos><cfdi:Traslados><cfdi:Traslado Base="25000.00" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" Importe="4000.00" /></cfdi:Traslados></cfdi:Impuestos></cfdi:Concepto></cfdi:Conceptos><cfdi:Impuestos TotalImpuestosTrasladados="4000.00"><cfdi:Traslados><cfdi:Traslado Importe="4000.00" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" /></cfdi:Traslados></cfdi:Impuestos><cfdi:Complemento><tfd:TimbreFiscalDigital xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" xsi:schemaLocation="http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd" Version="1.1" SelloCFD="fAixaFxS9Y7snLVXzC39FdjLqy7vuLHEsuBPTPxT/aLdaXoHPy2UdAoNgSc4X6MBjmNCCIXmpyPrMG7e2aQgymUs2IyuHIBPciwTA6vjRN6P/W0OUzFtM7hXI5l+96JmYa23rizE0Gn49Hhc4CbP8M0l1atzNVzTRkO8MZ1bIRfB09S025l+OzO3XEa4k1JXVPLmq+2yaktcThIbX4IR/4d8L+ic9I4NhjGIN8lm7cQ6qsNGChHXNQcnBey/58w+ePmYV4/pHQMHPFYR6sjAplVBu1nGrEdMOqkHgF9m98dvenTI/vPkxBFA21g7rUvOO/kz5dVn4Rl6tsXxLHIrRA==" NoCertificadoSAT="00001000000504204441" RfcProvCertif="CVD110412TF6" UUID="FB657B83-4C66-4B45-A352-97BBCA9C1130" FechaTimbrado="2021-02-23T15:51:27" SelloSAT="yx37Ne1EqLmQOT2D0ox9OUhqeBVo0Sr+ew5uIVKQemKT1xgI6TH00EBx14CrcX/871qKCEs17hBD+3E3Vl5v/0SF+nDh0KWHqsc2sGKP0XRDuenEK738DJjaQ2p6JfK3T5v7oOlxqvSMPGOKU9jcO2ZyiiywctoTyuUylzNRxUY9DIcwv0NfCwlKyFoTMvO73M2PAoRmSvPsvUKKwBXMktzGCYozBMn5CrxN2912YUQ8f9dbM/p2JhTcwD+g5c+ekePRaFPjbZS92K80UvT8CXTRSZXcyOPrVcQFOHy4ISve0CZh1XdCt3tzvyv0ChI6zsM1zbapSAojJJ2/Fk6Drw==" /></cfdi:Complemento></cfdi:Comprobante>',
    )
    return cfdi_example


@pytest.fixture
def cfdi_example_dict() -> Dict[str, Any]:
    dict_repr = {
        "UUID": "FB657B83-4C66-4B45-A352-97BBCA9C1130",
        "Folio": "1",
        "Serie": "RINV/2021/",
        "NoCertificado": "00001000000503989239",
        "Certificado": "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",
        "TipoDeComprobante": "E",
        "Fecha": datetime(2021, 2, 23, 15, 51, 25),
        "LugarExpedicion": "44259",
        "FormaPago": "03",
        "MetodoPago": "PUE",
        "Moneda": "MXN",
        "SubTotal": Decimal("25000.00"),
        "Total": Decimal("29000.00"),
        "RfcEmisor": "NAPM9608096N8",
        "NombreEmisor": "Navarro Presas Moisés Alejandro",
        "RfcReceptor": "PGD1009214W0",
        "NombreReceptor": "PLATAFORMA GDL S  DE RL DE CV",
        "RfcPac": "CVD110412TF6",
        "FechaCertificacionSat": datetime(2021, 2, 23, 15, 51, 27),
        "EfectoComprobante": "E",
        "Estatus": "0",
        "FechaCancelacion": datetime(2021, 2, 24, 21, 4, 42),
        "TipoCambio": None,  # TODO
        "Conceptos": [
            {
                "Cantidad": 1,
                "Descripcion": "Desarrollo de Software - Plataforma EzBill",
                "Importe": 25000,
                "ValorUnitario": 25000,
            },
        ],
        "xml": '\ufeff<?xml version="1.0" encoding="UTF-8"?>\n<cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd" Version="3.3" Sello="fAixaFxS9Y7snLVXzC39FdjLqy7vuLHEsuBPTPxT/aLdaXoHPy2UdAoNgSc4X6MBjmNCCIXmpyPrMG7e2aQgymUs2IyuHIBPciwTA6vjRN6P/W0OUzFtM7hXI5l+96JmYa23rizE0Gn49Hhc4CbP8M0l1atzNVzTRkO8MZ1bIRfB09S025l+OzO3XEa4k1JXVPLmq+2yaktcThIbX4IR/4d8L+ic9I4NhjGIN8lm7cQ6qsNGChHXNQcnBey/58w+ePmYV4/pHQMHPFYR6sjAplVBu1nGrEdMOqkHgF9m98dvenTI/vPkxBFA21g7rUvOO/kz5dVn4Rl6tsXxLHIrRA==" Fecha="2021-02-23T15:51:25" Folio="1" Serie="RINV/2021/" FormaPago="03" NoCertificado="00001000000503989239" Certificado="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" SubTotal="25000.00" Moneda="MXN" Total="29000.00" TipoDeComprobante="E" MetodoPago="PUE" LugarExpedicion="44259"><cfdi:CfdiRelacionados TipoRelacion="01"><cfdi:CfdiRelacionado UUID="2BBAD813-2ADE-4F2C-B171-7F0EAEFBEFA9" /></cfdi:CfdiRelacionados><cfdi:Emisor Rfc="NAPM9608096N8" Nombre="Navarro Presas Moisés Alejandro" RegimenFiscal="621" /><cfdi:Receptor Rfc="PGD1009214W0" Nombre="PLATAFORMA GDL S  DE RL DE CV" UsoCFDI="G03" /><cfdi:Conceptos><cfdi:Concepto ClaveProdServ="81111507" Cantidad="1.000000" ClaveUnidad="H87" Unidad="Unidades" Descripcion="Desarrollo de Software - Plataforma EzBill" ValorUnitario="25000.00" Importe="25000.00"><cfdi:Impuestos><cfdi:Traslados><cfdi:Traslado Base="25000.00" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" Importe="4000.00" /></cfdi:Traslados></cfdi:Impuestos></cfdi:Concepto></cfdi:Conceptos><cfdi:Impuestos TotalImpuestosTrasladados="4000.00"><cfdi:Traslados><cfdi:Traslado Importe="4000.00" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" /></cfdi:Traslados></cfdi:Impuestos><cfdi:Complemento><tfd:TimbreFiscalDigital xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" xsi:schemaLocation="http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd" Version="1.1" SelloCFD="fAixaFxS9Y7snLVXzC39FdjLqy7vuLHEsuBPTPxT/aLdaXoHPy2UdAoNgSc4X6MBjmNCCIXmpyPrMG7e2aQgymUs2IyuHIBPciwTA6vjRN6P/W0OUzFtM7hXI5l+96JmYa23rizE0Gn49Hhc4CbP8M0l1atzNVzTRkO8MZ1bIRfB09S025l+OzO3XEa4k1JXVPLmq+2yaktcThIbX4IR/4d8L+ic9I4NhjGIN8lm7cQ6qsNGChHXNQcnBey/58w+ePmYV4/pHQMHPFYR6sjAplVBu1nGrEdMOqkHgF9m98dvenTI/vPkxBFA21g7rUvOO/kz5dVn4Rl6tsXxLHIrRA==" NoCertificadoSAT="00001000000504204441" RfcProvCertif="CVD110412TF6" UUID="FB657B83-4C66-4B45-A352-97BBCA9C1130" FechaTimbrado="2021-02-23T15:51:27" SelloSAT="yx37Ne1EqLmQOT2D0ox9OUhqeBVo0Sr+ew5uIVKQemKT1xgI6TH00EBx14CrcX/871qKCEs17hBD+3E3Vl5v/0SF+nDh0KWHqsc2sGKP0XRDuenEK738DJjaQ2p6JfK3T5v7oOlxqvSMPGOKU9jcO2ZyiiywctoTyuUylzNRxUY9DIcwv0NfCwlKyFoTMvO73M2PAoRmSvPsvUKKwBXMktzGCYozBMn5CrxN2912YUQ8f9dbM/p2JhTcwD+g5c+ekePRaFPjbZS92K80UvT8CXTRSZXcyOPrVcQFOHy4ISve0CZh1XdCt3tzvyv0ChI6zsM1zbapSAojJJ2/Fk6Drw==" /></cfdi:Complemento></cfdi:Comprobante>',
    }
    return dict_repr
