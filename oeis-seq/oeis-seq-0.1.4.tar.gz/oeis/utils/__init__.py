# coding=utf-8
"""Various utility functions."""
from functools import lru_cache
from itertools import combinations
from math import gcd, isqrt
from random import randrange
from typing import List, Set

__all__ = [
    "aliquot_sum",
    "coprime",
    "divisors",
    "is_abundant",
    "is_deficient",
    "is_perfect",
    "is_prime",
    "is_semiperfect",
    "is_superperfect",
    "proper_divisors",
    "sigma",
]


@lru_cache
def aliquot_sum(n: int) -> int:
    """Return the aliquot sum of n - s(n)."""
    return sum(proper_divisors(n))


@lru_cache
def coprime(a: int, b: int) -> bool:
    """Determine whether a and b are coprime."""
    return gcd(a, b) == 1


@lru_cache
def divisors(n: int) -> List[int]:
    """Return the divisors of n."""
    ret: Set[int] = set()
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
    return sorted(ret)


def _is_composite(a: int, d: int, n: int, s: int) -> bool:
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True


@lru_cache
def is_abundant(n: int) -> bool:
    """
    Return whether or not a number is an Abundant number.

        Args:
            n: Number.
    """
    return aliquot_sum(n) > n


@lru_cache
def is_deficient(n: int) -> bool:
    """
    Return whether or not a number is a Deficient number.

        Args:
            n: Number.
    """
    return aliquot_sum(n) < n


@lru_cache
def is_perfect(n: int) -> bool:
    """
    Return whether or not a number is a Perfect number.

        Args:
            n: Number.
    """
    return aliquot_sum(n) == n


def is_prime(n: int, k: int = 8) -> bool:
    """
    Miller-Rabin primality test.

    Args:
            n: Number to test.
            k: Optional number of rounds, default 8.
    """
    if n in [0, 1, 4, 6, 8, 9]:
        return False
    if n in [2, 3, 5, 7]:
        return True
    s: int = 0
    d: int = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = randrange(2, n)
        if _is_composite(a, d, n, s):
            return False

    return True


@lru_cache
def is_semiperfect(n: int) -> bool:
    """
    Return whether or not a number is a Semiperfect number.

        Args:
            n: Number.
    """
    pd: List[int] = proper_divisors(n)
    l: int = len(pd)
    for i in range(l + 1):
        for combo in combinations(pd, i):
            if sum(combo) == n:
                return True
    return False


@lru_cache
def is_superperfect(n: int) -> bool:
    """
    Return whether or not a number is a Superperfect number.

        Args:
            n: Number.
    """
    return sigma(sigma(n)) == 2 * n


@lru_cache
def proper_divisors(n: int) -> List[int]:
    """Return the proper divisors of n."""
    return divisors(n)[:-1]


@lru_cache
def sigma(n: int) -> int:
    """Return the sum of the positive divisors of n, including 1 and n itself."""
    return sum(divisors(n))
