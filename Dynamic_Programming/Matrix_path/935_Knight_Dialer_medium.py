# 这个第一个solution是自己硬想出来的，只针对于这道题，不具有普遍性的一个解法，没必要看了
class Solution:
    def knightDialer(self, n: int) -> int:
        mod=10**9+7
        if n==0:
            return 0
        elif n==1:
            return 10
        elif n==2:
            return 20
        else:
            dp=[(4,4,1),(10,8,2)]
            for i in range(2,n):
                dp.append((2*dp[i-1][1]+2*dp[i-1][2],2*dp[i-1][0],dp[i-2][1]+2*dp[i-2][2]))
            return sum(dp[n-1])%mod
# 关于这道题有一个谷歌面试官写的比较好的一步步从top down recursive到bottom up dp的整个思考过程
# https://alexgolec.dev/google-interview-questions-deconstructed-the-knights-dialer/
# 以下是一个比较按套路的，但是space不是最优的解法
# 首先我们要能够意识到，这道题和62及64题是非常相近的，尤其是跟62。不同点如下：62题问的是固定了起点的终点
# 问你从起点到终点一共有几条不同的路线，没有明确说限制可以走几步，但是实际上因为在长方形的grid里，
# 在不走重复路线，不绕圈子的前提下一定是走(m-1)+(n-1)步，m和n是长方形的长和宽，这一点在62题的第二种用排列组合的解法里
# 我们也已经指出了。而这道题则是不限制起点和终点，从哪里开始在哪里结束都可以，但是限制一共总n步，问一共有多少种路线。
# 实际上最关键的内核，及recurrence relation和62题还是一样的，即走n步到达A点的路线的数量等于走n-1步到达A的所有邻居的位置的和
# 在这道题中邻居指的是从一个位置开始是一步可以走到的8个位置，对于62题而言邻居则是一个位置上边的和左边的两个位置。（当然，在62题
# 中因为我们不走重复的路，所以不用提到几步走到这个问题）

# 下面的solution我们是用的bottom up的iterative的方法来写的
class Solution:
    def knightDialer(self, n: int) -> int:
        dp={}
        # 这是一个knight可以走向的八个位置
        directions=[(-1,2),(-1,-2),(1,2),(1,-2),(-2,1),(-2,-1),(2,1),(2,-1)]
        currN=0
        totalCount=0
        # 因为是高步数走到一个位置的路线数量，是通过低步数走到它的邻居的路线数量之和算出来，所以为了实现bottom up我们
        # 从0步开始，那么从一个位置开始走0步，那就还在原地，因此每个数字都有1种方式可以走0步到达，因此只有1位的电话号码有10个
        while currN<=n-1:
            # 我们过一一遍从1到0的所有数字
            for i in range(0,4):
                for j in range(0,3):
                    # 这里第四行的第一个和第三个是井号键和星号键，我们不管他们
                    if (i,j)==(3,0) or (i,j)==(3,2):
                        continue
                    # 如果是求0步到达一个数字的路线数量，则答案是1
                    if currN==0:
                        dp[(i,j,0)]=1
                    # 如果不是求0步
                    else:
                        count=0
                        # 过一遍八个可以一步到达的邻居中的每一个
                        for d in directions:
                            # 算出邻居的坐标
                            newPos=(i+d[0],j+d[1])
                            # 只要见key pad之内的位置
                            if newPos[0]<0 or newPos[0]>=3 or newPos[1]<0 or newPos[1]>=3:
                                if newPos !=(3,1):
                                    continue
                            # 把n-1步到达邻居的路线数量挨个加在count上
                            count+=dp[(newPos[0],newPos[1],currN-1)]
                        # 存在dp里
                        dp[(i,j,currN)]=count
            # 不要忘了increment要走的步数
            currN+=1
        # 把对于每个位置而言的走n-1步才到达的路线数量加起来
        for i in range(0,4):
            for j in range(0,3):
                if (i,j)==(3,0) or (i,j)==(3,2):
                        continue
                totalCount+=dp[(i,j,n-1)]
        MOD = 10**9 + 7
        return totalCount%MOD

# optimize了DP的memory，上面的解法我们相当于用了一个3D list来存dp，即行坐标，列坐标，步数三个纬度
# 我们实际上可以优化成只用两个2D list来存，因为在计算n步到达一个位置的路线数量时，只会用到n-1步到达其他位置的路线数量，
# 不需要用到被步数的，因此我们就用一个currDP来存n步到达每个位置的路线数量，prevDP来存n-1步到达每个位置的路线数量
# 当步数increment时让prevDP=currDP，currDP重新等于一个空的新list
class Solution:
    def knightDialer(self, n: int) -> int:
        prevDP={}
        currDP={}
        directions=[(-1,2),(-1,-2),(1,2),(1,-2),(-2,1),(-2,-1),(2,1),(2,-1)]
        currN=0
        totalCount=0
        while currN<=n-1:
            currDp={}
            for i in range(0,4):
                for j in range(0,3):
                    if (i,j)==(3,0) or (i,j)==(3,2):
                        continue
                    if currN==0:
                        currDP[(i,j)]=1
                    else:
                        count=0
                        for d in directions:
                            newPos=(i+d[0],j+d[1])
                            if newPos[0]<0 or newPos[0]>=3 or newPos[1]<0 or newPos[1]>=3:
                                if newPos !=(3,1):
                                    continue
                            count+=prevDP[(newPos[0],newPos[1])]
                        currDP[(i,j)]=count
            prevDP=currDP.copy()
            currN+=1
        for i in range(0,4):
            for j in range(0,3):
                if (i,j)==(3,0) or (i,j)==(3,2):
                        continue
                totalCount+=currDP[(i,j)]
        MOD = 10**9 + 7
        return totalCount%MOD