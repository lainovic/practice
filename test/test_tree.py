from copy import deepcopy
import unittest

from src.tree import TreeNode


class TreeTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_serialization(self):
        r = TreeNode(5)
        r.add_left(3)
        r.add_right(6)
        r.left.add_left(2).add_left(1)
        r.left.add_right(4)
        self.assertEqual(TreeNode.deserialize(
            TreeNode.serialize(r)), r)

    def test_eq(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        self.assertEqual(r, r)
        cpy = deepcopy(r)
        self.assertEqual(r, cpy)

    def test_neq(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        self.assertNotEqual(r, None)
        cpy = deepcopy(r)
        cpy.right.right = TreeNode(17)
        self.assertNotEqual(r, cpy)
        cpy.right.right = None
        r.right.right = TreeNode(42)
        self.assertNotEqual(r, cpy)

    def test_get_values_at_distance(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        self.assertEqual(r.get_values_at_distance(0), [1])
        self.assertEqual(r.get_values_at_distance(1), [10])
        self.assertEqual(r.get_values_at_distance(2), [5, 20])
        self.assertEqual(r.get_values_at_distance(3), [])

    def test_size(self):
        r = TreeNode(1)
        self.assertEqual(r.size(), 1)
        r.add_right(10)
        self.assertEqual(r.size(), 2)
        r.right.add_left(5)
        r.right.add_right(20)
        self.assertEqual(r.size(), 4)
        r.right.right = None
        self.assertEqual(r.size(), 3)

    def test_count_leaves(self):
        r = TreeNode(1)
        self.assertEqual(r.count_leaves(), 1)
        r.add_right(10)
        self.assertEqual(r.count_leaves(), 1)
        r.right.add_left(5)
        r.right.add_right(20)
        self.assertEqual(r.count_leaves(), 2)
        r.right.right = None
        self.assertEqual(r.count_leaves(), 1)

    def test_is_valid(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)
        self.assertTrue(r.is_valid())
        r.right.left.add_left(15)
        self.assertFalse(r.is_valid())

    def test_insert(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        r.insert(2)
        self.assertEqual(2, r.right.left.left.val)
        r.insert(3)
        self.assertEqual(3, r.right.left.left.right.val)
        r.insert(12)
        self.assertEqual(12, r.right.right.left.val)
        r.insert(26)
        self.assertEqual(26, r.right.right.right.val)
        r.insert(7)
        self.assertEqual(7, r.right.left.right.val)

    def test_find(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        self.assertTrue(r.find(1) is not None)
        self.assertTrue(r.find(10) is not None)
        self.assertTrue(r.find(5) is not None)
        self.assertTrue(r.find(20) is not None)

        self.assertEqual(None, r.find(3))
        self.assertEqual(None, r.find(12))
        self.assertEqual(None, r.find(26))
        self.assertEqual(None, r.find(7))

    def test_contains(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        self.assertTrue(1 in r)
        self.assertTrue(10 in r)
        self.assertTrue(5 in r)
        self.assertTrue(20 in r)

        self.assertFalse(3 in r)
        self.assertFalse(12 in r)
        self.assertFalse(26 in r)
        self.assertFalse(7 in r)

    def test_height(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        self.assertEqual(2, r.height())

    def test_min(self):
        r = TreeNode(1)
        r.add_right(10)
        r.right.add_left(5)
        r.right.add_right(20)

        self.assertEqual(1, r.min())
        self.assertEqual(1, r.min_bst())
        self.assertEqual(5, r.right.left.min())
        self.assertEqual(5, r.right.left.min_bst())

    def test_siblings(self):
        r = TreeNode(1)
        r.add_left(5).add_left(7)
        r.add_right(6).add_right(4)
        r.right.add_left(3)

        self.assertTrue(r.are_siblings(5, 6))
        self.assertTrue(r.are_siblings(4, 3))
        self.assertFalse(r.are_siblings(4, 6))
        self.assertFalse(r.are_siblings(6, 7))

    def test_get_ancestors(self):
        r = TreeNode(1)
        r.add_left(2).add_left(4).add_left(7)
        r.add_right(3)
        r.left.add_right(5)

        self.assertEqual(r.get_ancestors(7), [1, 2, 4])
        self.assertEqual(r.get_ancestors(5), [1, 2])
        self.assertEqual(r.get_ancestors(3), [1])
        self.assertEqual(r.get_ancestors(1), [])
        self.assertEqual(r.get_ancestors(None), [])

    def test_max(self):
        r = TreeNode(1)
        self.assertEqual(r.max(), 1)
        r.add_right(10)
        self.assertEqual(r.max(), 10)
        r.right.add_left(5)
        r.right.add_right(20)
        self.assertEqual(r.max(), 20)
        r.right.right = None
        self.assertEqual(r.max(), 10)


if __name__ == "__main__":
    unittest.main()
