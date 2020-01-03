#先算出来整个array所有elements的和sum
#再从左开始iterate，如果leftsum=(sum-nums[i+1])/2的话return i+1
#因为i+1就是哪个index
class Solution:
    def pivotIndex(nums):
        if len(nums)<3:
            return -1
        else:
            sum=0
            for num in nums:
                sum+=num
            leftsum=0
            if leftsum==(sum-nums[0])/2:
                return 0
            for i in range(0,len(nums)-1):
                leftsum+=nums[i]
                if leftsum==(sum-nums[i+1])/2:
                    return i+1
            return -1

    test=[-1,-1,0,1,1,0]
    print(pivotIndex(test))