# 假设我们要组成的target amount是n，那么n的最优组合是这样算出来的：
# 对于coins的每种面额c，我们都看n-c的最优组合需要几个硬币，取需要最少硬币的那个n-c的c，那么组成n所需的硬币数量
# 就等于组成n-c所需的硬币数量+1，这个1就是那一个面额是c的硬币
# 因此我们可以从1到n一直traverse上去，之后用一个dp array来存subproblem的结果
# dp[i]里存的就是组成i这个amount所需的最少的硬币数量
# 当然有一种情况是，对于某一个n值，我们把所有的面额c都试了一遍，但是所有的n-c都是无法被现有硬币的面额组合出来的
# 那么我们就把dp[n]存成-1
# 实际上，这样一来，当我们遇到更大的n时，看到dp[n-c]=-1，那么我们就知道n-c是无法被现有的硬币面额组合出来的了
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount or amount == 0:
            return 0
        # 注意dp[0]一直等于0，因为如果对于某个k，就有一个和他相等的面额c的话，那么只需要一个硬币就可以组成k
        # 且因为我们在下面设minNum为dp[k-c]+1,所以这里dp[k-c]即dp[0]得等于0
        dp = [0 for _ in range(amount+1)]
        for k in range(1,amount+1):
            minNum = float('inf')
            for c in coins:
                if c<=k:
                    if dp[k-c] != -1:
                        minNum = min(minNum, dp[k-c]+1)
            # 如果for c in coins这个for loop走了一圈，minNum还是无限大的话
            # 那说明所以的c要不然是c比k大，要不然是dp[k-c]==-1，因此说明现有的面额c们无法组成k
            # 因此让dp[k]=-1
            if minNum == float('inf'):
                dp[k] = -1
            else:
                dp[k]=minNum

        return dp[amount]