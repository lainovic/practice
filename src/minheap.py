from copy import deepcopy
from typing import List, Callable, Optional, TypeVar
from operator import __lt__

T = TypeVar("T")


class MinHeap:
    def __init__(self, capacity: int = 1, less_than_predicate: Callable[[T, T], bool] = None) -> None:
        self.capacity = capacity
        self._size = 0  # just for practicing, not that it's needed with dynamic arrays
        self.list = [None] * self.capacity
        self.__lt__ = less_than_predicate if less_than_predicate is not None else __lt__

    def empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def heapify(self, values: List[T], less_than_predicate: Callable[[T, T], bool] = None) -> None:
        self.__lt__ = less_than_predicate if less_than_predicate is not None else __lt__
        if len(values) == 0:
            self.capacity = 1
        else:
            self.capacity = len(values)
        self.list = [None] * self.capacity
        self._size = 0
        for val in values:
            self.insert(val)

    def min(self) -> Optional[T]:
        if self.empty():
            return None
        return self.list[0]

    def extract_min(self) -> Optional[T]:
        if self.empty():
            return None
        res = self.list[0]
        self.list[0] = self.list[self._size - 1]
        self._size -= 1
        self._sift_down()
        return res

    def insert(self, value: T) -> None:
        self._ensure_extra_capacity()
        self.list[self._size] = value
        self._size += 1
        self._sift_up()

    def _has_left_child(self, parent_index: int) -> bool:
        return self._left_child_index(parent_index) < self._size

    def _left_child(self, parent_index: int) -> T:
        return self.list[self._left_child_index(parent_index)]

    @staticmethod
    def _left_child_index(parent_idx: int) -> int:
        return 2 * parent_idx + 1

    def _has_right_child(self, parent_index: int) -> bool:
        return self._right_child_index(parent_index) < self._size

    def right_child(self, parent_index: int) -> T:
        return self.list[self._right_child_index(parent_index)]

    @staticmethod
    def _right_child_index(parent_index: int) -> int:
        return MinHeap._left_child_index(parent_index) + 1

    @staticmethod
    def _has_parent(child_index: int) -> bool:
        return MinHeap._parent_idx(child_index) >= 0

    def _parent(self, child_index: int) -> T:
        return self.list[self._parent_idx(child_index)]

    @staticmethod
    def _parent_idx(child: int) -> int:
        return (child - 1) // 2

    def _swap(self, idx_1: int, idx_2: int) -> None:
        tmp = self.list[idx_1]
        self.list[idx_1] = self.list[idx_2]
        self.list[idx_2] = tmp

    def _ensure_extra_capacity(self) -> None:
        if self._size == self.capacity:
            self.capacity *= 2
            tmp = self.list
            self.list = [0] * self.capacity
            for i, e in enumerate(tmp):
                self.list[i] = deepcopy(e)

    def _sift_up(self) -> None:
        idx = self._size - 1
        while self._has_parent(idx) and self.__lt__(self.list[idx], self._parent(idx)):
            parent_idx = self._parent_idx(idx)
            self._swap(idx, parent_idx)
            idx = parent_idx

    def _sift_down(self) -> None:
        idx = 0
        while self._has_left_child(idx):
            smaller_child_idx = self._right_child_index(idx) \
                if self._has_right_child(idx) and self.__lt__(self.right_child(idx), self._left_child(idx)) \
                else self._left_child_index(idx)
            if self.__lt__(self.list[idx], self.list[smaller_child_idx]):
                break
            self._swap(smaller_child_idx, idx)
            idx = smaller_child_idx
