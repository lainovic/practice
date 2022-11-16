import unittest

from src.tree_traversals import *
from src.tree import TreeNode


class TreeTraversalTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_tree_traversals(self):
        TREE_GRAPH = r"""
                    5
                    / \
                3   6
                / \
                2   4
                /
            1
            """

        root = TreeNode.deserialize("5,3,2,1,N,N,N,4,N,N,6,N,N")
        print(f"tree: {TREE_GRAPH}")

        print("\npreorder_recursive:")
        preorder_recursive(root, lambda x: print(x))

        print("\npreorder_iterative:")
        preorder_iterative(root, lambda x: print(x))

        print("\ninorder_recursive:")
        inorder_recursive(root, lambda x: print(x))

        print("\ninorder_iterative:")
        inorder_iterative(root, lambda x: print(x))

        print("\npostorder_recursive:")
        postorder_recursive(root, lambda x: print(x))

        print("\npostorder_iterative:")
        postorder_iterative(root, lambda x: print(x))

        print("\nlevelorder_recursive:")
        levelorder_recursive(root, lambda x: print(x))

        print("\nlevelorder_iterative:")
        levelorder_iterative(root, lambda x: print(x))


if __name__ == "__main__":
    unittest.main()
