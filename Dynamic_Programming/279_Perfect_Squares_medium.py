#这道题有两种解法
#第一种是DP的解法，第二种是BFS的解法
#先说DP的解法：
#对于每一个n而言，里面完全平方数的数量最少且sum等于n的完全有完全平方数组成的数组的构成一定是，
# 由一个小于n的完全平方数j*j（这里j*j算一个数了）加上里面完全平方数的数量最少且sum等于n-j*j的完全平方数的数组
#这里的j*j不一定是越大越好比如，对于n=12而言，小于12的最大的j*j是9，但是如果要9的话，那么还需要3个1，这一共就要4个
#完全平方数才能构成12了
#真正帮我们找到的12的最优解的完全平方数的组合的是，12减去一个完全平方数j*j（j可以是任何一个小于sqrt(12)的整数）
# 以后剩下的差里面哪个数k对应的完全平方数组合是里用的数是最少的。我们只需要把k的完全平方数组合里的数量+1就是12对应
# 的最优解的完全平方数的组合里面的数的数量了，加的这个1就是j*j
import math
class Solution:
    def numSquares(self, n: int) -> int:
        #dp[i]里存的就是i的最优解完全平方数组合里的完全平方数的数量
        dp=[0]
        #1到i一个一个过
        for i in range(1,n+1):
            nsqrt=math.floor(math.sqrt(i))
            count=float("inf")
            #从1到小于sqrt(n)的每一个整数都作为j试以下，找到最小的那个dp[i-j*j],最后让count等于这个
            #最小的dp[i-j*j]+1
            for j in range(1,nsqrt+1):
                #这里注意一个小trick，当i就本身是一个完全平方数的时候，那么i-j*j就会等于0
                #而我们之前就让dp[0]=0了，因此对于本身就是完全平方数的i而言，最后count=0+1=1
                count=min(count,dp[i-j*j]+1)
            dp.append(count)
        return dp[n]



#下面这个是BFS的方法等复习了BFS在尝试自己写以下

  # Approach two 利用队列和BFS，最先搜索到的结果一定是最短的。 队列中存储（位置,步数） ，效率比较低。
        # q = [[n, 0]]
        # visited = [False for _ in range(n + 1)]
        # visited[n] = True
        # while any(q):
        #     num, step = q.pop(0)   # 出栈，被pop掉的元素将同时返回给两个变量
        #     i = 1
        #     tnum = num - i ** 2
        #     while tnum >= 0:            # 前进一步
        #         if tnum == 0: return step + 1   # 最先到达0的一定是步数最少的
        #         if not visited[tnum]:
        #             q.append((tnum, step + 1))
        #             visited[tnum] = True     # 只添加没有遍历过的节点，减少计算量
        #         i += 1
        #         tnum = num - i ** 2

#这个题还有一个最优解就是用 Lagrange's Four Square theorem
#答案在下面链接的3.mathematical Solution
# https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)