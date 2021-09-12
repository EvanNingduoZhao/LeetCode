# 题目很简单，就是先sort一下horizontalCuts和verticalCuts
# traverse两者，分别找到horizontalCuts之间最大的空隙和verticalCuts之间最大的空隙
# 两者乘积就是要return的结果 注意要mod
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxHeight=max(horizontalCuts[0],h-horizontalCuts[-1])
        maxWidth=max(verticalCuts[0],w-verticalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            height = horizontalCuts[i]-horizontalCuts[i-1]
            maxHeight=max(maxHeight,height)
        for j in range(1, len(verticalCuts)):
            width = verticalCuts[j]-verticalCuts[j-1]
            maxWidth=max(maxWidth,width)
        return (maxHeight*maxWidth)%(10**9+7)