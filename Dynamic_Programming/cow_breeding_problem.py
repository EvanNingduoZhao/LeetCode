# 题目描述：假设农场中成熟的母牛每年都会生 1 头小母牛，并且永远不会死。第一年有 1 只小母牛，从第二年开始，
# 母牛开始生小母牛。每只小母牛 3 年之后成熟又可以生小母牛。给定整数 N，求 N 年后牛的数量。

# 每年的牛的数量等于，前一年牛的数量加上三年前母牛的数量（因为三年前的成熟的三年后还在生，三年前刚出生的，到今年第一次生）
# 所以今年新出生的母牛的数量就应该等于三年前的母牛的数量（因为每头母牛一年生一头母牛）
# 因此dp[i]=dp[i-1]+dp[i-3]
# 如果给这道题加一个限制条件，母牛的寿命只有十年（假设第十年还会生，生完当年就死了）
# 那么每年母牛的数量就要减去十年前出生的母牛的数量，也就是十三年前的母牛的数量
# dp[i]=dp[i-1]+dp[i-3]-dp[i-13] (for i>=13)

# 以下的代码是加了牛的寿命只有10年这个限制条件，且第一头小母牛第一年两岁的code

def cow_breeding(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        dp=[-1 for _ in range(n)]
        #第一年是的index是1,因为第二年第一头牛才生了一头小牛，那说明第一年时第一头牛两岁
        #那也就是说第一头时在第-1年出生的
        dp[-1]=1
        dp[0]=1
        dp[1]=1
        dp[2]=2
        dp[3]=3
        #从第4年到第8年，这是时候没有牛死
        for i in range[4,n+1]:
            dp[i]=dp[i-1]+dp[i-3]
            #第9年的时候第一头牛10岁了,第一头牛死掉了，但是因为当年它十岁的这年它也生了小牛，所以依旧符合上面的公式
            # 只是要在第九年把牛的总数减1，即减掉死去的它自己
            if i==9:
                dp[i]-=1
            #第12年时第二年出生的牛死了，第二年出生的牛的数量等于第-1年牛的数量，即1头
            #因此从第12年开始每年死掉的牛的数量等于第i-13年的牛的数量
            if i>=12:
                dp[i]=dp[i-1]+dp[i-3]-dp[i-13]
        return dp[n]