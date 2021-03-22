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
    raise NotImplementedError


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    raise NotImplementedError


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    raise NotImplementedError

