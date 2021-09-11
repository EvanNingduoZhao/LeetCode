#记这道题的笔记时要注意和coin change II那道题进行对比，主要的区别在于两层for loop的循序，以及为什么要这样
# 先去看518题的notes
# 这道题不同与377题，我们这里是对于每一个target都traverse一遍所有的数字（数字类比的是377里的硬币面额）
# 同样还是以target是5，面额是2和3来举例子。在让target等于5之前，我们已经让target等于过2和3了，并且发现target是2时有一种方法，target
# 是3也是一种方法，那么在target等于5时我们traverse到2时发现[3,2]的组合，traverse到3时则又会发现[2,3]的组合。
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0]=1
        for k in range(target+1):
            for num in nums:
                if num<=k:
                    dp[k]+=dp[k-num]
        return dp[target]