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


if __name__ == "__main__":
    unittest.main()
