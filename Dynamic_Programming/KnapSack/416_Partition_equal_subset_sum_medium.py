# 这道题实际上是一个经典背包问题的变形，它与经典背包问题的区别如下：
# 经典背包问题是指：我们面前有一系列物品，每个物品都有一个重量和价值，问在一个最大承重为w的背包中，
# 我们最多可以放入总价值为多少的物品
# 这道题首先可以简化为，假设nums的总和为M，那么这道题问的其实就是，在nums中有没有一个subset的总和是M/2
# （为什么可以做这样的简化呢？因为题目中要求把nums分成两个subset，即不能有剩下的，nums中的每一个数字最后
# 不是在一个subset中就是在另一个中，因此如果想要两个subset的和相等，那么每个subset的和都必须等于nums的和的一半）
# 这道题可以进一步被归为这样一个背包问题：我们可以把每个nums里的数字看作一个weight都是1，value等于这个数字的大小的物品
# 假设nums里一共有n个数，那么背包的最大承重就是n-1（背包里的物品是一个subset，不在背包里的是另一个，另一个里至少得有
# 一个数，所以背包的最大承重是n-1）那么题目问的就是，在一个最大承重为n-1的背包里，怎么能放下总价值正好等于M/2的物品

#我们先不考虑怎么用类似于经典背包问题的解法来解这道题，我们从DP的角度，从蛮力方法到memo再到tabulation来解，在解法的
# 演化过程中就可以看到其与经典背包问题的相似之处了

# 首先看蛮力解法：
# 这个蛮力解法虽然中心思想就是把nums中的每一组subset的组合的sum都计算一下，看有没有等于M/2的，但是它的代码实现很巧妙
# 他利用了一个recurrsion来做，思路如下：假设我们要找的subset的targetSum是M/2，我们从尾到头一个一个过nums里的数字，
# 对于nums里的一个element x，有两种可能的情况：1：如果x在subset里，那么我们下面就要在x左边的所有数字中找出来和为（targetSum-x的value）的组合
# 2：如果x不在subset里，那么我们继续在x左面的所有数字中找出和为targetSum的组合
# 这个recursion的base case是，如果targetSum在不断更新中变成0了，那说明正好凑成一个subset的和是M/2了，return True
# 如果targetSum还没变成0但是n已经变成0了，即在这个branch中向左走到头了想要放到subset里的数的和还没到M/2，return False
# 如果targetSum变成负的了，说明这条branch也不行，return False
# 如下面的code：我们从尾到头，一个一个过nums里的数字，对于每个数字我们都考虑它在subset里和不在subset里两种情况，
# 即对于每一个数字的处理，我们都分成两个branch。因此对于n个数字中的每一个都要考虑两种情况，那么一共就是2^n个情况
# 因此time是O(2^n) 因为我们这样的recursion实际上是dfs，就是对于一种情况一直执行到recursion tree的base case，
# 所以在任何时间点，recursion tree的depth最大就是n，因此space是O(n)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums: List[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(nums, n - 1, subset_sum)

# 上述蛮力解法有一个问题，比如对于nums是[6,7,4,3]而言，M/2是10，即targetSum是10
# 有一个branch会是把4和3都放到subset里，7不放进去，那么到了考虑6的时候targetSum就是10-4-3=3
# 另外一个branch则会是4和3都不放进去，但是7放进去，那么到了考虑6的时候，targetSum依然是10-7=3
# 因此对于targetSum是3时考虑要不要放6进去的这个subproblem我们做了两次，这就产生了overlapping subproblem
# 为了解决这个inefficiency，我们用memoization：用一个n*m大小的2d array来存已经算过的subproblem的结果
# 这里n是nums的size，m是targetSum。table里的每一个cell里应该填入的都是一个boolean，用来记录在当前走到的
# 这个element和目前所有还没走到的element中，能不能有一个subset其和能够等于此cell对应的column所代表的targetSum
# 有了这样一个用来记录的table，当我们遇到一个subproblem时就先到table里找这个问题是不是已经被算过一次了，如果是
# 直接用存好的结果。这个table在答案里给的code使用lru cache来实现的，目前还不知道这个是怎么回事
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)

# 上面的方法实际上用的还是recursion，属于top-down的，下面我们介绍buttom up的，这个解法和经典背包问题就非常相似了
# 解法的思路如下：我们真的用一个2d array，这个array的dimension是dp[n][targetSum]，for an array element i and sum j
# in the array nums. 这个array里的每一个cell都存的是一个boolean，dp[i][j]=true if the sum j can be formed by
# array elements in subset nums[0]...num[i] otherwise dp[i][j]=false
# 那么实际操作上dp[i][j]=true可以由两种情况来实现：
# 情况1：sum j can be formed without including the ith element,也就是说dp[i-1][j]就等于true，即只用前i-1个element
# in nums就可以得到一个和是j的subset
# 情况2：sum j can be formed including ith element,也就是说dp[i-1][j-第ith element的值]=true
# 具体code如下：
# 这里思考一下这道题和经典背包问题的关系：经典背包问题考虑的是把一个物品i放进或者不放进背包里后，只用这个物品和它前面的物品，最多
# 能组成多大的value，解决一个cell里应该填什么值，靠的是这个cell上面的那个cell（如果不把物品i放进背包）
# 或dp[i-1][weight capacity-weight of i](如果把i放进背包)，注意经典背包问题的cell里填的是值，且column对应的是从0到背包最大的weight capacity
# 这道题呢，考虑的是，把一个数字放进或者不放进subset里之后，在nums中这个数字和它左边的所有数字里能不能由一个sum是target sum
# 的subset。注意这个问题的cell里放的是boolean，解决当前cell的值靠的是当前cell上面的cell（如果不把这个数字放进subset里）
# 或dp[i-1][targetSum-value of i]（如果把这个数字放进subset里），且dp table的column对应的是从0到M/2的targetSum
# 最后说一下这种解法的time是O(m*n) space也是O(m*n) n是nums的size，m是nums的sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]
# 看了上面的code我们可以发现，在解决dp array目前这个row的时候只有上面一个row是有用的，因此我们的dp array实际上是
# 1d的就够了，不需要2d，具体code如下：
# 注意因为一个cell的值可能取决与上一个row里这个cell左边的cell的值，因此我们在traverse一个row时从右向左，这样就保证
# 左边的有用的值不会被抹去，这个方法的time是O(m*n) space也O(m)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]

# 下面的code是自己写的，不efficient不用看了
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2!=0:
            return False
        target=totalSum/2
        table=set()
        for num in nums:
            if num == target:
                return True
            temp=[]
            for n in table:
                newNum = n+num
                if newNum == target:
                    return True
                else:
                    temp.append(newNum)
            for n in temp:
                table.add(n)
            if num not in table:
                table.add(num)
        return False