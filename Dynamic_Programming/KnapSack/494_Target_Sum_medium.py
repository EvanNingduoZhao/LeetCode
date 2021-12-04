# 这道题还是和经典背包问题有很多相似之处，下面的code是最简介的space也优化成了只用两个row的一个dp table的形式
# 但是思路讲解我们还是用一个n*2m的dp table，其中n是nums里elements的数量，m是nums里所有elements的sum
# 首先我们可以得出的一个结论是，用nums里的element不管是什么expression，一个expression的值肯定都是在-m和m之间的
# 那么这个dp table中每一个col对应的就是从-m到m的一个数字。具体的说，如果代表sum是j的那个col的实际的index是j+m，
# （因为最小的，即第一个col对应的sum应该是-m，而这个col的实际index其实是0，因此一个sum j对应的实际col的index是j+m）
# 那么dp table里的一个第ith row，j+m th col的cell的意义就是，只用前i个element，有几种expression可以得到sum是j
# 那么该解决一个subproblem呢？有两种思路：第一种思路比较intuitive，第二种比较好code up
# 先讲第一种：想要用前i个element得到j有两种办法，（假设第i个element的值是x）
# 方法1：是用前i-1个element得到sum是j-x的sum再+第i个element
# 方法2：是用前i-1个element得到sum是j+x的sum再-第i个element
# 也就是说dp[i][j]=dp[i-1][j-x]+dp[i-1][j+x] （这里先不考虑要把实际值是负的j转化成非负的index）
# 但是这个方法的缺陷是，因为我们一个row里只有代表从-m到m这些sum的cols，如果j本身就是对应-m了，那么j-x就会是小于-m的了
# 同理如果j本身对应m了，那么j+x就会是大于m的了，这都会造成index out of range
# 因此我们采用第二种思路：
# 如果dp[i-1][j+totalSum]>0,即对于前n-1个element而言至少有一个expression可以得到sum j
# 那么dp[i][j+totalSum+x]和dp[i][j+totalSum-x]就都加上dp[i-1][j+totalSum]
# 这里注意对于dp[i-1][j+totalSum]>0的j+totalSum而言，j+totalSum+/-x肯定都是在col的range里的
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if -target<-totalSum or target>totalSum:
            return 0
        dp = [0 for j in range(-totalSum, totalSum+1)]
        # 填好第一个row
        dp[nums[0]+totalSum]+=1
        dp[-nums[0]+totalSum]+=1
        # 真正的loop从第二个row开始
        for i in range(1, len(nums)):
            x=nums[i]
            # temp是目前要fill的row
            # dp是上一个fill好的row
            # fill好temp后让dp=temp
            temp=[0 for _ in range(-totalSum, totalSum+1)]
            for j in range(-totalSum, totalSum+1):
                if dp[j+totalSum]>0:
                    temp[j+totalSum+x]+=dp[j+totalSum]
                    temp[j+totalSum-x]+=dp[j+totalSum]
            dp=temp
        return dp[target+totalSum]


    -3 -2 -1 0 1 2 3
2   0  1  0  0 0 1 0
1   1  0  1  0 1 0 1