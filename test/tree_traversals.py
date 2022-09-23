from src.tree import TreeNode


def preorder_recursive(node, fn):
    if not node:
        return
    fn(node.val)
    preorder_recursive(node.left, fn)
    preorder_recursive(node.right, fn)


def preorder_iterative(root, fn):
    stack = [root]
    while stack:
        node = stack.pop()
        fn(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def inorder_recursive(node, fn):
    if not node:
        return
    inorder_recursive(node.left, fn)
    fn(node.val)
    inorder_recursive(node.right, fn)


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


def postorder_recursive(node, fn):
    if not node:
        return
    postorder_recursive(node.left, fn)
    postorder_recursive(node.right, fn)
    fn(node.val)


def postorder_iterative(root, fn):
    stack = [root]
    while stack:
        node = stack.pop()
        fn(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


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


if __name__ == "__main__":
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
