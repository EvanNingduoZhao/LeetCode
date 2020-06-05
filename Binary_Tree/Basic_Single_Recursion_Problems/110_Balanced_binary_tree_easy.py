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


#这是在上面的方法的基础上，加一个dict存起来已经见过的node的height，这样recursive call的时候
#对于见过的就不用再算了，直接在dict里找就可以了
class Solution:
    #这里直接把depth_dict这个dict作为一个attribute加到Solution这个object里
    def __init__(self):
        self.depth_dict = {}

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            heightdiff = self.depth(root.left) - self.depth(root.right)
            if heightdiff < -1 or heightdiff > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        else:
            if root in self.depth_dict:
                return self.depth_dict[root]
            else:
                self.depth_dict[root] = 1 + max(self.depth(root.left), self.depth(root.right))
                return self.depth_dict[root]