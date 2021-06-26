from __future__ import annotations

from typing import List

from pydantic import Field

from locatieserver.schema.base import LocatieserverBaseModel


class Doc(LocatieserverBaseModel):
    bron: str
    woonplaatscode: str
    type: str
    woonplaatsnaam: str
    huis_nlt: str
    openbareruimtetype: str
    gemeentecode: str
    weergavenaam: str
    straatnaam_verkort: str
    id: str
    gemeentenaam: str
    identificatie: str
    openbareruimte_id: str
    provinciecode: str
    postcode: str
    provincienaam: str
    centroide_ll: str
    nummeraanduiding_id: str
    adresseerbaarobject_id: str
    huisnummer: int
    provincieafkorting: str
    centroide_rd: str
    straatnaam: str
    gekoppeld_perceel: List[str]


class Response(LocatieserverBaseModel):
    num_found: int = Field(..., alias="numFound")
    start: int
    docs: List[Doc]


class LookupResponse(LocatieserverBaseModel):
    response: Response
