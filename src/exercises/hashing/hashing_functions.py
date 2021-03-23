#!/usr/bin/env python3
"""
Exercise `hashing` implementation

@author:
"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key%size


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    
    squared = key * key
    string = str(squared)
    if len(string)%2 != 0:
        return int(string[int(len(string)/2-1.5):int((len(string)/2)+0.5)])%size
    else:
        return int(string[int(len(string)/2-1):int((len(string)/2)+1)])%size


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    keyList = []
    num = 0
    for index in key:
        if len(key) == num:
            num = 0
        if key[num] == "-":
            num += 1
        if num < len(key):
            keyList.append(key[num])
        num += 1
    keyList.pop()
    keyList.pop()
    num2 = 0
    total = 0
    for index in keyList:
        if num2%2 != 0:
            total += int(keyList[num2-1] + keyList[num2])
        num2 +=1
    return total%size
        
        


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    print(key)
    total = 0
    for index in key:
        total += ord(index)
    return total%size


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    raise NotImplementedError

