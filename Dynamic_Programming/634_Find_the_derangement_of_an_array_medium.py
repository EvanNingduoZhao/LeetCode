#这道题是leetcode的会员题，题目如下：

# https://www.cnblogs.com/grandyang/p/7210929.html 题干在这个链接里

# 这道题也是所谓的信件错排问题，即自己用的刷题分类的DP专题的斐波那契数列的第四题
# 假设我们现在要错排[1,2,3,4]，即打乱这四个数，但是要保证4不在第四个，3不在第三个，2不在第二个，1不在第一个
# 我们现在要找dp的recurrance relation,即在我们知道dp[0]（错排1个数）,dp[1]（错排两个数）,dp[2]（错排3个数),的前提下
# 怎么求dp[3](错排四个数)。我们可以把第四个数放到第三个位置（当然也可以放到第一个或者第二个的位置，所以实际上这里我们有
# 4-1=3种选择）[x,x,4,x]现在这个array变成了这样，那么4在第三个位置，根据我们要把3放在哪又回产生两种情况：
# 1). 把3放到第四个位置[x,x,4,3] 这下这个问题剩下的部分就变成了错排1和2两个数即dp[1]的答案
# 2). 不把3放到第四个位置[x,x,4,x(这里不能是3)]，那么这个问题剩下的部分其实就变成了错排1 2 3三个数的一个变形，
# 在orginal的错排1 2 3三个数里3是不能放在第三个位置的，现在这个问题变成了3不能放在第四个位置，1还是不能放在第一个位置
# 2还是不能放在第二个位置，因此虽然3的限制条件改变了，但是排列组合的本质还是一样的。因此符合把4放在第三个位置，
# 且3不能放在第四个位置的错排方式的数量的还是等于dp[3]
# 因此符合把4放在第三个位置上的错排方式的总数就是dp[2]+dp[3],而就像上面所说的，4不一定非要放在第三个位置，也可以放在
# 第一个或者第二个，因此4一共用3个位置可以放，且符合4放在第一个和第二个位置的错排方式的总数也都是dp[2]+dp[3]
# 因此四个数的错排方式一共就有3(dp[2]+dp[3])个。由此我们可以得出n个数的错排方式有(n-1)(dp[n-2]+dp[n-1])个

def num_of_derangement(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        dp=[-1 for _ in range(n)]
        #dp[0]=0代表错排1个数有0种方法
        dp[0]=0
        dp[1]=1
        for i in range(2,n):
            dp[i]=(i-1)*(dp[i-2]+dp[i-1])
        return dp[i]


def num_of_derangement_2(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        #dp[0]=0代表错排1个数有0种方法
        prev2=0
        prev1=1
        for i in range(2,n):
            current=(i-1)*(prev1+prev2)
            prev2=prev1
            prev1=current
        return prev1