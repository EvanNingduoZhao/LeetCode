# 这道题中sub problem之间的关系如下
# 对于从text1 的第i个char开始的substirng和从text2的第j个char开始的substring而言，它们两个substirng
# 中longestCommomSubsequence（以下简称LCS）的长度有以下这两种情况：
#  第一种情况：如果text1[i]==text2[j],即这两个substring的开头字母相同的话，那么这个两个subString的LCS的长度等于
#  1+从text1 的第i+1个char开始的substirng和从text2的第j+1个char开始的substring它俩之间的LCS的长度
#  即1+LCS(i+1,j+1),这里LCS是一个求两个string之间的LCS长度的recursive function，它的两个params
# 分别是两个substrings从text1和text2的那个一个char开始

# 第二种情况：如果text1[i]！=text2[j]那么我们继续往下找，这里往下找怎么找，就有两种选择，要么是把i前进一个位置
#  要么是把j前进一个位置，这两种方法哪个能得到的结果更大就取哪个方法的值。因此LCS(i,j)=max(LCS(i+1,j),LCS(i,j+1))
#  实际上两者的common substring的每一个char都是在第一种情况下找到的，第二种情况只是为了寻找第一种情况

# 下面的这个solution就是以上想法的top down recursion实现
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def LCS(i, j):
            if (i, j) not in dp:
                # 这个recursion的base case是如果i或者j中的任何一个指向不存在的char了，
                #  那么就return 0. 比如说text1 和text2各自的最后一个char是相等的
                # 那么LCS(m-1,n-1)=1+LCS(m,n)但是m和n多是指向不存在的char了，因此LCS(m-1,n-1)=1
                # 符合我们想要的
                if i == len(text1) or j == len(text2):
                    dp[(i, j)] = 0
                else:
                    if text1[i] == text2[j]:
                        dp[(i, j)] = 1 + LCS(i + 1, j + 1)
                    else:
                        dp[(i, j)] = max(LCS(i + 1, j), LCS(i, j + 1))
            return dp[(i, j)]

        LCS(0, 0)
        return dp[(0, 0)]

# 想要把一个top down的方法转化成一个bottom up的我们就得找到top down解法里的最小的sub problem在哪
# 答案就是LCS(m-1,n-1)，因此我们如果要iterative bottom up的话得从两个string的末尾开始
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(0, m + 1)] for _ in range(0, n + 1)]
        for j in reversed(range(0, m)):
            for i in reversed(range(0, n)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
