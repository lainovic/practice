from collections import deque


def preorder_recursive(node, fn):
    if not node:
        return
    fn(node.val)
    preorder_recursive(node.left, fn)
    preorder_recursive(node.right, fn)


def inorder_recursive(node, fn):
    if not node:
        return
    inorder_recursive(node.left, fn)
    fn(node.val)
    inorder_recursive(node.right, fn)


def postorder_recursive(node, fn):
    if not node:
        return
    postorder_recursive(node.left, fn)
    postorder_recursive(node.right, fn)
    fn(node.val)


def levelorder_recursive(root, fn):
    h = root.height()
    for i in range(h + 1):
        for val in root.get_values_at_distance(i):
            fn(val)


def preorder_iterative(root, fn):
    stack = [root]
    while stack:
        node = stack.pop()
        fn(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def inorder_iterative(root, fn):
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        fn(curr.val)
        curr = curr.right


def postorder_iterative(root, fn):
    stack = []
    curr = root
    prev = None
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if curr.right is None or prev == curr.right:
            fn(curr.val)
            prev = curr
            curr = None
        else:
            stack.append(curr)
            curr = curr.right


def levelorder_iterative(root, fn):
    q = deque([root])
    while q:
        lenq = len(q)
        for _ in range(lenq):
            node = q.popleft()
            fn(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
