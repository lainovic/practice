from typing import Callable, List, TypeVar
from src.minheap import MinHeap
from operator import __ge__

T = TypeVar("T")


class MaxHeap:
    def __init__(self,
                 capacity: int = 1,
                 less_than_predicate: Callable[[
                     T, T], bool] = None,
                 negative: Callable[[T], T] = None) -> None:
        """
        :note: in case of user-derived values, users must provide the operator on how to negate the value.
        Leaky abstractions, I know, I know...
        """
        self.negation_op = negative if negative else lambda x: (-1) * x
        self.minheap = MinHeap(capacity, less_than_predicate)

    def empty(self) -> bool:
        return self.minheap.empty()

    def size(self) -> int:
        return self.minheap.size()

    def heapify(self,
                values: List[T],
                less_than_predicate: Callable[[T, T], bool] = None, negative: Callable[[T], T] = None) -> None:
        """
        :note: in case of user-derived values, users must provide the operator on how to negate the value.
        Leaky abstractions, I know, I know...
        """
        if negative:
            self.negation_op = negative
        for i in range(len(values)):
            values[i] = self.negation_op(values[i])
        self.minheap.heapify(values, less_than_predicate)

    def max(self) -> T:
        return self.negation_op(self.minheap.min())

    def extract_max(self) -> T:
        return self.negation_op(self.minheap.extract_min())

    def insert(self, value: T) -> None:
        self.minheap.insert(self.negation_op(value))
