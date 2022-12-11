import math
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
        new_node = TreeNode(val)
        curr = self
        while True:
            if val >= curr.val:
                if curr.right is None:
                    print(f"-----> Insert to right of {curr}.")
                    curr.right = new_node
                    return
                print(f"-----> {val} >= {curr.val}, go right...")
                curr = curr.right
            elif val < curr.val:
                if curr.left is None:
                    print(f"-----> Insert to left of {curr}.")
                    curr.left = new_node
                    return
                print(f"-----> {val} < {curr.val}, go left...")
                curr = curr.left

    def find(self, val) -> Optional["TreeNode"]:
        print(f"-----> Finding {val}...")
        curr = self
        while curr is not None:
            if val > curr.val:
                print(f"-----> {val} > {curr.val}, go right...")
                curr = curr.right
            elif val < curr.val:
                print(f"-----> {val} < {curr.val}, go left...")
                curr = curr.left
            else:
                print(
                    f"-----> Found it. Returning the object {curr}.")
                return curr
        print(f"-----> {val} wasn't found. Returning None.")
        return None

    def size(self):
        res = 0

        def helper(node):
            if node is None:
                return
            nonlocal res
            res += 1
            helper(node.left)
            helper(node.right)

        helper(self)
        return res

    def count_leaves(self):
        res = 0

        def helper(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                nonlocal res
                res += 1
                return
            helper(node.left)
            helper(node.right)

        helper(self)
        return res

    def height(self) -> int:
        def helper(node):
            if node is None:
                print(f"-----> height(None) -> -1")
                return -1
            res = 1 + max(helper(node.left), helper(node.right))
            print(
                f"-----> height({node}) -> {res}")
            return res
        print(f"-----> Finding the height of {self}...")
        return helper(self)

    def max(self):
        res = -math.inf

        def helper(node):
            if node is None:
                return
            nonlocal res
            res = max(res, node.val)
            helper(node.left)
            helper(node.right)

        helper(self)
        return res

    def min(self) -> Optional[int]:
        def helper(node):
            if node is None:
                print(f"-----> min(None) -> Inf")
                return math.inf
            res = min(node.val, helper(node.left), helper(node.right))
            print(
                f"-----> min({node}) -> {res}")
            return res
        print(f"-----> Finding the min starting from {self}...")
        return helper(self)

    def min_bst(self) -> int:
        print(f"-----> Finding the height of BST {self}...")
        curr = self
        while curr is not None:
            if curr.left is None:
                print(f"-----> Found the leftmost node => min -> {curr.val}")
                return curr.val
            curr = curr.left

    def are_siblings(self, val_a, val_b):
        if self.left and self.right:
            print(
                f"-----> Checking if {val_a} and {val_b} are siblings under '{self}'...")
            if self.left.val == val_a and self.right.val == val_b or\
                    self.left.val == val_b and self.right.val == val_a:
                print(
                    f"-----> Yep.")
                return True
        res = False
        if self.left:
            print(f"-----> Going left from '{self}'...")
            res = res or self.left.are_siblings(val_a, val_b)
        if self.right:
            print(f"-----> Going right from '{self}'...")
            res = res or self.right.are_siblings(val_a, val_b)
        if res is False:
            print(f"-----> Nope, not under '{self}'.")
        return res

    def get_ancestors(self, target):
        res = []

        def helper(node):
            if node is None:
                print(f"-----> Dead end, going back.")
                return False
            if node.val == target:
                print(f"-----> Found {target}, the ancestors are: {res}.")
                return True
            print(f"-----> Adding {node.val}.")
            res.append(node.val)
            print(f"-----> Going left from {node.val}...")
            if helper(node.left):
                return True
            print(f"-----> Going right from {node.val}...")
            if helper(node.right):
                return True
            print(f"-----> Removing {node.val}.")
            res.pop()
            return False

        if target is None:
            print(f"-----> Given invalid target {target}, returning {res}.")
            return res
        print(f"-----> Finding ancestors of {target}...")
        helper(self)
        return res

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
        if other is None:
            return False
        return self.val == other.val \
            and self.left == other.left \
            and self.right == other.right

    def __contains__(self, val) -> bool:
        print(f"-----> Checking if '{self}' contains {val}.")
        if self.val == val:
            print(f"-----> Found {val}.")
            return True
        res = False
        if self.left:
            print(f"-----> Going left from '{self}'...")
            res = res or self.left.__contains__(val)
        if self.right:
            print(f"-----> Going right from '{self}'...")
            res = res or self.right.__contains__(val)
        if res is False:
            print(f"-----> {val} not found.")
        return res

    def get_values_at_distance(self, k):
        res = []

        def helper(node, dist):
            if node is None:
                return
            if dist <= 0:
                res.append(node.val)
                return
            helper(node.left, dist - 1)
            helper(node.right, dist - 1)

        helper(self, k)
        return res

    def is_valid(self):
        def is_within(left_val, node, right_val):
            if node is None:
                return True
            return left_val <= node.val <= right_val and \
                is_within(left_val, node.left, node.val) and \
                is_within(node.val, node.right, right_val)

        return is_within(-math.inf, self, math.inf)

        # brute force 1:
        # def less_than(node, val):
        #     if node is None:
        #         return True
        #     return val <= node.val and less_than(node.left, val) and less_than(node.right, val)
        # def greater_than(node, val):
        #     if node is None:
        #         return True
        #     return val >= node.val and greater_than(node.left, val) and greater_than(node.right, val)
        # def valid(node):
        #     if node is None:
        #         return True
        #     return greater_than(node.left, node.val) and less_than(node.right, node.val) and \
        #         valid(node.left) and valid(node.right)
        # return valid(self)

        # brute force 2:
        # def find_min(node):
        #     if node.left is None:
        #         return node.val
        #     return find_min(node.left)
        # def find_max(node):
        #     while node.right is not None:
        #         node = node.right
        #     return node.val
        # def helper(node):
        #     if node is None:
        #         return True
        #     if node.left and find_max(node.left) > node.val:
        #         return False
        #     if node.right and find_min(node.right) < node.val:
        #         return False
        #     return helper(node.left) and helper(node.right)
        # return helper(self)

        # brute force 3:
        # arr = []

        # def helper(node):
        #     if node is None:
        #         return
        #     if helper(node.left) is False:
        #         return False
        #     if len(arr) > 0 and arr[-1] > node.val:
        #         return False
        #     arr.append(node.val)
        #     if helper(node.right) is False:
        #         return False
        #     return True

        return helper(self)

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
