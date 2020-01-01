#很简单 简单到没啥价值
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        max=0
        for num in nums:
            if num==1:
                counter+=1
                if counter>max:
                    max=counter
            else:
                counter=0
        return max