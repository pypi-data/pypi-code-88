from abc import ABC, abstractmethod
from typing import List


class CandidateModelBase(ABC):
    @abstractmethod
    def get_candidates(self, word: str) -> List[str]:
        pass
