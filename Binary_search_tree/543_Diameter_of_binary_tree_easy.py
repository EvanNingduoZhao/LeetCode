#首先这道题最重要的思想是，题中所说的所谓longest path肯定是某一个node的左子树里最低的leaf和右子树里最低
#的leaf之间的path。如果这个node正好是root，那么这个path就是pass through root的，如果不是root，则这个path
# 则不path through root。验证一下就可以发现，对于每一个node自己的这个longest path就是这个node的left child
# 的height加上right child的height。因此我们只需要用recursive的手段来access一般所有的tree node，给每个
# tree node都计算出这个longest path，并和目前的max longest path比较，该替换替换就可以了
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #预先define一个我们之后要return的variable

        #Note：这里我们把这个variable define成一个object的attribute，而不是一个普通的variable，原因如下：
        #因为我们要在height这个inner function里update这个variable的值
        #但是对于普通的variable而言，因为scope的原因，在inner function中只能access outer function里
        #define的variable，不能change。如果change的话，其实是在inner中建立了一个新的同名variable
        #但是height里有这样一行self.best = max(self.best, left_height + right_height)
        #如果self.best是一个普通variable的话，这一行就先create了一个同名variable也叫self.best，但是
        #给它assign值的时候用的是max(self.best, left_height + right_height)，而这里用到了刚create的
        # self.best (which还没被assign值)，所以就会报local variable self.best is referenced before
        # assignment的错。但是实际上self.best是一个object的attribute， which在inner function里也可以直接被
        # change，所以不会报错。
        self.best = 0

        #这里height是一个inner function
        #其实height只是在基本的recursive求一个Binary Tree的fuction的基础上加了3行
        def height(root):
            if root is None:
                return 0
            else:
                #下面3行就是加的那3行
                #虽然这个function return的不是self.best,但是每次call这个function，self.best都会被
                #（potentially）update。
                left_height = height(root.left)
                right_height = height(root.right)
                self.best = max(self.best, left_height + right_height)
                return 1 + max(left_height, right_height)
        #这里call一下height只是为了让self.best被update成我们最后要return的result
        height(root)
        return self.best