# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 这道题其实和543题很像，都属于是potential double recursion的拐点问题，只不过543是求最长的path的长度
# 这道题是求max path Sum。对于这种拐点的问题我们要清楚，对于拐点是node A的path而言，这条path的我们要求的性质
# 比如说这道题里问的path sum，是等于node A的value + 以node A的left child为起点的单一方向向下不带拐点的path的Sum
# + 以node A的right child为起点的单一方向向下不带拐点的path的Sum （当然只有在后两个加数是大于0的前提下我们才
# 会把它加上去，否则不加上去）因此我们在进行recursion的过程中，每个node都会当一次node A，我们要针对
# 每一个node都算出来这样一个和，之后和目前已经见过的最大的比，该update就update。这里这个目前已经
# 见过的最大值我们存在self.best里。但是recursive function不能把这个和作为要return的东西，因为
# 以node A的child为这个node A算出来的这个和，对计算以node A自己为node A的这个和是没有帮助的
# 在计算以node A自己为node A的这个和时，我们要用的是以node A的left/right child为起点的单一方向向下不带拐点的path的Sum
# 因此以node A自己的value + max(node A的left child为起点的单一方向向下不带拐点的path的Sum,node A的right child为起点的单一方向向下不带拐点的path的Sum)
# 才是我们要在recursion中return的
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.best=float('inf')*(-1)
        def pathSum(root):
            # 如果root是none，那么经过这个node的path的sum一定是0
            if not root:
                return 0
            # 如果以node A的left child为起点的单一方向向下不带拐点的path的Sum是小于0的话，我们
            # 还不如不加上它，所以如果它是小于0的，我们leftSum就是0
            leftSum=max(pathSum(root.left),0)
            # 右侧同理
            rightSum=max(pathSum(root.right),0)
            # 这里看以node A为拐点的path的sum能不能比目前最大的sum还大
            # 注意leftSum或者rightSum如果实际是小于0的话，我们都让它们等于0了，因此相当于如果
            # 小于0就没加它了
            self.best=max(self.best,root.val+leftSum+rightSum)
            # recursive function return的是
            # node A自己的value + max(node A的left child为起点的单一方向向下不带拐点的path的Sum,node A的right child为起点的单一方向向下不带拐点的path的Sum)
            return max(root.val+max(leftSum,rightSum),root.val)
        pathSum(root)
        return self.best