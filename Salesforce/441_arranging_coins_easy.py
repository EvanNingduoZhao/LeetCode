# 这道题其实就是要解不等式，假设正确结果是x
# 那么要解的不等式就是(1+x)x/2<=n
# 下面这个方法是直接用解二次方程的公式解的
# 也可用binary search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int) (0.5*(-1+(1+8*n)**0.5))