class Solution:
    #这是自己写的DFS的做法 关于DFS和BFS是什么区别以后学到了再补上
    #这个方法其实就是preorder遍历，每access到一个node就把它的左右child调换
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                temp=node.left
                node.left=node.right
                node.right=temp
                stack.append(node.right)
                stack.append(node.left)
        return root

    # recursively
    def invertTree1(self, root):
        if not root:
            return None
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root