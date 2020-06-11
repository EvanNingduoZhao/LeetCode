#用inorder traversal遍历整个BST，这样就是从小到大看遍BST的所有node
#在遍历的过程当中 keep updating mindiff，即当前node value和上一个看到的node的value的差值
#如果再破新低就update
#这里自己写的是iterative的inorder traversal
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minDiff=float('inf')
        prev=None
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                return minDiff
            node=stack.pop()
            #如果这是最左下角的第一个node，那么我们让prev等于它的value
            #先不计算diff 等遇到下一个node以后用下一个node的value和它做diff
            if prev is None:
                prev=node.val
            if node.val!=prev:
                diff=node.val-prev
                minDiff=min(minDiff,diff)
                prev=node.val
            root=node.right

    #这个是comment里找到的很简洁的recursive的inorder traversal的解法
    def getMinimumDifference(self, root):
        L = []
        #recursive的inorder traveral
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)

        dfs(root)
        #zip就是把两个list合在一起，变成一个list of tuples
        #每一个tuple里的两个elements就是前后两个consecutive的nodes
        return min(b - a for a, b in zip(L, L[1:]))