class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # we first determine the base case of our recursion
        # imagine a single node with its left and right children both as None
        # the tree consisted of this single node should be considered as balanced
        # so when root is None, base case should return True
        if root is None:
            return True
        else:
            heightdiff = self.height(root.left) - self.height(root.right)
            # if height diff's absolute value larger than 1, tree is imbalanced return False
            if heightdiff < -1 or heightdiff > 1:
                return False
            # if height diff's abs not larger than 1
            # this only proves that the height diff of the two children nodes at this level are within 1
            # 即这只说明 这两个node下面各自长的树枝长度差不超过1，
            # 但是可能一个长树枝的在某一个node开始的两个小树杈的长度差超过1
            else:
                # 所以开始recursion 一个level 一个level的查
                return self.isBalanced(root.left) and self.isBalanced(root.right)

    # this is a helper function to get the height of a node
    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))