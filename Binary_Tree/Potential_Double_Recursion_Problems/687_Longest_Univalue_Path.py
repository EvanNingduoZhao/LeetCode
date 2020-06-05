#这道题不需要用double recursion，single recursion就够了
#这道题本质上和543_diameter of binary tree是一样的
#区别是543这道题这要有child node就可以在left/right path length上+1
#但是这道题是不仅得有child node且child node的val得和自己的val一样才可以+1
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            self.longest = 0
            self.helper(root)
            return self.longest

    def helper(self, root):
        if not root:
            return 0
        #这里的llength和rlength指的是不算目前的node本身
        #从这个node的left child或right child为头开始算 univalue path的length是多少
        llength = self.helper(root.left)
        rlength = self.helper(root.right)
        #如果这个node的left child的value和它自己的value一样
        #那么就可以把这个node本身也算到左侧的这个univalue path里了（length+1）
        if root.left and root.left.val == root.val:
            left = llength + 1
        #但如果自身的value和leftchild的value不相等，那就得归零从新开始count等于目前这个node
        #的univalue path的长度了
        else:
            left = 0
        #右侧同理
        if root.right and root.right.val == root.val:
            right = rlength + 1
        else:
            right = 0
        #每次把算上自身的左侧和右侧univalue path的length算出来以后
        #把两者相加就是pass through目前这个node的univalue path的长度了
        #每次得出这样的一个长度以后就和目前的最长的这个长度去比较 该替换替换
        self.longest = max(self.longest, left + right)

        #每次去算出pass through自己这个node的univalue path的length是为了自己
        #但是每次recursive call return出来的value是用来给算自己的pass through 自己的parent node
        # 的univalue path的length的 所以要把自己左右侧univalue path中更长的那个return回去
        return max(left, right)