def goodSegment(badNumbers, lower, upper):
    badNumbers.sort()
    print("badNumber is:", badNumbers)
    # 用binary search 找到sorted badNumbers中第一个比lower大的数字
    start = 0
    end = len(badNumbers)-1
    while start < end:
        mid = start + (end-start)//2
        if badNumbers[mid]<lower:
            start = mid+1
        else:
            end = mid
    print("startBadNumber is:", badNumbers[start])
    # 如果badNumbers[start]的确是一个在lower和upper之间的数的话
    if badNumbers[start]>=lower and badNumbers[start]<=upper:
        maxDiff = badNumbers[start]-lower
        # 如果start不是badNumbers里的最后一个index
        if start!=len(badNumbers)-1:
            for i in range(start+1, len(badNumbers)):
                # 如果当前看到的badNumber[i]要大于upper，那么要把upper-badNumbers[i - 1]和现有的maxDiff比较一下
                if badNumbers[i]>upper:
                    maxDiff = max(maxDiff, upper - badNumbers[i - 1])
                    break
                maxDiff = max(maxDiff,badNumbers[i]-badNumbers[i-1])
                print("maxDiff is:", maxDiff)
        # 如过start就是badNumbers里的最后一个index，那上面的for loop用不了，要如下单独讨论
        else:
            maxDiff=max(badNumbers[start]-lower, upper-badNumbers[start])
        return maxDiff-1
    # 可能badNumbers里没有在lower和upper之间的数字，这种情况下我们要return upper-lower+1
    else:
        return upper-lower+1

badNumbers = [37, 7, 22, 15, 49, 60]
lower = 3
upper = 48
print(goodSegment(badNumbers, lower, upper))


# LC 163和这道题很像
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