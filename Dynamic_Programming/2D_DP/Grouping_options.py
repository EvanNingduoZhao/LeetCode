# 题目
# There are nn people in a row. They must all be divided into mm contiguous groups from left to right.
# If each group must be at least as large as the group to its left, determine how many distinct ways
# groups can be formed. For a group to be distinct, it must differ in size for at least one group
# when sorted ascending. For example, [1, 1, 1, 3] is distinct from [1, 1, 1, 2] but not from [1, 3, 1, 1].
# Example：
# Input:
# 8
# 4
# Output: 5
# Explanation: [1, 1, 1, 5], [1, 1, 2, 4], [1, 1, 3, 3], [1, 2, 2, 3], [2, 2, 2, 2]

# 这道题要使用2D的list来作为dp list

# 思路是dp[i][j]可以分为2部分: 第1个数是1的和第1个数不是1的。
# 比如说n=8, m=4，那第1个数是1的情况就包括{1,1,1,5}, {1,1,2,4},{1,1,3,3},{1,2,2,3}，第1个数不是1的情况就是{2,2,2,2}。
# 那实际上
# 1）第1个数是1的情况就等价于dp[7][3]，即dp[i-1][j-1]，即把第1个数拿掉后的情况，{1,1,5}, {1,2,4}, {1,3,3}, {2,2,3}。
# 2）第1个数不是1的情况就是将8分为4个数，但第1个数不是1的情况。等价于dp[4][4]，即dp[i-j][j]，即因为每个元素都>1，所以每个元素减去1，然后求dp[4][4]即可。
# 怎么理解呢？比如说第2种情况是{2,3,4,5}，n=14，那么，我们可以给4个数每个数先分配一个1，剩下10在4个数里面分配，这就是dp[10][4]。

def grouping_options(n,m):
    #如果要分的组数比人数还多那是分不出来的
    if m>n:
        return 0
    # initialize一个n*m的2D list，里面所有的value的初始值都是0
    dp=[[0 for j in range(m+1)]for i in range(n+1)]
    # base case 就是dp[1][0],dp[1][1]这些值，所有带0的值都该是0，以及initialize好了
    # 所有i和j相等的都是1，我们用下面这个for loop给它们都赋上值
    for i in range(m+1):
        dp[i][i]=1
    for i in range(2,n+1):
        for j in range(1,min(i+1,m+1)):
            dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
            print(i,j,dp[i][j])
    return dp[n][m]

print(grouping_options(8,4))