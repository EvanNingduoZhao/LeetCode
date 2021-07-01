class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(0, amount+1)]
        dp[0]=1
        for c in coins:
            for target in range(c, amount+1):
                dp[target]+=dp[target-c]
        return dp[amount]