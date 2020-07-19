#这道题有两种做法一种是DP，另一种的greedy
#下面写的是DP的做法，等学了greedy以后再做一遍这个题
# 这道题用DP做的思路几乎和300题是一摸一样的，先复习300再复习这道题
# 唯一的区别就是因为300题规定了要的是subsequence，即可以跳着挑但是不能改变
# 循序，而这道题则没有这样的要求，是可以改变循序进行组合的，那么我们可以先把这个list of pairs根据每个pair的第一个值的
# 大小sort一下，这样一来每个j pair可以follow的i pair就一定都在自己左边了，因此虽然还是可以改变顺序挑，但是因为
# 在你右边的pair的第一个值都比你的第一个值大，那它的第二个值就也一定比你的第一个值大，那你是不可能能去follow你右边的pair的

# 这样sort之后这道题就变成了和300题一摸一样了，即对于每一个j pair都用pointer i traverse j左边的所有pairs
# 看看j pair的第一个值是不是大于i pair的第二个值，如果是的话，dp[j]=dp[i]+1，在traverse所有自己
# 左边的i pairs过程中keep track of最大的dp[j]，最后return max(dp)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        #[[1,2][3,4][6,8]]
        # edge cases:
        if not pairs:
            return 0
        if len(pairs)==1:
            return 1
        else:
            #把pairs根据每个pair的第一个值的大小增序排列
            pairs.sort()
            # 每一个pair自身都可以看作是一个长度为1的pair chain
            dp =[1 for _ in range(len(pairs))]
            for j in range(1,len(pairs)):
                for i in range(0,j):
                    if pairs[j][0]>pairs[i][1] and dp[i]>=dp[j]:
                        dp[j]=dp[i]+1
            return max(dp)