#首先这道题最本质需要想透的点就是，对于任何一个Binary tree的node而言，在不走重复路的情况下，
#从root走到这个node只有一条唯一的path

#那么在用stack遍历的时候，每次push到stack里的不能只是一个node了，而得是一个tuple，tuple[0]是这个node
#tuple[1]则是，按照从root走到这个node的唯一path，目前已经走过的node的val之和，这样每次pop出来一个node的时候
#还同时知道走到这个岔路口时的之前经过的nodes的vals的和是多少
class Solution:
    #自己想的DFS的方法，实际上是传统preorder遍历的变形，需要思考时间较长，实际面试应该首先套用典型方法
    #典型方法见下面的评论中找到的DFS stack方法
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack=[]
        cur=root
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val != sum:
                return False
            else:
                return True
        path_sum=0
        while True:
            if cur.left and cur.right:
                path_sum+=cur.val
                stack.append((cur,path_sum))
                cur=cur.left
            elif cur.left and cur.right is None:
                path_sum+=cur.val
                cur=cur.left
            elif cur.left is None and cur.right:
                path_sum+=cur.val
                cur=cur.right
            else:
                path_sum+=cur.val
                if path_sum == sum:
                    return True
                else:
                    if stack:
                        tp=stack.pop()
                        cur,path_sum=tp[0].right,tp[1]
                    else:
                        return False

    # DFS with stack
    def hasPathSum2(self, root, sum):
        #先check一下root是不是null
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            #如果curr既没有left child 也没有right child 那说明curr是leaf node了
            #每次碰到leaf node 我们都要check一下 从root到这个leaf node的path的node vals之和是不是等于sum
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            #这里和传统的preorder遍历有所不同
            #传统的preorder是不看你到底有没有right或者left child的
            #如果没有的话，给stack push进去的就是None
            #但是这里因为需要把curr.right或left的val加到val上去
            #None.val会报错，所以要先check一下curr到底有没有左右child
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
        #stack空了还没return True说明到每一个leaf node的path sum都check了，没有一个等于sum，所以return
        #False
        return False

    # Recursively
    def hasPathSum1(self, root, sum):
        if not root:
            return False
        #在recursion的这个过程中，只要碰到一个leaf node的val，等于目前parameter里的sum就return True
        #因为sum其实在每次recursive call里都被减去了当前root的val，等到leaf node是root时，
        #如果这个path的sum真的是sum的话，这时parameter里的sum应该就等于root.val
        if root and not root.left and not root.right and root.val == sum:
            return True

        #Note：每次新call一次这method，要把root的val从sum里减掉
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)