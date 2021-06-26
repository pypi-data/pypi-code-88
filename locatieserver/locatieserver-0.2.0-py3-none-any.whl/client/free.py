from typing import Optional

from locatieserver.client.utils import filter_defaults, http_get
from locatieserver.schema.free import FreeResponse

PATH = "free"


def free(
    q: Optional[str] = "*:*",
    fl: Optional[str] = "id,weergavenaam,type,score",
    sort: Optional[str] = "score desc, sortering asc, weergavenaam asc",
    df: Optional[str] = "tekst",
    rows: Optional[int] = 10,
    start: Optional[int] = 0,
    wt: Optional[str] = "json",
    indent: Optional[bool] = True,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    fq: Optional[str] = "type:(gemeente OR woonplaats OR weg OR postcode OR adres)",
) -> FreeResponse:

    params = filter_defaults(
        free,
        q=q,
        fl=fl,
        sort=sort,
        df=df,
        rows=rows,
        start=start,
        wt=wt,
        indent=indent,
        lat=lat,
        lon=lon,
        fq=fq,
    )

    response = http_get(PATH, params=params)

    return FreeResponse.parse_raw(response.content)
