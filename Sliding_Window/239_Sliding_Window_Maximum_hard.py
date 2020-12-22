#这道题我们要用一个double ended queue来解决，double ended queue（简称deque）
# 就是一个从左右两侧都可以push或者pop的数据结构
#我们在这个deque里的存的是数字在nums里的index，一个数字得符合两个条件它的index才有资格被存在deque里面
#首先它得在目前的window里，其次比它后进来的数字不能比它大
#第一个条件很好理解，因为deque里存的都是能够成为目前window里的max的candidate，你当然要在目前的window里才有可能是max
#第二个条件说的是，如果在你后面进来的数字都比你大的话，那你永远也没有机会成为max了，因为从此以后在你离开window之前
#你后面那个比你大的永远都会跟你在同一个window里，你永无出头之日。
#最后我们再讨论一下，如果A作为一个新进来的数字，A比目前deque里的所有数字都小，要把A留在deque里么，答案是要
#因为虽然目前在deque里的那些都比A大，但是它们都是比A先进来的，所以总会有一个时刻，它们这些先进来的会
#离开window之后被pop出去，那么A就有机会了（当然前提是比A后进来的那些都比A小）
#最后探讨一下时间复杂度，这里我们需要用amortized analysis，nums里的一个数字只会被push进deque一次，也只会被pop出deque
#一次，同时也只会在deque里最多被compare两次，因为compare的结果要么是newcomer大于等于自己，自己被pop出去了，
# 那就再也不会被compare，要么就是newcomer比自己小，那么newcomer就直接被append到自己后面了，它以后会给我们挡着
# 其他的compare，因此time complexity是和N成正比的，即O(N)，space complexity是O(N)，因为一共有n-k+1组
# res里就会被存n-k+1个数，而deque里是最多不超过k个，所以取更大的
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums)==0 or k==0:
            return None
        if k==1:
            return nums
        dq=deque([0])
        res=[]
        for i in range(1,len(nums)):
            if dq[0]==i-k:
                dq.popleft()
            while dq and nums[i]>=nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res


