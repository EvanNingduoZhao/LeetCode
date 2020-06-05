# recursive solution has already been covered in the Binary_tree_learning_notes
# This is the iterative solution

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        # after we reach the last node of the BST
        # it will still push two None into the stack
        # a stack with None element in it is still not empty
        # 所以这时while loop还会继续，每次都只执行while loop里面的第一行，pop出一个None，直到所有的None都
        #被pop出去了 才会return res
        while stack:
            node = stack.pop()
            # because for the leaf nodes, we push None as their left and right into the stack
            # we don't want to include None in our result
            # so if the node popped out by the stack is None, we do nothing
            if node:
                res.append(node.val)
                # first push right then push left so left will be popped out first
                stack.append(node.right)
                stack.append(node.left)
        return res