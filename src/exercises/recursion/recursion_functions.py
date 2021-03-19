#!/usr/bin/env python3
"""
`recursion` implementation

@author:
"""


def gcd(a: int, b: int) -> int:
    """Greatest Common Denominator"""
    while a % b:
        a, b = b, a % b
    return b


def diamond_ite(levels: int) -> None:
    """Print a diamond"""
    for level in levels:

        raise NotImplementedError 


def diamond_rec(levels: int) -> None:
    """Print a diamond"""
    raise NotImplementedError


def hourglass_ite(levels: int) -> None:
    """Print an hourglass"""
    for level in levels:
        raise NotImplementedError 


def hourglass_rec(levels: int) -> None:
    """Print an hourglass"""
    raise NotImplementedError
