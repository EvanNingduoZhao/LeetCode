class Solution:
    #对于一个node而言，它要么没有child，要么有两个children
    #如果有两个children而言有两种情况
    # 1）要么这两个children都和它自己的val一样大
    #对于这种情况我们把这两个children都push到stack里
    #2）要么一个child A的value和自己的value一样，另一个child B的value更大一些
    #那么我们把A push到stack里，而这个更大一些Child B就可能是我们要找的第二小的
    #但我们没有必要把这个child B的子node也append到stack里了，因为它的子node至少都是大于等于它的
    #
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        else:
            if not root.left and not root.right:
                return -1
            else:
                stack=[root]
                min=root.val
                while stack:
                    node=stack.pop()
                    if node.left:
                        if node.left.val!=root.val:
                            #如果目前min还等于root.val那就说明之前我们碰到的所有node
                            #的value都还等于root的val，所以对于这个第一个不等于root value的node，
                            #我们直接让min等于它 的value
                            if min==root.val:
                                min=node.left.val
                            else:
                                if node.left.val<min:
                                    min=node.left.val
                        else:
                            stack.append(node.left)
                        if node.right.val!=root.val:
                            if min==root.val:
                                min=node.right.val
                            else:
                                if node.right.val<min:
                                    min=node.right.val
                        else:
                            stack.append(node.right)
                if min!=root.val:
                    return min
                else:
                    return -1