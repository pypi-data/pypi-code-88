from typing import Any, Dict, Optional, Tuple, Union

from upend.util import escape
from upend.lib import LiveServerSession
import logging
from dataclasses import dataclass


@dataclass
class UpEndEntry:
    entity: Optional[str]
    attribute: Optional[str]
    value: Optional[Union[str, int]]

    def as_sexp(self) -> str:
        return f"(matches {self._arg(self.entity)} {self._arg(self.attribute)} {self._arg(self.value)})"

    @staticmethod
    def _arg(arg: Optional[Union[str, int]]) -> str:
        return f'"{escape(str(arg))}"' if arg else "?"

    def __str__(self) -> str:
        return self.as_sexp()


class UpEndError(RuntimeError):
    pass


class UpEndCheckError(UpEndError):
    pass


UpEndOptionalTriplet = Tuple[Optional[str], Optional[str], Optional[str]]
UpEndTriplet = Tuple[Optional[str], str, Union[str, int]]


class UpEnd:
    def __init__(
        self,
        hostname: str = "localhost",
        port: int = 8093,
        ssl: bool = False,
        initial_check: bool = True,
    ) -> None:
        self.logger = logging.getLogger("upend")
        self.session = LiveServerSession(
            f"{'https' if ssl else 'http'}://{hostname}:{port}/api/"
        )

        if initial_check:
            self.check()

    def check(self) -> bool:
        info = self.session.get("info")
        if info.status_code != 200:
            self.logger.error("Connection check failed!")
            raise UpEndCheckError(info.text)
        else:
            self.logger.debug("Connection check passed successfully.")
            return True

    def query(
        self, query: Union[UpEndOptionalTriplet, UpEndEntry, str]
    ) -> Dict[str, Any]:
        query_out = None

        if type(query) is UpEndEntry:
            query_out = query.as_sexp()
        if type(query) is tuple:
            query_out = UpEndEntry(*query).as_sexp()
        if type(query) is str:
            query_out = query

        if query_out is None:
            raise RuntimeError("Incorrect argument type.")

        self.logger.debug(f"Querying: {query_out}")

        result = self.session.get("obj", params={"query": query_out})
        if not result.ok:
            raise UpEndError(result.text)
        return result.json()

    def get_raw(self, address: str, chunk_size: int = 8192):
        request = self.session.get(f"raw/{address}", stream=True)
        request.raise_for_status()
        for chunk in request.iter_content(chunk_size=chunk_size):
            yield chunk

    def insert(
        self, entry: Union[UpEndTriplet, UpEndEntry], value_type: str = "Value"
    ) -> Dict[str, Any]:
        entry_out = None
        if type(entry) is tuple:
            entry_out = UpEndEntry(*entry)
        if type(entry) is UpEndEntry:
            entry_out = entry
        if entry_out is None:
            raise RuntimeError("Incorrect argument type.")
        self.logger.debug(f"Inserting: {entry_out.as_sexp()}")
        request = self.session.put(
            f"obj",
            json={
                "entity": entry_out.entity,
                "attribute": entry_out.attribute,
                "value": {"t": value_type, "c": entry_out.value},
            },
        )
        request.raise_for_status()
        return request.json()
