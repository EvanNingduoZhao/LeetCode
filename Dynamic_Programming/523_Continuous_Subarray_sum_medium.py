# 下面是自己想到的这道题的dp解法，time是n square，space是n，
# 思路如下，对于一个以第i个数字结尾的size是三的continuous array而言，它的sum等于第i个数字的值加上以第i-1个数字为
# 结尾的size为2的continuous array的和。因此我们可以traverse整个array，对于第i个数字而言，以它结尾的话，我们可以有
# size是从2一直到i的continuous subarray，那么每个subarray的sum都可以用上面说的那种手段算出来
# 且第i-1个字母结尾的某个size的continuous subarray的size在i之前指向第i-1个字母时就被我们算过之后存到dp array里了
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        n = len(nums)
        # prevSums的第0个index不用，从1开始表示以第i个数字为结尾的长度为1的continues subarray的sum是多少
        # 随着traversal的进行，我们针对每一个数字都更新一次prevSums
        prevSums = [0 for _ in range(n + 1)]
        prevSums[1] = nums[0]
        # 从第二个数字开始traversal
        for i in range(1, n):
            # 在i指向第i个数字时，我们开始用之前i指向第i-1个数字时算出来的结果来更新prevSums的内容
            # 这里的index有些tricky，假设现在i是4，那么算上i指的那个数字，其实i和i前面一共有5个数字
            # 因此最多可以算以第i个数字结尾的size是5的continuous subarray的sum，我们也就从这个最长的开始算
            # 因此j的index就得从5开始，之后慢慢递减，因为i等于4，那么想要j能等于5，range的上限就得是i+2
            # j最小到2就行，因为j=1时长度就是1，即i指的数字本身的值，我们在下面单独改它
            for j in reversed(range(2, i + 2)):
                prevSums[j] = nums[i] + prevSums[j - 1]
                # 注意对于k=0的情况要单独check
                if k == 0:
                    if prevSums[j] == 0:
                        return True
                else:
                    if prevSums[j] % k == 0:
                        return True
            # 单独改长度是1的subarray的sum
            prevSums[1] = nums[i]
        return False

# 下面介绍一种用hashTable来实现的时间和空间都是n的解法
# 这个方法用到了一个很简单的数学思想，即如果a%k=x，b%k=x,那么(a-b)%k=0
# 这个思想落实到code上就是用一个sumSoFar来记录traverse list过程中遇到所有elements的和
# 每遇到一个element就把它加到sumSoFar上，但是加完了以后，如果input的k不等于0
# 就让sumSoFar=sumSoFar%k，因为我们一路上感兴趣的也是sumSoFar%k的余数
# 而让sumSoFar=sumSoFar%k是不影响之后的余数的值的，因此可以这样
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums)==0:
            return False
        n=len(nums)
        memo={}
#         对于只有两个elements且两者加和等于k的整数倍的nums，它其实是合格的
#         但是这个nums的最后一个element的index是1，要想满足和memo中已有的
#         跟目前sumSoFar%k的结果一样的（目前sumSoFar%k的结果是0）的那个element的index相差2
#         那那个element的index就得是-1，而-1又不是天然就有的，所以我们要在开头给它加上去
#         这里memo的key是对于某一个element而言的sumSoFar%k的结果，value是那个element的index
        memo[0]=-1
        sumSoFar=0
        for i in range(0,n):
            sumSoFar+=nums[i]
            # 注意：题目中只要求sum=n*K，n只要是整数就行，所以可以是0，因此只要又一个长度超过2的连续subarray的
            # 和是0就是符合要求的
            # 如果k==0的话，那么如果下两行的if是不会执行的，如果连着两个element都是0的话
            # sumSoFar的值不便，一直保持着第一个0前面的那个element的sumSoFar，加了两个0上去以后
            # sumSoFar的值不变，但是index的差距拉开了2，所以会return true
            if k!=0:
                sumSoFar=sumSoFar%k
            if sumSoFar in memo:
                if i-memo[sumSoFar]>1:
                    return True
            else:
                memo[sumSoFar]=i
        return False