from typing import Optional

from locatieserver.client.utils import filter_defaults, http_get
from locatieserver.schema.lookup import LookupResponse

PATH = "lookup"


def lookup(
    id: str,
    rows: Optional[int] = 10,
    start: Optional[int] = 0,
    wt: Optional[str] = "json",
    indent: Optional[bool] = True,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    fq: Optional[str] = "type:(gemeente OR woonplaats OR weg OR postcode OR adres)",
) -> LookupResponse:
    params = filter_defaults(
        lookup,
        id=id,
        rows=rows,
        start=start,
        wt=wt,
        indent=indent,
        lat=lat,
        lon=lon,
        fq=fq,
    )

    response = http_get(PATH, params)

    return LookupResponse.parse_raw(response.content)
