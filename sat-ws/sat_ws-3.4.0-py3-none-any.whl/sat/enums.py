import enum
from importlib import resources

from . import templates


class DownloadType(enum.Enum):
    """Helper to select the download type"""

    ISSUED = "RfcEmisor"
    RECEIVED = "RfcReceptor"


class RequestType(enum.Enum):
    """Helper to select the request type"""

    CFDI = "CFDI"
    METADATA = "Metadata"


TEMPLATES = {
    "Envelope": resources.read_text(templates.common, "Envelope.xml"),
    "KeyInfo": resources.read_text(templates.common, "KeyInfo.xml"),
    "Signature": resources.read_text(templates.common, "Signature.xml"),
    "SignedInfo": resources.read_text(templates.common, "SignedInfo.xml"),
    "Timestamp": resources.read_text(templates.login, "Timestamp.xml"),
    "LoginEnvelope": resources.read_text(templates.login, "Envelope.xml"),
    "SolicitaDescarga": resources.read_text(templates.query, "SolicitaDescarga.xml"),
    "VerificaSolicitudDescarga": resources.read_text(
        templates.verify, "VerificaSolicitudDescarga.xml"
    ),
    "PeticionDescargaMasivaTercerosEntrada": resources.read_text(
        templates.download, "PeticionDescargaMasivaTercerosEntrada.xml"
    ),
}
