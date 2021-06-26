from typing import Optional

from locatieserver.client.utils import filter_defaults, http_get
from locatieserver.schema import SuggestResponse

PATH = "/suggest"


def suggest(
    q: Optional[str] = "*:*",
    fl: Optional[str] = "id,weergavenaam,type,score",
    sort: Optional[str] = "score desc, sortering asc, weergavenaam asc",
    qf: Optional[str] = "score desc, sortering asc, weergavenaam asc",
    bq: Optional[
        str
    ] = "type:provincie^1.5 type:gemeente^1.5 type:woonplaats^1.5 type:weg^1.5 type:postcode^0.5 type:adres^1",
    rows: Optional[int] = 10,
    start: Optional[int] = 0,
    wt: Optional[str] = "json",
    indent: Optional[bool] = True,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    fq: Optional[str] = "type:(gemeente OR woonplaats OR weg OR postcode OR adres)",
) -> SuggestResponse:

    params = filter_defaults(
        suggest,
        q=q,
        fl=fl,
        sort=sort,
        qf=qf,
        bq=bq,
        rows=rows,
        start=start,
        wt=wt,
        indent=indent,
        lat=lat,
        lon=lon,
        fq=fq,
    )

    response = http_get(PATH, params=params)

    return SuggestResponse.parse_raw(response.content)
