#!/usr/bin/env python3
"""
`mapadt` implementation

@author:
"""


from typing import Any, List, Tuple


class HashMap:
    """Class HashMap"""

    def __init__(self, size_init: int = 16):
        """
        Initialize HashTable

        @param size_init: size of the map
        """
        self._size: int = size_init
        self._keys: List = [None] * self._size
        self._values: List = [None] * self._size

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Setter

        @param key: key of the item in the collection
        @param value: new value to be added to (updated in) the collection
        """
        self.put(key, value)

    def put(self, key: int, value: Any) -> None:
        """
        Setter

        @param key: key of the item in the collection
        @param value: new value to be added to (updated in) the collection
        """
        """code from textbook"""
        
        hash_value = self._hash(key)

        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = value
        else:
            if self._keys[hash_value] == key:
                self._values[hash_value] = value  # replace
            else:
                next_slot = self._rehash(hash_value)
                while (
                    self._keys[next_slot] is not None
                    and self._keys[next_slot] != key
                ):
                    next_slot = self._rehash(next_slot)

                if self._keys[next_slot] is None:
                    self._keys[next_slot] = key
                    self._values[next_slot] = value
                else:
                    self._values[next_slot] = value

    def __getitem__(self, key: int) -> Any:
        """
        Getter

        @param key: key of the new item in the collection
        """
        return self.get(key)

    def get(self, key: int) -> Any:
        """
        Getter

        @param key: key of the new item in the collection
        """
        return self._keys

    def __len__(self) -> int:
        """
        Map size

        @return a number of key-value pairs stored in the collection
        """
        if None in self._keys:
            return 0
        return self._size

    def __contains__(self, key: int) -> bool:
        """
        key in HashMap

        Check if the key is in the collection
        @param key: key of an item in the collection
        @return True if the key is found, False otherwise
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        String representation of the collection

        @return collections as a string
        """
        strDict = {}
        for index1 in self._keys:
            for index2 in self._values:
                if index1 == index2:
                    strDict[index1] = index2
        if None in strDict:
            return "{}"
        return f"{strDict}"

    def _hash(self, key: int) -> int:
        """
        Hash function

        Simple remainder
        @param key: key of an element
        """
        return key%self._size

    def _rehash(self, old_hash: int, step: int = 1) -> int:
        """
        Rehash function

        Use quadratic probing
        @param old_hash: old hash value
        @param step: step (1 by default)
        @return new hash
        """
        return (old_hash+step)%self._size

    def keys(self) -> List[int]:
        """
        Keys in the collection

        @return all keys
        """
        if None in self._keys:
            return []        
        return self._keys

    def values(self) -> List[Any]:
        """
        Values in the collection

        @return all values
        """
        if None in self._values:
            return []
        return self._values

    def items(self) -> List[Tuple[int, Any]]:
        """
        Items (key: value) in the collections

        @return all items
        """
        tupList = []
        for index1 in self._keys:
            for index2 in self._values:
                if index1 == index2:
                    tupList.append((index1, index2))
        if index1 == None and index2 == None:
            return []
        return f"{tupList}"