#!/usr/bin/env python3
"""
`heaps` implementation

@author:
"""


from typing import Any, List


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self.heap: List[Any] = []
        self.size = 0

    def perc_up(self, cur_idx: int):
        """Move a node up"""
        """code from textbook"""
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def perc_down(self, cur_idx: int):
        """Move a node down"""
        """code from textbook"""
        while 2 * cur_idx + 1 < len(self._heap):
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = min_child_idx

    """code from textbook"""
    def _get_min_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def insert(self, item: Any):
        """Add a new item"""
        """code from textbook"""
        self._heap.append(item)
        self.perc_up(len(self._heap) - 1)

    def delete(self) -> Any:
        """Remove an item from the heap"""
        """code from textbook"""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self.perc_down(0)
        return result

    def heapify(self, not_a_heap: List[Any]) -> None:
        """Turn a list into a heap"""
        """code from textbook"""
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def __len__(self) -> int:
        """Get heap size"""
        return self.size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self.heap)
