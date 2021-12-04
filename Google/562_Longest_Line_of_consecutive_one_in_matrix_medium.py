# 假设在input matrix中[i,j]位置的值是1，那么以[i,j]位置作为结尾的最长的horiziontal line的
# 长度等于1+以[i,j-1]为结尾的最长的horiziontal line的长度。用同样的办法我们可以算出结尾在[i,j]
# 的最长的vertical，diagonal，anti-diagonal line的长度。因此比较naitive的办法是用4个2D dp array
# 每个代表一种line，来存memoization info，例如dp[i][j][0]就存着以[i,j]为结尾的最长的horiziontal line的长度
# dp[i][j][1]就存着以[i,j]为结尾的最长的vertical line的长度。但是我们要注意，这里还有一些要处理的corner case，
# 比如当j=0时，[i,j]左边就没有位置了，因此没有[i,j-1]来让你算horiziontal了，当i=0,j=n-1 (n是一个row的长度)时
# 就没有[i-1,j+1]来给你算anti-diagonal（右上到左下）的长度了。为了处理corner case，我们的dp array要在远input matrix的基础上
# 左边右边各加一个column，上面加一个row来作为buffer，这些所有buffer的位置的值都是0
# 从而解决corner case。也就是在input matrix中结尾在[i,j]的某种line的最大长度
# 是存在dp[i+1][j+1]里的。那么上述corner case里的
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[[0, 0, 0, 0] for j in range(n + 2)] for i in range(m + 1)]
        ll = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i + 1][j + 1][0] = dp[i + 1][j][0] + 1
                    dp[i + 1][j + 1][1] = dp[i][j + 1][1] + 1
                    dp[i + 1][j + 1][2] = dp[i][j][2] + 1
                    dp[i + 1][j + 1][3] = dp[i][j + 1 + 1][3] + 1
                    ll = max(ll, max(dp[i + 1][j + 1]))
        return ll
