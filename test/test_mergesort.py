import unittest

from src.sorts.mergesort import *


class MergeSortTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_sorts(self):
        for fn in [mergesort_top_bottom, mergesort_bottom_up]:
            self.assertEqual(fn([8, 9, 3]), [3, 8, 9])
            self.assertEqual(fn([5, 2, 3]), [2, 3, 5])
            self.assertEqual(fn([5, 5, 5]), [5, 5, 5])
            self.assertEqual(fn(
                [5, 6, 4, 2, 8, 9, 3]), [2, 3, 4, 5, 6, 8, 9])
            self.assertEqual(fn(
                [5, 6, 4, 3, 2, 1, 0]), [0, 1, 2, 3, 4, 5, 6])
            self.assertEqual(fn([1]), [1])
            self.assertEqual(fn([]), [])


if __name__ == "__main__":
    unittest.main()
