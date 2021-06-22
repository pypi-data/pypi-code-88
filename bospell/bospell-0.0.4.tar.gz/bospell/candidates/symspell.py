from typing import List

from symspellpy import SymSpell

from ..config import Config
from . import CandidateModelBase


class SymSpellModel(CandidateModelBase):
    """
    Candidate model based on symspell algorithm.
    https://github.com/wolfgarbe/SymSpell
    """

    def __init__(
        self,
        config: Config,
    ):
        self.sym_spell = SymSpell()
        self.config = config
        self.load_dictionary()

    def load_dictionary(self):
        if not self.config.DICTIONARY_PATH.is_file():
            raise FileNotFoundError("Dictionary doesn't exists")
        self.sym_spell.load_dictionary(
            self.config.DICTIONARY_PATH, term_index=0, count_index=1
        )

    def get_candidates(self, word: str, n=float("inf")) -> List[str]:
        suggestions = self.sym_spell.lookup(
            word, self.config.verbosity, max_edit_distance=self.config.max_edit_distance
        )
        suggested_words = []
        for i, suggestion in enumerate(suggestions):
            if i > n:
                break
            suggested_words.append(suggestion.term)
        return suggested_words
