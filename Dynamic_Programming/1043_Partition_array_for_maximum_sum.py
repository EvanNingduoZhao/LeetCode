
# 这道题和longest increasing subsequence里的题目解法有些类似，都是dp[i]里存着input array[:i+1]的解，之后考虑加入了第i+1个item以后
# input array[:i+2]的解和我们已经解决过的subproblems有什么联系
# 这道题还是采用一个buttom up的想法来实现，对于index i，我们定义一个subproblem为对于arr[:i+1]这个subarray，largest sum after partitioning
# 是多少。那么根据bottom up的原则，我们要考虑的是，在arr[:i+1]这个subarray的尾巴上再加上一个arr[i+1]这个item，会对原本subproblem的结果有什么
# 影响，即对于arr[:i+2]这个subarray而言subproblem的解是多少。我们用[1,15,7,9,2,5,10]来举例，假设现在i是3，arr[3]是9，也就是说[1] [1,15] [1,15,7]
# 这三个subarray对应的subproblem的解都已经算出来了。这里注意dp[0] = 0这是我们为了方便的一个小trick，dp[1]里存的才是[1]这个subproblem的结果
# 因为我们的k是3，所以能够形成的带有9的partition是[9][7,9][15,7,9],他们被按照规则转化过后就是[9] [9,9] [15,15,15],那么用[9]这个partition的话
# 最后[1,15,7,9]这个subproblem的就被分成了[1,15,7][9]且结果就是dp[3]+9,用[9,9]结果就是dp[2]+9*2,用[15,15,15]的话就是dp[1]+15*3.
# 最大的是dp[3]+9 = 15+15+15+9 = 54
# 因此我们让dp[4]=54. 以此类推对于arr里的n个item每一个我们都这么过一遍，因为多加一个item i最多能产生k种新的partition，时间复杂度是O(nk),空间复杂度
# 是O(n)
def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    dp = [0] * (len(arr) + 1)
    dp[1] = arr[0]
    for i in range(1, len(arr)):
        # maxSum里存着目前为止我们对arr[:i+1]这个subproblem发现的最优解
        maxSum = float("inf") * (-1)
        # 关于maxNum这里有些tricky，看37行的comment
        maxNum = float("inf") * (-1)
        for j in range(0, k):
            if i - j >= 0:
                maxNum = max(maxNum, arr[i - j])
                # 如果我们不用maxNum的话，代码应该是下面这么写的，max(arr[i-j:i+1])的作用是算出来包含item i的这个新partitiom里最大的number是
                # 多大，当item i是9，j=2时，新的partition，即arr[i-j:i+1]是[15,7,9],那么之中的最大值是15。但是这样的问题是list slicing比较费时
                # 观察后我们发现，其实可以用maxNum来记录目前见到的最大的item，当j=0时arr[i-j]是9，j=1时arr[i-j]是7，而目前我们见过最大的是9
                # 所以[7,9]这个partition应该被变成[9,9]，而j=2时arr[i-j]是15，此时见过最大的就是15了，因此[15,7,9]这个partition应该变成
                # [15,15,15]
                # newSum = max(arr[i - j:i + 1]) * (j + 1) + dp[i - j]
                newSum = maxNum * (j + 1) + dp[i - j]
                maxSum = max(maxSum, newSum)
        # 注意dp[1]是存着[1]这个subproblem的解的，所以当i=3，[1,15,7,9]这个subproblem的解存在dp[4]里
        dp[i + 1] = maxSum

    return dp[len(arr)]