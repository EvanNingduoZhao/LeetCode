#这基本是一个标准的inorder traversal
#对于BST而言，inorder traversal return的结果就是从小到大的
#这个code其实就是在94题标准的inorder traversal的基础上加了
def kthSmallest(self, root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return
        # the order of pop is the same as
        # BST order, so the first time will
        # pop the smallest element, and so on,
        # we track this pop operation, after k
        # times, we get the answer
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        root = node.right