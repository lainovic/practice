from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

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
        res = []

        def helper(node):
            res.append(str(node.val) if node else "N")
            if node:
                helper(node.left)
                helper(node.right)

        helper(root)
        return ",".join(res)

    @staticmethod
    def deserialize(data: str) -> Optional["TreeNode"]:
        if len(data) == 0:
            return None
        data = [int(i) if i != "N" else None for i in data.split(",")]
        idx = 0

        def helper():
            nonlocal idx
            val = data[idx]
            idx += 1
            if val is None:
                return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        return helper()
