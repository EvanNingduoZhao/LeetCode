#这个题的最重要的就是edge case们
#这个题的道理是：
#对于121而言它本身有 1 2 1，12 1，1 21这三种decode的方法
#而对于1212，在121后面加了一个2以后，那么在最后一个2单独作为一个字母B时，那么它可以和只有121的时候的三种decode的方法
#分别组合，那么如果最后一个2不是要单独作为一个字母B而是要和它前面那个字母组成一个两位数的话，那么一最后两位12在一起作为
# 一个两位数为前提的decode的方式有n种，这里n等于前两位12可以被decode的方式的数量，因为这里其实就相当于把后两位12
# 代表的第12个字母，加到每种由前两位的12所decode出来的内容后面
# 因此如果加上一个新的digit以后，有三种讨论情况：
# （1）后两位和在一起的两位数是小于等于26的话，那么新加一个digit后的string的decode的
# 方式的数量就等于（假设加完一个digit以后有k个digit）前k-1个digit可decode的方式的数量+前k-2个digit
# 可以decode的方式的数量
# （2）后两位加在一起的两位数大于26，那么后两位就没办法被何在一起看成一个两位数，那么decode这个k个digit的方式的数量
# 就等于decode那前k-1个digits的方式的数量，因为最后一个新加上去的digit只能作为单个的被加在每一种decode前k-1个digit的
# 方式的结果的最后
# （3） 如果新加的digit是0，前面的最后一个digit是1或2，那么就只能最后两个digit组合一个两位数了，不能最后一个作为单独的
#字母加在每种k-1个digit的decode的方式的结果的最后了，因此这种情况下k个digit的decode方式的数量等于前k-2个digit的
#decode的方式的数量

class Solution:
    def numDecodings(self, s: str) -> int:
        # 首先如果input是空的，那么return 0
        if len(s)==0:
            return 0
        # 其次如果input的开头是0的话，那么是不合法的，因为0只有前面是1或者2时才能组成10或者20，
        # 才有对应的字母，单个的0是不合法的
        if s[0]=='0':
            return 0
        # 在唯一一个char不是0的前提下，len是1的input return 1
        if len(s)==1:
            return 1
        # 之后还要针对整个input里有没有不合法的0做一个check
        # 如果有0的前面不是1或者2的话，那么这个input就是不合法的return 0
        for i in range(1,len(s)):
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    continue
                else:
                    return 0
        #dp[i]存的是从开头到第i个digit的这个substring有几种decode的方式
        dp=[0 for _ in range(len(s)+1)]
        #dp[0]=1是一个trick，下面会说
        dp[0]=1
        #dp[1]=1表示1个digit只有一种decode的方法
        dp[1]=1
        #从s的第二个个digit开始traverse到最后一个
        for i in range(1,len(s)):
            #首先dp[i+1]代表的是上面所说的k个digit的可以被decode的方式的数量
            #dp[i]代表的是上面所说的k-1个digit的可以被decode的方式的数量
            #dp[i-1]代表的是上面所说的k-2个digit的可以被decode的方式的数量
            if (s[i-1]=='1'and s[i]!='0') or (s[i-1]=='2' and int(s[i])<=6 and s[i]!='0') :
                #第（1）种情况
                #这里是dp[0]=1的作用了，因为在i=1时，i指的是第二个digit，k=i+1=2
                #那么这里的dp[i]也就是只有第一个digit时decode的方式的数量，即1
                #这里的dp[i-1]也就是有0个digit时decode的方式的数量，这里应该是1
                #因为我们加上dp[i-1]其实是想加上把前两个digit看成一个两位数的情况
                # （i=1时一共也只有两个digit，这两个digit一起看成一个两位数就是1种decode的方式，因此dp[i-1]=1）
                dp[i+1]=dp[i]+dp[i-1]
            else:
                #第（3）种情况
                if s[i]=='0':
                    dp[i+1]=dp[i-1]
                #第（2）种情况
                else:
                    dp[i+1]=dp[i]
        return dp[len(s)]