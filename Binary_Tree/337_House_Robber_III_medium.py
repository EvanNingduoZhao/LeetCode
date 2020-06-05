#这道题用recursion来解
#对于一个node来说 我们有两种选择
# 1）偷：那么相应的我们就一定不能偷它的left或者right child了
# 2）不偷：那么相应的我们可以偷也可以不偷它的left或者right child，有可能不偷left child是因为没准偷left
# child的child能偷到的更多。不偷right child也是同理
# 这里要注意的是，对于一个node而言，去计算以偷这个node或者不偷这个node为起点的偷窃path的总收益只需要知道
# 以偷或不偷他的左右子node为起点的偷窃path的总收益
# 对于上面的第一种情况 偷这个node，那么这个path的总收益就等于root.val+不偷左子node为起点的path总收益+
# 不偷右子node为起点的path的总收益
# 对于上面第二种情况，不偷这个node，那么这个path的总收益则等于
# max（不偷左子node为起点的path总收益，偷左子node为起点的path总收益）+
# max（不偷右子node为起点的path总收益，偷右子node为起点的path总收益）
# https://www.youtube.com/watch?v=-i2BFAU25Zk 这个方法的解说在这个视频里

class Solution:
    def rob(self, root: TreeNode) -> int:
        res=self.helper(root)
        return max(res[0],res[1])
    def helper(self,root):
        # base case，如果这个node是none那么偷或不偷它我们拿的钱肯定都是0
        if not root:
            return [0,0]
        else:
            result=[0,0]
            left=self.helper(root.left)
            right=self.helper(root.right)
            #result[O]记录的信息是如果不偷这个node，那么从这个不偷node开始为起点的偷窃path一共能偷多少钱
            result[0]=max(left[0],left[1])+max(right[0],right[1])
            # result[1]记录的信息是如果偷这个node，那么从偷这个node开始为起点的偷窃path一共能偷多少钱
            result[1]=root.val+left[0]+right[0]
            #现在result里存这偷或不偷这个node的分别的收益
            #把这个result 返回给它的recusive caller，就足够让它的caller计算出偷与不偷它的caller的
            #分别的总收益了
            return result