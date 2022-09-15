from collections import deque
from turtle import right
from typing import List, Optional


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
    def serialize(root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            res.append(node.val if node else None)
            if node:
                q.append(node.left)
                q.append(node.right)
        last_idx = len(res) - 1
        while res[last_idx] is None:
            last_idx -= 1
        return res[: last_idx + 1]

    @staticmethod
    def deserialize(data: List[int]) -> Optional["TreeNode"]:
        if len(data) == 0:
            return None
        root = TreeNode(data[0])
        q = deque([root])
        i = 1
        while i < len(data):
            node = q.popleft()
            left_val = data[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                q.append(node.left)
            if i < len(data):
                right_val = data[i]
                i += 1
                if right_val is not None:
                    node.right = TreeNode(right_val)
                    q.append(node.right)
        return root
