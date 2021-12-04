# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 用dfs traverse这个tree，碰到一个node，如果这个node在to_delete里，那么分两种情况：
# 1.这个node是一个leaf node，那么我们只需要切断它和它的parent之间的connection
# 2.这个node不是leaf node，那么我们需要做三件事，第一切断它和parent之间的connection，第二切断它和它的children之间的connection，第三
# 把它的children也放到stack里，因为以它的children为root的subtree里也可能还有我们需要delete的node，第四如果它的children不在to_delete里的话，把它的children放到res里
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        stack = [(root, None, True)]
        res = []
        to_delete_set = set(to_delete)
        if root.val not in to_delete_set:
            res.append(root)
        while stack:
            node, parent, ifLeft = stack.pop()
            if node:
                # check if node is in to_delete
                if node.val in to_delete_set:
                    # check if is leaf node
                    if node.left or node.right:
                        if node.left:
                            stack.append((node.left, None, True))
                            if node.left.val not in to_delete_set:
                                res.append(node.left)
                            node.left = None
                        if node.right:
                            stack.append((node.right, None, True))
                            if node.right.val not in to_delete_set:
                                res.append(node.right)
                            node.right = None
                    # cut connection between node and its parent
                    if parent:
                        if ifLeft:
                            parent.left = None
                        else:
                            parent.right = None
                else:
                    stack.append((node.left, node, True))
                    stack.append((node.right, node, False))

        return res