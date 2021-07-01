# 这道题是经典背包问题的3d版，经典背包问题是一个2d的table，每一个row代表能在前几个objects里面选择，每一个column代表
# 背包的承重capatity，每个cell里填的value代表目前row和col情况下的能装的最大的总value。而这道题相当于把背包的最大
# 承重量着一个限制条件换成了两个要同时满足的限制条件，即0的总数不多于m，1的总数不多于n，而每个str（即可以往背包里装的物品）
# 的所谓重量也就是这个str里1和0的数量。现在我们要work with的是一个3d的dp table，m和n作为两个限制性的纬度组成一个plane，
# 而原本2d dp table中的row对应的能从前几个strs中做选择，现在变成了3d table的height
# 为了优化空间，我们实际上不需要一个3d table，因为填充第i层时，只需要看i-1层，因此我们一共有两层就够了


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(0,m+1)] for _ in range(0,n+1)]
        strsLen = len(strs)
        # 先记录第一个str里有多少个1和0，km是有多少个0，kn是有多少个1
        km = 0
        kn = 0
        for char in strs[0]:
            if char == '0':
                km+=1
            else:
                kn+=1
        # 对于第一层而言，对于一个cell而言，如果它对应的m大于等于km，n大于等于kn，那么就说明
        # 在只用第一个string的情况下，对于m和n而言，可以得到一个有1个str的subset（这个str就是第一个str自己）
        # 因此在这些cell里填上1
        for i in range(0, n+1):
            for j in range(0, m+1):
                if kn<=i and km<=j:
                    dp[i][j] = 1
        # 之后从第二层正式开始
        for k in range(1, strsLen):
            km = 0
            kn = 0
            for char in strs[k]:
                if char == '0':
                    km+=1
                else:
                    kn+=1
            # 我们填cell时用temp，填完之后让dp等于temp，到了填再下一层时再建新的空白的temp
            temp = [[0 for _ in range(0,m+1)] for _ in range(0,n+1)]
            for i in range(0,n+1):
                for j in range(0,m+1):
                    # 如果光是这一层对应的那个str里的km和kn就大于m和n了，那那就更别说还要和前面的str组成subset了
                    # 直接让这个cell的值等于它上一层同一个位置的那个cell的值
                    if kn>i or km>j:
                        temp[i][j] = dp[i][j]
                    # 如果km和kn都小于等于m和n的话，如果把这层对应的str选进subset，那么我们的subset的size就会变成
                    # dp[i-kn][j-km]+1，如果不加它进去，size则是dp[i][j]，哪个大我们就选哪个
                    else:
                        temp[i][j] = max(dp[i-kn][j-km]+1, dp[i][j])
            dp = temp
        return dp[n][m]