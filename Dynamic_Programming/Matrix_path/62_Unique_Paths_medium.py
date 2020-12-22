#这道题和第64题的思路是一样的，先复习64题再来看这道题，实际上这道题应该是比64要简单一些的
# 但是因为64题的笔记已经都写好了，就先去理解64题的思路和64题的3个DP solution在空间复杂度上的层层优化
# 看好了64题以后再来看这道题就非常好理解了

# 这道题有两种解法，第一种是用DP，第二种是用数学的排列组合

#先说第一种DP解法，这里就直接写了一个空间复杂度最优的，只用一个1D list的solution
# 这个solution是模仿64题的空间复杂读最优的，只用一个1D list的解法
# 以下的comment的详细程度是assume自己刚才以及看了64题的解法以后再来看这道题的

#首先要理解的是，对于grid的里的任何一个position A，只能从A上面的那个position B，和A左面的那个position C
#到达A，那么到达A的路径的数量就等于不同的到达B的路径的数量加上不同的到达C的路径的数量

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 0
        #如果这个grid是只有1行或者1列的话，那么从起点到终点只有直线的一个路径
        elif m==1 or n==1:
            return 1
        # 首先要理解，对于top edge即第一行，和left edge即第一列上的每一个position，都只有一种方式到达
        #这里我们采用的是一个col一个col traverse的顺序
        else:
            #这里我们的1D list的size是n-1，这是因为每个col的第一个position都是top edge上的position
            #能reach它们的路径永远都是只有1种，所以就不浪费一个list上的位置去存=它了
            # 先把dp这个list的n-1个位置都填成1，因为第一个col里的所有position，因为在left edge上
            # 都只有一种path去reach
            dp=[1 for _ in range(n-1)]
            #从第二列开始真的traverse
            for col in range(2,m+1):
                #这里的dp[0]存的是每个col的第二个position有几种path去reach 它
                #（因为如上面已经说过的，每个col的第一个位置都只有一种方式到达，都是1，不变的，没必要存）
                dp[0]=1+dp[0]
                #从每个col的第三个位置开始才需用再用一个inner for loop去traverse
                #因此对于n==2的grid 不需要进入这个inner for loop，n==0和n==1的情况在上面已经cover了
                if n>=3:
                    for row in range(3,n+1):
                        #这里的index稍微有些复杂
                        #因为row的value代表的是这个col的第几个位置，如果row=3指的就是第三个位置
                        #但dp[0]对应的是每个col的第二个位置，因此dp[row-2]对应的才是每个col里row
                        #这个iterator index对应的位置
                        # 这里还是64题那个最优空间的思路，在计算新的dp[row-2]应该是多少时
                        # dp[row-2]里存的还是上一个col里的这个位置的path数，即新的这个dp[row-2]对应的位置的左边的位置
                        #的path数，而dp[row-3]是刚才已经update过了的，指的是现在这个col里
                        # 新的这个dp[row-2]对应的位置的上边的位置
                        dp[row-2]=dp[row-3]+dp[row-2]
            # dp[n-2]对应的是每个col的最后一个位置
            return dp[n-2]

#第二种方法，用数学的排列组合：
#在讲这道题之前先复习以下排列组合的知识
#首先 ABCDE五个字母可重复使用，能组合成多少个长度为3的string？ 即"AAA"也算数
# 因为这个string上的3个位置，每个位置都可以放五个字母中的任何一个所以答案是3^5种

#那么不可重复使用的话能组成多少长度为3的string呢？
#那么第一个位置有五种选择，第二个位置不能选第一个位置选过那个了，因此第二个位置只有四种选择
#以此类推第三个位置只有三种，因此一共有5*4*3种string，也就等于5！/2！，即公式N！/（N-k）！
#这里N是可选的字母的数量，k是要组成的string的长度的数量

#以上说的是排列问题，也就是说ACE和ECA和CEA这些都算是不同的，但是从组合的角度讲它们都是有A C和E三个字母组成的，只算1种
#因此如果要算在5个字母里挑3个字母，有多少种组合的话，那就要用总的排列的数量处以每种组合可以产生的不能重复使用的排列的数量
#三个字母的不能重复使用的排列数量是3*2*1即3！，因此5个里面选3个的组合数量就是（5！/（5-3）！）/3！
#等于5！/[(5-3)!*3!] general的公式就是N！/[(N-k)!*k!]

#这道题呢就是一共要向下走n-1次，向右走m-1次，一共走n+m-2次
#那么不同的走法的数量就等于在这n+m-2步里，我们挑哪几步作为往右走的，剩下的自然是往下走的
#也就是从n+m-2里挑m-1有多少种组合
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N=m+n-2
        k=m-1
        #N!/k!(N-k)!
        #nume代表分子
        nume=1
        for i in range(1,N+1):
            nume=nume*i
        #denom代表分母
        denom=1
        for i in range(1,N-k+1):
            denom=denom*i
        for i in range(1,k+1):
            denom=denom*i
        return int(nume/denom)


