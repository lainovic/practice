import unittest

from src.minheap import MinHeap


class MinHeapTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def insert_and_verify_min(self, mh, val_to_insert, val_to_verify):
        mh.insert(val_to_insert)
        self.assertEqual(mh.min(), val_to_verify)

    def test_extract_min(self):
        mh = MinHeap()
        mh.heapify([6, 3, 1, 2, 6, 7])
        self.assertEqual(mh.size(), 6)
        self.assertEqual(mh.extract_min(), 1)
        self.assertEqual(mh.size(), 5)
        self.assertEqual(mh.extract_min(), 2)
        self.assertEqual(mh.size(), 4)
        mh.insert(0)
        self.assertEqual(mh.extract_min(), 0)
        self.assertEqual(mh.size(), 4)
        mh.insert(5)
        self.assertEqual(mh.extract_min(), 3)
        self.assertEqual(mh.size(), 4)

    def test_min(self):
        mh = MinHeap()
        mh.heapify([0])
        self.insert_and_verify_min(mh, -1, -1)
        self.insert_and_verify_min(mh, 1, -1)
        self.insert_and_verify_min(mh, -2, -2)
        self.insert_and_verify_min(mh, -4, -4)
        self.insert_and_verify_min(mh, 3, -4)

        mh.heapify([])
        self.insert_and_verify_min(mh, -3, -3)
        self.insert_and_verify_min(mh, -2, -3)
        self.insert_and_verify_min(mh, -4, -4)
        self.insert_and_verify_min(mh, 0, -4)
        self.insert_and_verify_min(mh, 4, -4)

    def test_with_custom_predicate(self):
        mh = MinHeap()
        mh.heapify([(0, 9), (1, 8), (2, 7), (3, 7), (4, 6), (5, 12)],
                   less_than_predicate=lambda x, y: x[0] < y[0])
        self.assertFalse(mh.empty())
        self.assertEqual(mh.size(), 6)
        self.assertEqual(mh.extract_min(), (0, 9))
        self.assertEqual(mh.size(), 5)
        self.assertEqual(mh.extract_min(), (1, 8))
        self.assertEqual(mh.size(), 4)
        self.assertEqual(mh.extract_min(), (2, 7))
        self.assertEqual(mh.size(), 3)
        self.assertEqual(mh.extract_min(), (3, 7))
        self.assertEqual(mh.size(), 2)
        mh.insert((10, 10))
        self.assertEqual(mh.size(), 3)
        self.assertEqual(mh.extract_min(), (4, 6))
        self.assertEqual(mh.size(), 2)
        mh.insert((1, 1))
        self.assertEqual(mh.size(), 3)
        self.assertEqual(mh.extract_min(), (1, 1))
        self.assertEqual(mh.size(), 2)
        self.assertEqual(mh.extract_min(), (5, 12))
        self.assertEqual(mh.size(), 1)
        self.assertEqual(mh.extract_min(), (10, 10))
        self.assertTrue(mh.empty())


if __name__ == "__main__":
    unittest.main()
