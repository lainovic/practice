import unittest

from src.maxheap import MaxHeap

class MaxHeapTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def insert_and_verify_max(self, mh, val_to_insert, val_to_verify):
        mh.insert(val_to_insert)
        self.assertEqual(mh.max(), val_to_verify)

    def test_extract_max(self):
        mh = MaxHeap()
        mh.heapify([6, 3, 1, 2, 6, 7])
        self.assertEqual(mh.size(), 6)
        self.assertEqual(mh.extract_max(), 7)
        self.assertEqual(mh.size(), 5)
        self.assertEqual(mh.extract_max(), 6)
        self.assertEqual(mh.size(), 4)
        mh.insert(0)
        self.assertEqual(mh.extract_max(), 6)
        self.assertEqual(mh.size(), 4)
        mh.insert(15)
        self.assertEqual(mh.extract_max(), 15)
        self.assertEqual(mh.size(), 4)

    def test_max(self):
        mh = MaxHeap()
        mh.heapify([0])
        self.insert_and_verify_max(mh, -1, 0)
        self.insert_and_verify_max(mh, 1, 1)
        self.insert_and_verify_max(mh, -2, 1)
        self.insert_and_verify_max(mh, -4, 1)
        self.insert_and_verify_max(mh, 3, 3)

        mh.heapify([])
        self.insert_and_verify_max(mh, -3, -3)
        self.insert_and_verify_max(mh, -2, -2)
        self.insert_and_verify_max(mh, -4, -2)
        self.insert_and_verify_max(mh, 0, 0)
        self.insert_and_verify_max(mh, 4, 4)


if __name__ == "__main__":
    unittest.main()
