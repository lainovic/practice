import unittest

from tree import TreeNode


class TestTree(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.root = TreeNode(5)
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(6)
        self.root.left.left = TreeNode(2)
        self.root.left.right = TreeNode(4)
        self.root.left.left.left = TreeNode(1)
        self.list = [5, 3, 6, 2, 4, None, None, 1]

    def test_fromlist(self):
        self.assertEqual(TreeNode.from_list(self.list), self.root)

    def test_tolist(self):
        self.assertEqual(TreeNode.to_list(self.root), self.list)


if __name__ == "__main__":
    unittest.main()
