import os

from .text_cleaner import clean_text
from .tokenization_kodoc import KodocTokenizer

version_txt = os.path.join(os.path.dirname(__file__), "version.txt")
with open(version_txt) as f:
    __version__ = f.read().strip()


def get_kodoc_tokenizer():
    return KodocTokenizer.from_pretrained(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets"))
