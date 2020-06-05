class Solution:
    # BFS method(most efficient solution)
    # 这种问最短路径的题目用BFS来解是最effcient的
    # 因为BFS是一层一层的遍历，在遍历过程中碰到的第一个没有children的node一定就是离root最近的leaf node
    # 因此直接return这个node的level就好了 下面其他的node根本都不用看了
    # 这里如果用DFS的话是需要遍历所有的node，keep updating level最小的leaf node，没有BFS那么efficient
    class Solution:
        def minDepth(self, root: TreeNode) -> int:
            if not root:
                return 0
            queue = [(root, 1)]
            while queue:
                node, level = queue.pop()
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.insert(0, (node.left, level + 1))
                if node.right:
                    queue.insert(0, (node.right, level + 1))

    # DFS iterative method
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            res=[0]
            stack=[(root,1)]
            while stack:
                node,l=stack.pop()
                if not node.left and not node.right:
                    if res[0]==0:
                        res[0]=l
                    else:
                        if l<res[0]:
                            res[0]=l
                if node.left:
                    stack.append((node.left,l+1))
                if node.right:
                    stack.append((node.right,l+1))
            return res[0]

