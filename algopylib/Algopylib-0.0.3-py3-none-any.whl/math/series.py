"""
Functions on Arithmetic and Geometric Progression Series. 
"""

import math

def nth_term_ap(a: float, d: float, n: int) -> float:
        '''
        Returns the nth term of an Arithmetic Progression.

        Parameters:
                a: First term of Progression
                d: Common difference of the Progression
                n: nth term to be calculated

        Returns:
                The value of the nth term
        '''
        if n<0:
                raise ValueError("n cannot be negative")
        return (a + (n - 1) * d)


def nth_term_gp(a: float, r: float, n: int) -> float:
        '''
        Returns the nth term of a Geometric Progression.

        Parameters:
                a: First term of Progression
                r: Common ratio of the Progression
                n: nth term to be calculated

        Returns:
                The value of the nth term
        '''
        if n<0:
                raise ValueError("n cannot be negative")
        return ( a * (int)(math.pow(r, n - 1)) )


def sum_ap(a: float, d: float, n: int) -> float:
        '''
        Returns the sum upto n terms of an Arithmetic Progression.

        Parameters:
                a: First term of Progression
                d: Common difference of the Progression
                n: Value (int) upto which sum is to be calculated

        Returns:
                The value of the nth term.
        '''
        if n<0:
                raise ValueError("n cannot be negative")
        return ((n/2) * (2 * a + (n - 1) * d)) 


def sum_gp(a: float, r: float, n: int) -> float:
        '''
        Returns the sum upto n terms of a Geometric Progression.

        Parameters:
                a: First term of Progression
                r: Common ratio of the Progression
                n: Value (int) upto which sum is to be calculated

        Returns:
                The value of the nth term
        '''
        if n<0:
                raise ValueError("n cannot be negative")

        total = 0
        value = a
        for i in range(n):
                total = total + value
                value = value * r
        return total