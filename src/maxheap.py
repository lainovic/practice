from src.minheap import MinHeap


class MaxHeap:
    def __init__(self):
        self.minheap = MinHeap()

    def empty(self):
        return self.minheap.empty()

    def size(self):
        return self.minheap.size()

    def heapify(self, nums):
        for i in range(len(nums)):
            nums[i] = (-1) * nums[i]
        self.minheap.heapify(nums)

    def max(self):
        return (-1) * self.minheap.min()

    def extract_max(self):
        return (-1) * self.minheap.extract_min()

    def insert(self, value):
        self.minheap.insert((-1) * value)
