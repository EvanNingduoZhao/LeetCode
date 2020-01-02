#很简单 不用看
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            max=1
            current=1
            for i in range(1,len(nums)):
                if nums[i]>nums[i-1]:
                    current+=1
                    if current>max:
                        max=current
                else:
                    current=1
            return max