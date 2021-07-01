#记这道题的笔记时要注意和coin change II那道题进行对比，主要的区别在于两层for loop的循序，以及为什么要这样
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0]=1
        for k in range(target+1):
            for num in nums:
                if num<=k:
                    dp[k]+=dp[k-num]
        return dp[target]