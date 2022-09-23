from copy import deepcopy
import unittest

from tree import TreeNode


class TreeTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.root = TreeNode(5)
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(6)
        self.root.left.left = TreeNode(2)
        self.root.left.right = TreeNode(4)
        self.root.left.left.left = TreeNode(1)
        self.list = [5, 3, 6, 2, 4, None, None, 1]

    def test_serialization(self):
        self.assertEqual(TreeNode.deserialize(
            TreeNode.serialize(self.root)), self.root)

    def test_eq(self):
        self.assertEqual(self.root, self.root)

    def test_neq(self):
        self.assertNotEqual(self.root, None)
        foo = deepcopy(self.root)
        foo.left.left.left.right = TreeNode(17)
        self.assertNotEqual(self.root, foo)
        foo.left.left.left.right = None
        self.root.right.right = TreeNode(42)
        self.assertNotEqual(self.root, foo)


if __name__ == "__main__":
    unittest.main()
