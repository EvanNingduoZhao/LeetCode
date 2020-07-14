# 这是自己写的和答案里的标准DP解法很相近的解法，看下面答案的标准DP解法就够了
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        else:
            pdiff=A[1]-A[0]
            curr_len=2
            res=0
            for i in range(2,len(A)):
                cdiff=A[i]-A[i-1]
                if cdiff==pdiff:
                    curr_len+=1
                    if curr_len>=3:
                        res+=curr_len-2
                else:
                    curr_len=2
                pdiff=cdiff
            return res

# 答案标准DP解法
# 这种问题要规范的按照DP的思路去想，即上一个sub problem的什么性质可以帮助我解决这个sub problem
# 有规范的思路 面试时才想的快
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        #因为Arithmetic slice（AS）至少要有3个element，所以A的长度小于3的话不可能有
        if len(A)<3:
            return 0
        #假设一个等差数列种一共原本有x个arithmetic slices，那么如果在这个等差数列的结尾再加一个符合等差的数
        #那么这个等差数列里airthmetic slices的数量就会再增加x+1个
        #道理是这样的，3，5，7，9里原来有x个AS，现在变成3，5，7，9，11那么增加的AS是5，7，9，11里可以找出来的AS
        #的数量是和3，5，7，9里能找出来的数量是一样的，这是多了x个，除了这x个以外，还有一个3，5，7，9，11本身
        #一共多了x+1个
        else:
            #最开始dp=0，这里dp就是x
            dp=0
            res=0
            for i in range(2,len(A)):
                #如果现在dp是0，即A[i-1]不是一个AS里的，那么这一个if 一下check 3个elements
                #符合if的话，直接就找到了一个AS
                #如果本身A[i-1]就在一个AS里的话，A[i]-A[i-1]的差等于A[i-1]-A[i-2]的差，说明A[i]
                #也可以假如A[i-1]所在的那个等差数列，A[i]加入的话按照上面说的等差数列里的AS数量增加dp+1个
                if A[i]-A[i-1]==A[i-1]-A[i-2]:
                    dp=dp+1
                    res+=dp
                #如果等差数列结束了，那么dp要归零
                else:
                    dp=0
            return res