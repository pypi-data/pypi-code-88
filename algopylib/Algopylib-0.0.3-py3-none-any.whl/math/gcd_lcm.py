def gcd(a : int, b : int) -> int:
    """Computes the greatest common divisor of integers a and b using Euclid's Algorithm.
    gcd(a, b) = gcd(−a, b) = gcd(a, −b) = gcd(−a, −b)
    See proof: https://proofwiki.org/wiki/GCD_for_Negative_Integers
    """
    a_int : bool = isinstance(a, int)
    b_int : bool = isinstance(b, int)
    a = abs(a)
    b = abs(b)

    if not(a_int or b_int):
        raise ValueError("Input arguments are not integers")

    if (a == 0) or (b == 0) :
        raise ValueError("One or more input arguments equals zero")

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a : int, b : int) -> int:
    """Computes the lowest common multiple of integers a and b.
    lcm = product of two number / gcd 
    """
    return abs(a) * abs(b) // gcd(a, b)


def trailing_zero(x : int) -> int:
    """Given a positive integer x, computes the number of trailing zero of x
    """
    cnt : int = 0
    while x and not x & 1:
        cnt += 1
        x >>= 1
    return cnt

def gcd_bit(a : int , b : int) -> int:
    """Given two non-negative integer a and b,
    computes the greatest common divisor of a and b using bitwise operator.
    """
    tza : int = trailing_zero(a)
    tzb : int = trailing_zero(b)
    a >>= tza
    b >>= tzb

    while b:
        if a < b:
            a, b = b, a
        a -= b
        a >>= trailing_zero(a)

    return a << min(tza, tzb)
