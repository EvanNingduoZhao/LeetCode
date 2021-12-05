# 这个题是图形类dp里很有意义的题，要好好复习

# 这道题我们首先要想到需要找到一个标准的count squares的方式，有一个方式比较好
# 即对于我们在matrix中traverse到的每一个position，我们都看如果以它为正方形的右下角
# 能形成几个正放心
# 其次，对于一个pos A而言，如果它想成为一个2x2的正方形的右下角的话，那么它上面的邻居
# 左面的邻居和左上角的邻居都必须是1，如果有一个不是都不行，且如果它能够成为一个2x2的正方形
# 的右下角的话，那么以它为右下角可以形成2个正方形，即一个边长为1的一个边长为2的
# 再继续看，如果一个pos A想要成为一个边长为3的正方形的右下角，那么它的上，左及左上三个邻居都
# 必须自身就是一个边长为2的正方形的右下角。同时如果一个posA是一个变成为3的正方形的右下角，
# 那么以它作为右下角的正方形应该也有3个，边长分别为1 2 3
# 因此综上我们可以总结出，一个位置能作为几个正方形的右下角等于它能作为右下角的最大的正方形
# 的边长。我们就把这个值（能作为几个正方形的右下角）作为我们的dp array要track的
# 它和它周边邻居的关系是这样的dp[r][c]=1+min(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])
# class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for r in range(m):
            for c in range(n):
                # 因为matrix的第一个row和第一个col里面的位置最多作为一个
                # 边长是1的正方形的右下角，因此直接把它们在matrix中的值放到dp array里
                if r==0 or c==0:
                    dp[r][c] = matrix[r][c]
                    count+=dp[r][c]
                else:
                    # 必须这个位置自己本身在matrix中的值就是1
                    # 才可能有资格作为一个正方形的右下角
                    if matrix[r][c]==1:
                        dp[r][c] = 1+min(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])
                        count+=dp[r][c]
        return count