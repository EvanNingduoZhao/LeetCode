# 这道题难度比较大，是一个嵌套的DP，解决整个问题用的是一个大DP，之后在populate这个大DP
# 的过程中，为了解决小问题，还得在用一个小dp（运用left和right）
# 这道题想解释明白要写很多字，下面是一个人已经写好的配图的讲解，之后就自己看一下这个讲解吧
# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/C%2B%2BJavaPython-3-DP-Explanation-with-pictures.
# 这道题很有意义，要看一看
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        def fillLeft(pointsRow, left):
            left[0] = pointsRow[0]
            for i in range(1, n):
                left[i] = max(left[i - 1] - 1, pointsRow[i])

        def fillRight(pointsRow, right):
            right[-1] = pointsRow[-1]
            for i in range(n - 2, -1, -1):
                right[i] = max(right[i + 1] - 1, pointsRow[i])

        pre = points[0]
        for i in range(m - 1):
            left = [0 for _ in range(n)]
            right = [0 for _ in range(n)]
            fillLeft(pre, left)
            fillRight(pre, right)
            curr = [0 for _ in range(n)]
            for j in range(n):
                curr[j] = points[i + 1][j] + max(right[j], left[j])
            pre = curr[:]
        return max(pre)