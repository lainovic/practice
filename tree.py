from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

    @staticmethod
    def from_list(values_list) -> Optional["TreeNode"]:
        if len(values_list) == 0:
            return None
        root = TreeNode(values_list[0])
        q = deque([root])
        i = 1
        while i < len(values_list):
            node = q.popleft()
            left_val = values_list[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                q.append(node.left)
            if i < len(values_list):
                right_val = values_list[i]
                i += 1
                if right_val is not None:
                    node.right = TreeNode(right_val)
                    q.append(node.right)
        return root

    @staticmethod
    def to_list(root):
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
