from enum import Enum
import re, time

import requests
from bs4 import BeautifulSoup
from requests.sessions import session


class TimePeriod(Enum):
    NONE = -1
    LAST_WEEK = 1
    LAST_MONTH = 2
    LAST_QUARTER = 3
    LAST_HALF_YEAR = 4
    LAST_YEAR = 5
    CUSTOM = 6


class SearchType(Enum):
    """Corresponds to "Ämnesområde".
    NONE: Samtliga
    SUMMONS: Kallelser
    BOLAGSVERKET_REGISTRATIONS: Bolagsverkets registreringar
    BANKRUPTCIES: Konkurser
    FAMILY_LAW: Familjerätt
    DEBT_RESTRUCTURINGS: Skuldsaneringar
    OTHER: Övrigt
    LIQUIDATION_INJUNCTIONS: Likvidationsföreläggande
    PROCLAMATIONS_BUILDING_LAW: Kungörelse enligt plan- och bygglagen
    """

    NONE = -1
    SUMMONS = 1
    BOLAGSVERKET_REGISTRATIONS = 2
    BANKRUPTCIES = 3
    FAMILY_LAW = 4
    DEBT_RESTRUCTURINGS = 5
    OTHER = 6
    LIQUIDATION_INJUNCTIONS = 7
    PROCLAMATIONS_BUILDING_LAW = 8


def parse_details_page(raw_html: str) -> str:
    soup = BeautifulSoup(raw_html, "html.parser")
    event_date = (
        soup.find("dt", string="Publiceringsdatum:").find_previous_sibling("dd").string
    )
    proclamation_text = soup.find("div", "kungtext").string.strip()
    return event_date, proclamation_text


class POIT:
    def __init__(self) -> None:
        self.session = requests.Session()

        self.session.get("https://poit.bolagsverket.se")
        self.session.get(
            "https://poit.bolagsverket.se/poit/PublikSokKungorelse.do?method=redirect&forward=main.sokkungorelse"
        )
        self.session.get(
            "https://poit.bolagsverket.se/poit/PublikSokKungorelse.do?method=avanceradSokning"
        )

    def search(
        self,
        id_number: str = "",
        id_numbers: set = set(),
        time_period: TimePeriod = TimePeriod.NONE,
        search_type: SearchType = SearchType.NONE,
        fetch_details: bool = False,
        custom_from_date: str = None,
        custom_to_date: str = None,
    ) -> list[dict]:
        proclamations = []
        first_page = True
        while True:
            if first_page:
                data = {
                    "selectedPubliceringsIntervall": time_period.value,
                    "fritext": "",
                    "selectedAmnesomrade": search_type.value,
                    "selectedKungorelsetyp": -1,
                    "personorgnummer": id_number,
                    "personorgnamn": "",
                    "kundnamn": "",
                    "selectedKundtyp": -1,
                    "diarienummer": "",
                    "method": "Sök",
                }
                if time_period == TimePeriod.CUSTOM:
                    data["from"] = custom_from_date
                    data["tom"] = custom_to_date
                response = self.session.get(
                    "https://poit.bolagsverket.se/poit/PublikSokKungorelse.do",
                    data=data,
                )
                first_page = False
            else:
                response = self.session.get(
                    "https://poit.bolagsverket.se/poit/PublikSokKungorelse.do",
                    data={
                        "nextFocus": "movenextTop",
                        "scrollPos": "0,0",
                        "gotopageTop": "",
                        "method#button.movenext": ">",
                        "gotopageBottom": "",
                    },
                )

            raw_html = response.text
            soup = BeautifulSoup(raw_html, "html.parser")

            rows_body = soup.tbody
            rows = rows_body.find_all("tr") if rows_body else []

            for row in rows:
                row_id_number = (
                    row.find(headers="h-personorgnummer").string.strip()
                    if not id_number
                    else id_number
                )

                if not id_numbers or row_id_number in id_numbers:
                    proclamation = {
                        "Id": row.find(headers="h-diarienummer").a.string,
                        "Type": row.find(headers="h-kungorelsetyp").string.strip(),
                        "IdNumber": row_id_number,
                        "Name": row.find(headers="h-personorgnamn").string.strip(),
                        "PublishDate": row.find(headers="h-publicerad").string.strip(),
                    }

                    if fetch_details:
                        details_url = row.find(headers="h-diarienummer").a["href"]
                        details_response = self.session.get(
                            f"https://poit.bolagsverket.se{details_url}"
                        )
                        event_date, proclamation_text = parse_details_page(
                            details_response.text
                        )
                        proclamation["EventDate"] = event_date
                        proclamation["ProclamationText"] = proclamation_text

                        # Return to the results page
                        self.session.get(
                            "https://poit.bolagsverket.se/poit/PublikSokKungorelse.do",
                            data={
                                "nextFocus": "movenextTop",
                                "scrollPos": "0,0",
                                "method": "Föregående",
                            },
                        )

                    proclamations.append(proclamation)

            if not id_number:
                page_number_match = re.match(
                    r"Sida (?P<current_page>\d+) av (?P<page_count>\d+)", soup.em.string
                )
                current_page = page_number_match["current_page"]
                page_count = page_number_match["page_count"]

                # print(f"Parsed page {current_page} of {page_count}")

                if current_page == page_count:
                    break
            else:
                break

        return proclamations
