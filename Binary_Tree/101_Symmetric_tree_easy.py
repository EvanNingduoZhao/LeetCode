class Solution:
    ## recursive solution
    #首先这个问题如果用recursion来做的话肯定是single recursion就能解决的，用不着double recursion
    #判定是否对称是两个node的问题，因为得两个对应位置的一对nodes的values相等我们才有symmetry
    #因此我们的recursive function需要两个parameters。给定的function只有一个parameter所以我们需要写一个
    #helper function作为我们的recursive function
    def isSymmetric(self, root: TreeNode) -> bool:
        #edge case： root是空的也可以视为对称
        if not root:
            return True
        #把root的左右child放到helper里开始进行recursive check
        else:
            return self.helper(root.left, root.right)

    def helper(self, l, r):
        #两个nodes都是none也是对称的
        if not l and not r:
            return True
        #一个是none一个不是肯定不对称
        elif l and not r:
            return False
        elif not l and r:
            return False
        #两个node都不是none的情况
        else:
            #先比较两个nodes的values是否相等，如果相等再把这两个nodes的一共四个孩子两两一组最为parameters
            #进行recursive call，具体这个两两一组为什么是这样分的：画出tree的第四层找规律就能找出来原因
            return l.val == r.val and self.helper(l.left, r.right) and self.helper(l.right, r.left)


    ## Iterative Solution
    # 这个方法的主要思想是把一整个tree看作root，以root的left child为root的left subtree
    # 和以root的right child为root的right subtree
    # 把一个symmetric tree的第四第五层画出来以后就会发现，如果我们用iterative 即stack的方式去traverse
    # left subtree和right subtree，并且在traverse left subtree的时候每次都是把一个node的left child先
    # push进去再push right child，但是traverse right subtree时则先push right child再push left child
    # 如果以这种方式traverse一个对称的tree的两个subtree的话，我们可以发现对于两个stack而言
    # 每次各自push和pop的node的values应该是一样的。因此我们就用这种方法来traverse，直到遇到两个stacks
    # 同时各自pop出来的nodes的value不相等时就return false
    def isSymmetric_iterative(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            if not root.left and not root.right:
                return True
            elif (not root.left and root.right) or (not root.right and root.left):
                return False
            else:
                stackl = [root.left]
                stackr = [root.right]
                while stackl and stackr:
                    lnode = stackl.pop()
                    rnode = stackr.pop()
                    #pop出来的两个node都是空的话也是符合对称的，因此continue
                    if not lnode and not rnode:
                        continue
                    elif (not lnode and rnode) or (not rnode and lnode):
                        return False
                    else:
                        if lnode.val == rnode.val:
                            #对于left subtree的stack 先push left child
                            stackl.append(lnode.left)
                            stackl.append(lnode.right)
                            # 对于right subtree的stack 先push right child
                            stackr.append(rnode.right)
                            stackr.append(rnode.left)
                        else:
                            return False
                return True