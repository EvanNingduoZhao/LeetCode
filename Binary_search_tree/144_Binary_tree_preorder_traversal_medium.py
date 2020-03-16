# recursive solution has already been covered in the Binary_tree_learning_notes
# This is the iterative solution

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            # because for the leaf nodes, we push None as their left and right into the stack
            # we don't want to include None in our result
            # so is the node popped out by the stack is None, we do nothing
            if node:
                res.append(node.val)
                # first push right then push left so left will be popped out first
                stack.append(node.right)
                stack.append(node.left)
        return res