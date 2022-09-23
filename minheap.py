from copy import deepcopy


class MinHeap:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0  # just for practicing, not that it's needed with dynamic arrays as in here in Python
        self.list = [0] * self.capacity

    def empty(self):
        return self.size == 0

    def heapify(self, nums):
        if len(nums) == 0:
            self.capacity = 1
        else:
            self.capacity = len(nums)
        self.list = [0] * self.capacity
        self.size = 0
        for num in nums:
            self.insert(num)

    def min(self):
        if self.empty():
            return None
        return self.list[0]

    def extract_min(self):
        if self.empty():
            return None
        res = self.list[0]
        self.list[0] = self.list[self.size - 1]
        self.size -= 1
        self._sift_down()
        return res

    def remove_last(self):
        res = self.list[-1]
        self.size -= 1
        return res

    def insert(self, value):
        self._ensure_extra_capacity()
        self.list[self.size] = value
        self.size += 1
        self._sift_up()

    def _has_left_child(self, index):
        return self._left_child_index(index) < self.size

    def _left_child(self, index):
        return self.list[self._left_child_index(index)]

    @staticmethod
    def _left_child_index(parent):
        return 2 * parent + 1

    def _has_right_child(self, index):
        return self._right_child_index(index) < self.size

    def right_child(self, index):
        return self.list[self._right_child_index(index)]

    @staticmethod
    def _right_child_index(parent):
        return MinHeap._left_child_index(parent) + 1

    @staticmethod
    def _has_parent(index):
        return MinHeap._parent_idx(index) >= 0

    def _parent(self, index):
        return self.list[self._parent_idx(index)]

    @staticmethod
    def _parent_idx(child):
        return (child - 1) // 2

    def _swap(self, idx_1, idx_2):
        tmp = self.list[idx_1]
        self.list[idx_1] = self.list[idx_2]
        self.list[idx_2] = tmp

    def _ensure_extra_capacity(self):
        if self.size == self.capacity:
            self.capacity *= 2
            tmp = self.list
            self.list = [0] * self.capacity
            for i, e in enumerate(tmp):
                self.list[i] = deepcopy(e)

    def _sift_up(self):
        idx = self.size - 1
        while self._has_parent(idx) and self._parent(idx) > self.list[idx]:
            parent_idx = self._parent_idx(idx)
            self._swap(idx, parent_idx)
            idx = parent_idx

    def _sift_down(self):
        idx = 0
        while self._has_left_child(idx):
            smaller_child_idx = self._right_child_index(idx) \
                if self._has_right_child(idx) and self.right_child(idx) < self._left_child(idx) \
                else self._left_child_index(idx)
            if self.list[idx] <= self.list[smaller_child_idx]:
                break
            self._swap(smaller_child_idx, idx)
            idx = smaller_child_idx
