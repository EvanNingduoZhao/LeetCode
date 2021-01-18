#这道题是一个tikTok OA里的real programmer game的简化版
#这道题用dp做，那么一个subproblem就是在有d个骰子的情况下，有多少中方式可以扔出和是target
#虽然题目中还有一个量，f即单个骰子的面数，但它实际上是一个常量
#那么解决这道题subproblem还得靠我们解决dp问题的经典手段，即把一个subproblem分解成多个已经解决的subproblems的和
#具体的分解方式如下
#假设我们要求扔五个每个有六个面的骰子，target是18
#那么实际上可以按照最后一个骰子扔出来是几，被分为6种情况
#如果最后一个骰子是1，那么这个问题就相当于剩下四个骰子的和是17
#如果最后一个骰子是2，那么这个问题就相当于剩下四个骰子的和是16
#以此类推
#因此dp[5][18]=dp[4][17]+dp[4][16]+dp[4][15]+dp[4][14]+dp[4][13]+dp[4][12]
#找到了这个关系以后，下面是bottom up的解法
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        #首先如果骰子数和每个骰子的面数之积小于target的话
        #或者target小于骰子数量的话（因为每个骰子最少扔1）
        #都没办法扔出target
        if d*f<target or target<d:
            return 0
        #index 0我们不用
        dp = [[0 for j in range(target+1)] for i in range(d+1)]
        #这里用了dp[0][0]只是因为下面的nested forloop里算dp[1][1]需要用到dp[0][0]
        dp[0][0]=1
        for dice in range(1,d+1):
            #对于每个dice的数量，我们直接以dice为最小值开始increment t，以此避免碰到target小于骰子数量的情况
            for t in range(dice,target+1):
                #如果骰子数和每个骰子的面数之积小于target的话，方法数量直接是0
                if dice*f<t:
                    dp[dice][t]=0
                else:
                    #用一个for loop来把最后一个骰子的值是1到min(f,t)的情况都加上去
                    #注意这里如果t比f小的话到t就行了，否则index就是负数了
                    for k in range(1,min(f,t)+1):
                        dp[dice][t]+=dp[dice-1][t-k]
        return dp[d][target]%1000000007