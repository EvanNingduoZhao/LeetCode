#这道题第二遍做的时候用recursion写
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

    #这是在comment里找的recursive的写法
    #实际上想法和我自己的是几乎一模一样的但是这个code用了recursion来是实现，
    #而且更精简。
    #注意这里采用的是recursion只用来遍历，并在遍历的过程中updating一个值（这里的这个值是self.ans）
    #注意这里这个值必须设定成object的一个attribute或者一个list的一个element，不能是普通的variable
    def findSecondMinimumValue(self, root):
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1