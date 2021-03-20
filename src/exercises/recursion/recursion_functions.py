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


def topDiamond_rec(exStarNum, curDuoLevels):
    while exStarNum < curDuoLevels:
        print('{:{align}{width}}'.format('*'*exStarNum, align='^', width=(curDuoLevels)))
        return topDiamond_rec(exStarNum+2, curDuoLevels)


# def botDiamond_rec(exStarNum, curDuoLevels):
#     while exStarNum > 0:
#         print('{:{align}{width}}'.format('*'*exStarNum, align='^', width=(curDuoLevels)))
#         return botDiamond_rec(exStarNum-2, curDuoLevels)


def diamond_rec(levels: int) -> None:
    """Print a diamond"""
    curDuoLevels = 2 * levels - 1
    exStarNum = 1
    return topDiamond_rec(exStarNum, curDuoLevels)
        


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
