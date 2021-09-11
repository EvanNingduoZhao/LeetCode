# 这题非常简单
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minValue = nums[0]
        sumSoFar = nums[0]
        for num in nums[1:]:
            sumSoFar += num
            minValue = min(sumSoFar, minValue)
        return max(1,1-minValue)