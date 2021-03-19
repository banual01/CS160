#!/usr/bin/env python3
"""
`recursion` implementation

@author:
"""


def gcd(a: int, b: int) -> int:
    """Greatest Common Denominator"""
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def diamond_ite(levels: int) -> None:
    """Print a diamond"""
    duoStarNum= 1
    duoLevels = 2 * levels - 1
    while duoStarNum < duoLevels:
        print('{:{align}{width}}'.format('*'*duoStarNum, align='^', width=(duoLevels)))
        duoStarNum += 2
    while duoStarNum > 0:
        print('{:{align}{width}}'.format('*'*duoStarNum, align='^', width=(duoLevels)))
        duoStarNum -= 2 


def diamond_rec(levels: int) -> None:
    """Print a diamond"""
    raise NotImplementedError


def hourglass_ite(levels: int) -> None:
    """Print an hourglass"""
    duoStarNum= 2 * levels - 1
    duoLevels = 2 * levels - 1
    while duoStarNum > 1:
        print('{:{align}{width}}'.format('*'*duoStarNum, align='^', width=(duoLevels)))
        duoStarNum -= 2 
    while duoStarNum <= duoLevels:
        print('{:{align}{width}}'.format('*'*duoStarNum, align='^', width=(duoLevels)))
        duoStarNum += 2


def hourglass_rec(levels: int) -> None:
    """Print an hourglass"""
    raise NotImplementedError
