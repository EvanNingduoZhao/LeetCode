# inorder 是left nodeitself right
# 那么我们return的结果里的第一个应该的这个tree的最下层的最左面的那个


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while True:
            #先左边
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            #node自己
            node = stack.pop()
            res.append(node.val)
            #在看这个node的right child，有可能这个node的right child是None
            #但即将开始的while loop的下一个iteration的开头 如果现在的root是none的话就不会执行内层while 直接pop stack
            #里的下一个
            root = node.right
        return res