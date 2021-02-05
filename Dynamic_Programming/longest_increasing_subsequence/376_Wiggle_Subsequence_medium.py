# 首先这道题可以用300题的那种对于每一个i都过一遍i左边的所有j的做法，之后用两个dp array
# 一个叫up 一个叫down，up[i]里存这的是以i为结尾的最长的且最后一个是up wiggle的wiggle sequence的长度
# down[i]里存的则是以i为结尾的最长的且最后一个是down wiggle的wiggle sequence的长度
# 那么在对于某个i，过他前面的所有j时，如果nums[i]>nums[j],那么up[i]=max(down[j]+1,up[i])因为如果i比j对应的数字大
# 那么nums[i]接在nums[j]后面是一个up wiggle，那么nums[j]和nums[j]前面的数字就得组成一个down wiggle了
# 相反如果nums[i]<nums[j]则down[i]=max(up[j]+1,down[i])
# 这种方法是时间是O（n^2）space是O(n)

# 以下是自己写的time是O(n)的方法，类似再下面一个要说的linear time的DP解法，但是不是标准解法，不用看了
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<2:
            return len(nums)
        posLen=0
        negLen=0
        i=0
        while i<len(nums)-1 and nums[i+1]<=nums[i]:
            i+=1
        if i<len(nums)-1:
            posLen=2
        wiggle="smaller"
        j=i+1
        while j<len(nums)-1:
            if wiggle=='smaller':
                if nums[j+1]<nums[j]:
                    posLen+=1
                    wiggle='larger'
                else:
                    j+=1
            else:
                if nums[j+1]>nums[j]:
                    posLen+=1
                    wiggle='smaller'
                else:
                    j+=1
        i=0
        while i<len(nums)-1 and  nums[i+1]>=nums[i]:
            i+=1
        if i<len(nums)-1:
            negLen=2
        wiggle="larger"
        j=i+1
        while j<len(nums)-1:
            if wiggle=='larger':
                if nums[j+1]>nums[j]:
                    negLen+=1
                    wiggle='smaller'
                else:
                    j+=1
            else:
                if nums[j+1]<nums[j]:
                    negLen+=1
                    wiggle='larger'
                else:
                    j+=1
        return max(1,posLen,negLen)

# 下面说linear time的DP解法
# 对于nums[i]和nums[i-1]而言无非有三种情况，第一是nums[i]大，第二是nums[i-1]大，第三是两者一般大
# 对于第一种情况up[i]=down[i-1]+1, down[i]=down[i-1]. 注意这里的down[i]表示的意思不在是必须以nums[i]
# 结尾的且最后是down wiggle的最长的wiggle sequence了，而是不要求结尾一定是nums[i]了，是nums[i]左边的
# 某个也可以
# 对于第二种情况down[i]=up[i-1]+1, up[i]=up[i-1]
# 对于第三种情况down[i]=down[i-1],up[i]=up[i-1]
# 这种方法和上面说的时间是N平方的DP解法在于，我们看清了一个本质，就是对于一个nums[i],我们没有必要拿他跟
# 他前面得所有j相比，只需要和nums[i-1]相比就好了。用这个方法过一遍 1 17 5 10 13 15 10 5 16 8 这个input
# 就会有更深入得理解

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 0
        n=len(nums)
        if n==1:
            return 1
        up=[1]
        down=[1]
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                up.append(down[i-1]+1)
                down.append(down[i-1])
            elif nums[i]<nums[i-1]:
                up.append(up[i-1])
                down.append(up[i-1]+1)
            else:
                up.append(up[i-1])
                down.append(down[i-1])
        return max(up[n-1],down[n-1])

# 实际上我们可以发现其实计算up[i]或者down[i]都只需要用到up[i-1] or down[i-1]
# 因此我们可以优化memory到O（1）
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 0
        n=len(nums)
        if n==1:
            return 1
        up=1
        down=1
        for i in range(1,n):
            # 我们在上一种方法里本来是这里还要让down[i]=down[i-1]
            # 但是对于down只用一个var来存储得话，down就相当于没变
            # 所以这里我们不需要handle down得问题
            if nums[i]>nums[i-1]:
                up=down+1
            # 同理这里我们不需要handle up
            elif nums[i]<nums[i-1]:
                down=up+1
        #         因为在上一种手段得else里max和down其实都没变，所以这里我们不用handle else
        # 即nums[i]==nums[i-1]得情况
        return max(up,down)

