# 这道题其实就是用recursive implementation 求 tree height
class Solution:
    # my answer
    def maxDepth(self, root: TreeNode) -> int:
        #因为题中的规定相当于是leaf node的height = 1
        if root is None:
            return 0
        else:
            return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))

    # answer found in discussion
    # this is just a preorder traversal that also records the level of the node (root is level 0, 依次递增)
    def maxDepth_iterative_with_stack(self, root):
        res = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            # 每次碰到node是None的时候 都是因为这个Node的parent是一个leaf node
            # 即每次到底的时候都把这个底的level和目前level最高的底的level比一下
            # 注意因为root的level 是0 所以从node到leafnode所经过的node数量应该等于leafnode的children的level
            if not node:
                res = max(res, level)
            else:
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res