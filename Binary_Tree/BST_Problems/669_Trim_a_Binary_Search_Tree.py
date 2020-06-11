class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        #base case：leaf node的child怎么trim都还是none
        if not root:
            return None
        #如果root的value都小于下限，那root即root的left subtree都要被去掉
        #直接把root的right child作为新的root，继续往下trim
        if root.val < L:
            root = root.right
            root = self.trimBST(root, L, R)
        #如果root的value正好等于下限，那root可以保留但是root的left subtree要去掉
        #继续检查并trim以root的right child为root的subtree
        elif root.val == L:
            root.left = None
            root.right = self.trimBST(root.right, L, R)
        #如果root在上下限之间，那么继续检查并trim以root的left及right child为root的subtrees
        elif root.val > L and root.val < R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        elif root.val == R:
            root.right = None
            root.left = self.trimBST(root.left, L, R)
        else:
            root = root.left
            root = self.trimBST(root, L, R)
        #改变结构的recusion要以node为纽带，return node
        return root
