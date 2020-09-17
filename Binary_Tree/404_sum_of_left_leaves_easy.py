class Solution:
    #iterative solution
    # 比较简单的一道题
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum=0
        if not root:
            return 0
        else:
            stack=[root]
            while stack:
                node=stack.pop()
                if node.left:
                    #每当碰到一个新的left node的时候，要检查一下它是不是一个leaf node，如果是就把它的val
                    #加到sum上
                    if not node.left.left and not node.left.right:
                        sum+=node.left.val
                    else:
                        stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return sum



    # recursive solution
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        #注意在class的一个function中define的普通variable是不能被该class的其他function所change的
        #硬要change的话，那个function不是change这个variable而是给新create一个同名variable
        #为了避免这个问题，所以这里用self.sum, object的attribute是可以被其他function change的
        self.sum = 0
        if not root:
            return 0
        else:
            self.helper(root)
            return self.sum
    # 这是不return东西，只是每次recursive call都potentially update self.sum
    def helper(self, root):
        if root.left:
            if not root.left.left and not root.left.right:
                self.sum += root.left.val
            else:
                self.helper(root.left)
        if root.right:
            self.helper(root.right)

    # recursive solution without helper function
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            #这种写法就是要每次recursive call都让sum归零
            #但是下面是sum+=
            #这样等所有recursive calls都return了，最初始的那一次call里最后sum就是该return的结果了
            #要能够熟练运用这两种recursion的写法
            sum = 0
            if root.left:
                if not root.left.left and not root.left.right:
                    sum += root.left.val
                else:
                    sum += self.sumOfLeftLeaves(root.left)
            if root.right:
                sum += self.sumOfLeftLeaves(root.right)
            return sum