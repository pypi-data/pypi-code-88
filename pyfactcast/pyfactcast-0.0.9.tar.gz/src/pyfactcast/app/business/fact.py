from pathlib import Path
from pyfactcast.client.entities import Fact
from typing import List, Optional
from uuid import UUID
from pyfactcast.client.sync import FactStore
from pydantic import parse_file_as


def serial_of(fact_id: UUID, *, fact_store: FactStore = FactStore()) -> Optional[str]:
    with fact_store as fs:
        return fs.serial_of(fact_id=fact_id)


def publish(fact_file: Path, *, fact_store: FactStore = FactStore()) -> None:
    facts = parse_file_as(List[Fact], fact_file)
    for fact in facts:
        fact_store.publish(fact=fact)  # IMPR: Async or as list
