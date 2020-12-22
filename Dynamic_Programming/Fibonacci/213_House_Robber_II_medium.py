#这道题实际上就相当于是两个198题何在一起，先看懂198题再来复习这个
#这道题就相当于是对第一个到倒数第二个房子做一遍198题，再对第二个到最后一个房子做一遍198题
#return结果更大的那个。为什么work？因为rob第一个就肯定不能rob最后一个，当然，在对于第一个到倒数第二个房子做一遍时
#是不会漏掉任何一种rob第一个的房子的方案的，同理rob了第二个就肯定不能rob第一个，所以对第二个到最后一个房子做一遍时
#也肯定不会漏掉任何一个rob第二个房子的方案的，两遍合起来就肯定什么都不会拉下了。

class Solution:
    def rob(self,nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        rf_prev1=0
        rf_prev2=0
        nrf_prev1=0
        nrf_prev2=0
        #对第一个到倒数第二个房子做一遍
        for i in range(len(nums)-1):
            rf_current=max(nums[i]+rf_prev2,rf_prev1)
            rf_prev2=rf_prev1
            rf_prev1=rf_current
        #对第二个到最后一个房子做一遍
        for i in range(1,len(nums)):
            nrf_current=max(nums[i]+nrf_prev2,nrf_prev1)
            nrf_prev2=nrf_prev1
            nrf_prev1=nrf_current
        # return结果更大的那个
        return max(rf_prev1,nrf_prev1)

    input=[2,2,4,3,2,5]
    print(rob(input))