class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = -float("inf")
        for i in range(int(len(nums)/2)):
            res = max(res,nums[i]+nums[len(nums)-i-1])
        return res