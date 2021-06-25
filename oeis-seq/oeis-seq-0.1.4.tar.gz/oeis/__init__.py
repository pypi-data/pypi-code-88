# coding=utf-8
"""OEIS Sequences."""
from .abundant import abundant
from .buttered_croissant import buttered_croissant
from .catalan import catalan
from .centered_polygonal import centered_polygonal, centered_square, centered_triangular
from .composite import composite
from .deficient import deficient
from .eratosthenes import eratosthenes
from .factorial import factorial
from .fibonacci import fibonacci
from .jacobsthal import jacobsthal
from .lazy_caterer import lazy_caterer
from .leonardo import leonardo
from .loeschian import loeschian
from .lucas import lucas
from .oblong import oblong
from .padovan import padovan
from .pell import pell
from .perfect import perfect
from .perrin import perrin
from .polite import polite
from .polygonal import (
    decagonal,
    dodecagonal,
    hendecagonal,
    heptagonal,
    hexagonal,
    natural,
    nonagonal,
    octagonal,
    pentagonal,
    polygonal,
    square,
    triangular,
)
from .pyramidal import square_pyramidal, triangular_pyramidal
from .recaman import recaman
from .semiperfect import semiperfect
from .superperfect import superperfect
from .sylvester import sylvester
from .totient import totient
from .tribonacci import tribonacci
from .vauban import vauban
from .weird import weird
from .woodall import woodall

__version__ = "0.1.4"
__all__ = [
    "abundant",
    "buttered_croissant",
    "catalan",
    "centered_polygonal",
    "centered_square",
    "centered_triangular",
    "composite",
    "decagonal",
    "deficient",
    "dodecagonal",
    "eratosthenes",
    "factorial",
    "fibonacci",
    "hendecagonal",
    "heptagonal",
    "hexagonal",
    "jacobsthal",
    "lazy_caterer",
    "leonardo",
    "loeschian",
    "lucas",
    "natural",
    "nonagonal",
    "oblong",
    "octagonal",
    "padovan",
    "pell",
    "pentagonal",
    "perfect",
    "perrin",
    "polite",
    "polygonal",
    "recaman",
    "semiperfect",
    "square",
    "sylvester",
    "square_pyramidal",
    "superperfect",
    "totient",
    "triangular",
    "triangular_pyramidal",
    "tribonacci",
    "vauban",
    "weird",
    "woodall",
]
