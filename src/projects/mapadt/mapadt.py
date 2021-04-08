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
        
        if not None in self._keys and key not in self._keys:
            raise MemoryError("Hash Table is full")

        hash_value = self._hash(key)
        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = value
        
        else:
            original_hash = hash_value
            count = 1
            while self._keys[hash_value] is not None and self._keys[hash_value] != key:
                hash_value = self._rehash(original_hash, count)
                count +=1
            if key not in self._keys and self._keys[hash_value] is None:
                self._keys[hash_value] = key
                self._values[hash_value] = value
            else:
                self._values[hash_value] = value

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
        """code from textbook"""
        start_slot = self._hash(key)

        position = start_slot
        while self._keys[position] is not None:
            if self._keys[position] == key:
                return self._values[position]
            else:
                position = self._rehash(position)
                if position == start_slot:
                    return None

    def __len__(self) -> int:
        """
        Map size

        @return a number of key-value pairs stored in the collection
        """
        return len(self.keys())

    def __contains__(self, key: int) -> bool:
        """
        key in HashMap

        Check if the key is in the collection
        @param key: key of an item in the collection
        @return True if the key is found, False otherwise
        """
        if key in self._keys:
            return True
        return False

    def __str__(self) -> str:
        """
        String representation of the collection

        @return collections as a string
        """
        strDict = {}
        kList = self.keys()
        vList = self.values()
        for index1 in range(len(kList)):
            strDict[kList[index1]] = vList[index1]
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
        return (old_hash+(step*step))%self._size

    def keys(self) -> List[int]:
        """
        Keys in the collection

        @return all keys
        """
        kList = []
        for index1 in self._keys:
            if index1 != None:
                kList.append(index1)
        return kList

    def values(self) -> List[Any]:
        """
        Values in the collection

        @return all values
        """
        vList = []
        for index2 in self._values:
            if index2 != None:
                vList.append(index2)
        return vList

    def items(self) -> List[Tuple[int, Any]]:
        """
        Items (key: value) in the collections

        @return all items
        """
        tupList = []
        kList = self.keys()
        vList = self.values()
        for index1 in range(len(kList)):
            tupList.append((kList[index1], vList[index1]))
        return tupList
