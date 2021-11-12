# 这道题的edge case非常有意思
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # 一个用来生成放到res里的string的helper function
        def formatRange(lower,upper):
            if lower==upper:
                return str(lower)
            else:
                return str(lower)+'->'+str(upper)
        # edge case
        if not nums or len(nums)==0:
            return [formatRange(lower,upper)]
        # 这道题的精髓就在于，对于nums之间相邻的两个数字，如果nums[i]>=nums[i-1]+2的话那么就要有东西加到res里了
        # 如果nums[i]==nums[i-1]+2，那么放到res里的就是num[i-1]+1这一个数字，如果nums[i]>nums[i-1]+2的话
        # 那么放到res里的就是nums[i-1]+1->nums[i]-1这个区间了
        # 但是比较tricky的是对于lower本身，如果nums[0]只比它大1，那么lower自己这个数字也要放到res里，所以为了和其他
        # 的情况统一，我们让prev不从lower开始，而是从lower-1开始
        prev = lower-1
        res = []
        for i in range(len(nums)):
            if nums[i]>=prev+2:
                res.append(formatRange(prev+1,nums[i]-1))
            prev = nums[i]
        # 因为nums里所有的数字都是小于等于upper的，如果nums[-1]==upper，那在上面的for loop里我们就已经cover了
        # 但如果nums[-1]<upper,我们要单独处理一下
        if nums[-1]<upper:
            res.append(formatRange(nums[-1]+1,upper))
        return res