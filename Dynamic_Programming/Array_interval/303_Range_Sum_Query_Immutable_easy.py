#这个题主要的点在于要求很多很多个不同或者想要index pairs的rangesum，所以最好能设计成每次求rangesum的query的
#所需时间都是O(1)的
#这个题，你如果每次给一对index的pair，你都用for loop到nums里去算的话，那么每次query的Time是O(n),space是O(1)
#如果你预先把nums里每种可能的pairs的range sum都算出来，存在一个dict里的话，那么pre process的时间是O(n^2)
# space是O(n^2),每次query的time是O(1)

#下面的这个方法是各方面综合起来最好的，pre process的时候针对nums里的每个index i先计算以下前i个elements的sum
#存在dp这个1D array里，即dp[i]里存的就是nums前i个elements的和。这样pre processing的时间是O(n),用的space也是O(n)
#每次query时，假设index pair是i和j，那么range sum就等于dp[j]-dp[i-1],因为nums[i]得保留在sum range里

class NumArray:

    def __init__(self, nums: List[int]):
        #这里我们做了一个小的trick和上面general的思路里说的有点不一样
        #根据上面的思路，要return dp[j]-dp[i-1]，那i等于0的时候就不行了，得用特殊的if来check i是不是为0
        #是0的话直接return dp[j],很麻烦。这里就直接让dp的第一位等于0，dp[1]等于nums[0],dp[2]等于nums[0]+nums[1]
        #这样下面就可以用self.dp[j+1]-self.dp[i]来cover所有的case了，相当于把之前的方法里dp里所有的value都往后挪了一位
        #那么j就变成j+1，i-1就变成1了
        self.dp=[0]
        for num in nums:
            self.dp.append(self.dp[-1]+num)

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]