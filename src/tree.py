from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_left(self, val):
        self.left = TreeNode(val)
        return self.left

    def add_right(self, val):
        self.right = TreeNode(val)
        return self.right

    def insert(self, val) -> None:
        print(f"-----> Inserting {val}...")
        curr = self
        while True:
            if val >= curr.val:
                if curr.right is None:
                    print(f"-----> Found it! Insert to right of {curr}.")
                    curr.right = TreeNode(val)
                    return
                print(f"-----> {val} >= {curr.val}, go right...")
                curr = curr.right
            elif val < curr.val:
                if curr.left is None:
                    print(f"-----> Found it! Insert to left of {curr}.")
                    curr.left = TreeNode(val)
                    return
                print(f"-----> {val} < {curr.val}, go left...")
                curr = curr.left

    def find(self, val) -> Optional["TreeNode"]:
        print(f"-----> Finding {val}...")
        curr = self
        while True:
            if val > curr.val:
                if curr.right is None:
                    print(
                        f"-----> {val} should've been placed right to {curr.val}, but wasn't found! Returning None.")
                    return None
                print(f"-----> {val} > {curr.val}, go right...")
                curr = curr.right
            elif val < curr.val:
                if curr.left is None:
                    print(
                        f"-----> {val} should've been placed left to {curr.val}, but wasn't found! Returning None.")
                    curr.left = TreeNode(val)
                    return
                print(f"-----> {val} < {curr.val}, go left...")
                curr = curr.left
            else:
                print(f"-----> Found it! Returning {curr}.")
                return curr

    def __str__(self) -> str:
        out = f"{self.val}"
        children = []
        if self.left:
            children.append(f"left: {self.left}")
        if self.right:
            children.append(f"right: {self.right}")
        out += " {" + ", ".join(children) + "}"
        return out

    def __eq__(self, other):
        def xor(a, b):
            return bool(a) != bool(b)

        if other is None:
            return False
        res = self.val == other.val
        if xor(self.left, other.left):
            return False
        res = res and self.left == other.left
        if xor(self.right, other.right):
            return False
        res = res and self.right == other.right
        return res

    @staticmethod
    def serialize(root: Optional["TreeNode"]) -> str:
        """
        Serialize the binary tree to an array that's stringified,
        with the order of elements corresponding to the DFS pre-order traversal.
        :return: A stringified array.
        """
        res = []

        def helper(node):
            res.append(str(node.val) if node else "N")
            if node:
                helper(node.left)
                helper(node.right)

        helper(root)
        return ",".join(res)

    @ staticmethod
    def deserialize(data: str) -> Optional["TreeNode"]:
        """
        Deserialize the tree that's previously serialized with :func:`~TreeNode.serialize` method.
        """
        if len(data) == 0:
            return None
        data = iter([int(i) if i != "N" else None for i in data.split(",")])

        def helper():
            val = next(data)
            if val is None:
                return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        return helper()
