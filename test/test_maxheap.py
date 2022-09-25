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

    def test_with_custom_predicate(self):
        mh = MaxHeap()
        mh.heapify([(0, 9), (1, 8), (2, 7), (3, 7), (4, 6), (5, 12)],
                   greater_than_or_equal_predicate=lambda x, y: x[0] >= y[0],
                   negative=lambda x : ((-1) * x[0], x[1]))
        self.assertFalse(mh.empty())
        self.assertEqual(mh.size(), 6)
        self.assertEqual(mh.extract_max(), (5, 12))
        self.assertEqual(mh.size(), 5)
        self.assertEqual(mh.extract_max(), (4, 6))
        self.assertEqual(mh.size(), 4)
        self.assertEqual(mh.extract_max(), (3, 7))
        self.assertEqual(mh.size(), 3)
        self.assertEqual(mh.extract_max(), (2, 7))
        self.assertEqual(mh.size(), 2)
        mh.insert((10, 10))
        self.assertEqual(mh.size(), 3)
        self.assertEqual(mh.extract_max(), (10, 10))
        self.assertEqual(mh.size(), 2)
        mh.insert((1, 1))
        self.assertEqual(mh.size(), 3)
        self.assertEqual(mh.extract_max(), (1, 8))
        self.assertEqual(mh.size(), 2)
        self.assertEqual(mh.extract_max(), (1, 1))
        self.assertEqual(mh.size(), 1)
        self.assertEqual(mh.extract_max(), (0, 9))
        self.assertTrue(mh.empty())


if __name__ == "__main__":
    unittest.main()
