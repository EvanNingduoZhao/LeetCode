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
    # 还有一种是recursive的解法，这种解法相当于DFS，肯定没有BFS好了，但是放在这里主要是为了复习recursion的写法
    class Solution:
        def minDepth(self, root: TreeNode) -> int:
            #base case有两个一个是这里没有root时该return 0
            if not root:
                return 0
            else:
                children = [root.left, root.right]
                #第二个base case是如果root没有children，return 1
                if not any(children):
                    return 1
                #children里永远只会有两个node
                #children里的child不用和别人比，只需要和跟自己一对的另一个比就好了
                #因此每一次一对chidlren之间比之前都会让min_depth=inf
                min_depth = float('inf')
                for child in children:
                    if child:
                        min_depth = min(self.minDepth(child), min_depth)
                #我们需要return的只是这一对children里谁的minDepth更小一点，那这一对children的
                #的parent的mindepth就等于其加1
                return min_depth + 1

