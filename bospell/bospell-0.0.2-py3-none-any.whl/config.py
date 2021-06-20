from pathlib import Path

from botok import WordTokenizer
from symspellpy.symspellpy import Verbosity


class Config:
    pass


class DefaultConfig(Config):
    tokenizer_class = "bospell.tokenizers.BotokWordTokenizer"

    # BoSpell components
    # ------------------

    # Candidates Model
    candidates_model_class = "bospell.candidates.symspell.SymSpellModel"
    DICTIONARY_PATH = (
        Path(__file__).parent / "resources" / "dictionaries" / "general.txt"
    )
    verbosity: Verbosity = Verbosity.CLOSEST
    max_edit_distance: int = 2

    # Error Model
    error_model_class = "bospell.error.NonWordErrorModel"
