from dataclasses import dataclass


@dataclass
class Concepto:
    Descripcion: str
    Cantidad: float
    ValorUnitario: float
    Importe: float
