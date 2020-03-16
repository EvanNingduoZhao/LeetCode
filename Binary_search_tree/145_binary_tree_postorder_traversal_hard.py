# 想理解这道题得先理解144题，post_order直接用iterative写写不出来
# iterative只有在node itself是第一个被access的时候才成立
# 我们知道post order的顺序是 left right nodeitself
# 那么我们可以把它的顺序调过来求出 nodeitself right left的结果 再在return是把这个结果整体reverse
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            # because for the leaf nodes, we push None as their left and right into the stack
            # we don't want to include None in our result
            # so is the node popped out by the stack is None, we do nothing
            if node:
                res.append(node.val)
                # 为了让右边的先被pop 我们先push左 再push右
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]