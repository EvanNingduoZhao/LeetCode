#just use hash table
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return nums[0]
        else:
            dict={}
            for num in nums:
                if num in dict:
                    dict[num]+=1
                    if dict[num]>len(nums)/2:
                        return num
                else:
                    dict[num]=1