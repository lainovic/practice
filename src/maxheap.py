from typing import Callable, TypeVar
from src.minheap import MinHeap
from operator import __ge__

T = TypeVar("T")


class MaxHeap:
    def __init__(self, capacity: int = 1, greater_than_or_equal_predicate: Callable[[T, T], bool] = None, negative: Callable[[T], T]=None) -> None:
        """
        :note: in case of user-derived values, users must provide the callback for negating the values. Leaky abstractions, I know...
        """
        less_than_predicate = None
        if greater_than_or_equal_predicate is not None:
            less_than_predicate = lambda x, y: not greater_than_or_equal_predicate(x, y)
        self.negation_op = negative if negative is not None else lambda x: self.negation_op(x)
        self.minheap = MinHeap(capacity, less_than_predicate)

    def empty(self) -> bool:
        return self.minheap.empty()

    def size(self) -> int:
        return self.minheap.size()

    def heapify(self, values, greater_than_or_equal_predicate: Callable[[T, T], bool] = None, negative: Callable[[T], T]=None) -> None:
        """
        :note: in case of user-derived values, users must provide the callback for negating the values. Leaky abstractions, I know...
        """
        less_than_predicate = None
        if greater_than_or_equal_predicate is not None:
            less_than_predicate = lambda x, y: not greater_than_or_equal_predicate(x, y)
        self.negation_op = negative if negative is not None else lambda x: (-1) * x
        for i in range(len(values)):
            values[i] = self.negation_op(values[i])
        self.minheap.heapify(values, less_than_predicate)

    def max(self) -> T:
        return self.negation_op(self.minheap.min())

    def extract_max(self) -> T:
        return self.negation_op(self.minheap.extract_min())

    def insert(self, value: T) -> None:
        self.minheap.insert(self.negation_op(value))
