#这里还是用一个double recursion来解，和另外一道double recursion的437题一起看
# helper function是inner recursion，用来check：
#  对于一个root是node A的s的subtree，来check这个subtree是不是完全和t相同
# outter recursion的作用则是让s里的每一个node都当一次node A，知道找到了一个合格的为止
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif s is None and t:
            return False
        else:
            return self.helper(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    #在每一个recursion call里我们只看一对对应位置是否都有node且node的val相等
    #这个recursion就属于single recursion里传递boolean的那种
    def helper(self, s, t):
        #如果两个树一样，那么一个树的leaf node的对应位置一定也是另一棵树的leaf node
        #所以check两棵树是否一样，check到最底部的时候一定会出现s和t都是None
        #这时候要return True，但这只是必要条件之一，得其他所有leaf nodes位置都对应另外一棵树的leaf node
        #才能最终判定两棵树一样（所以最下面一行用and）
        if not s and not t:
            return True
        #如果一对对应位置里有一个位置有node另一个没有那么这两个树一定不一样
        if (not s and t) or (not t and s):
            return False
        #同理 一对对应位置都有node但是value不一样，两个树肯定不一样
        elif s.val != t.val:
            return False
        #在s和t两个binary tree的对应位置都有node且node的value一样的话
        #那么我们需要确定这两个对应位置分别的左右子树也是完全一样的，这是一个典型的可以用recursion解决的问题
        else:
            return self.helper(s.left, t.left) and self.helper(s.right, t.right)

    #这是另外一种方法 用preorder traversal来把两个tree都traversal一遍并把每个node的value都分别放在一个list里
    #如果最后t的list in s的list的话那么t就是s的subtree
    # 但是和一般的preorder traversal有两个小区别：
    # 第一个碰到null也要把null放到list里（这是为了保证t包含所有s的那个subtree的子孙，t的leafnode在s里也得是leafnode）
    # 第二个每一个放进去的node value要用括号括起来 （这是为了保证不会出现【3，4，5】被当作在【23，4，5，6】里的错误判断）
    # 把preorder换成postorder这个方法还是可以work的但是换成inorder不行
    def preorder(node, vals):
        if not node:
            vals.append("NULL")
            return

        vals.append("(" + str(node.val) + ")")
        preorder(node.left, vals)
        preorder(node.right, vals)

    class Solution:
        def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
            s_vals = []
            t_vals = []

            preorder(s, s_vals)
            preorder(t, t_vals)

            return "".join(t_vals) in "".join(s_vals)