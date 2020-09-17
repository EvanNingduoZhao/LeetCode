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


#上面的第一种方法之所以需要把一个node的height算好几次，是因为第一种方法的recursion是top down的
# 在每次recursive call中，我们都是先算自己的两个children的height
#是不是balanced的（这就需要把目前所在的root下面的所有node的height算一遍），再算自己的两个children各自的两个children的height是不是
#balanced（这个过程中又得把自己的两个children下面的所有node的height算一遍，由此造成了重复计算）实际上，我们其实不需要加一个dict
#来存已经算好的node的height，只需要把我们的recursion改成bottom up的即可，即先看自己的两个children的两个children的height是不是
#balanced，在这个过程中我们就算出来了自己的两个children的height，那么我们就可以直接根据自己的两个children的height来算出
#自己的两个chidlren是不是balanced，并算出来自己的height，具体见下面的code：
    class Solution:
        # Return whether or not the tree at root is balanced while also returning
        # the tree's height
        def isBalancedHelper(self, root: TreeNode) -> (bool, int):
            # An empty tree is balanced and has height -1
            if not root:
                return True, -1

            # Check subtrees to see if they are balanced.
            leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
            if not leftIsBalanced:
                return False, 0
            rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
            if not rightIsBalanced:
                return False, 0

            # If the subtrees are balanced, check if the current tree is balanced
            # using their height
            return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

        def isBalanced(self, root: TreeNode) -> bool:
            return self.isBalancedHelper(root)[0]