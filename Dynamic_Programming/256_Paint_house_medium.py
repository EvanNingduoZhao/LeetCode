# 下面是自己想出来的space不optimize的解法，dp是一个list of tuples
# dp里的第n个tuple的三个elements里分别存的是把第n个房子paint成红 蓝 绿三种颜色，
# 并且第n个房子前的所有房子都在配合第n个房子的颜色的前提下，最少要花多少cost
# 这里subproblem之间的关系就是，把n个house刷成红色且前面的n-1个house也配合这个颜色的min cost
# 等于把第n个house刷成红色的cost+min（把第n-1个房子刷成绿色且前n-2个房子都配合的最小总cost，
# 把第n-1个房子刷成蓝色且前n-2个房子都配合的最小总cost）
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or len(costs)==0:
            return 0
        dp=[costs[0]]
        n=len(costs)
        # 这样我们就从头到位travese所有的house之后按照上面说的subproblem之间的关系来计算就好了
        for i in range(1,n):
            redCost=costs[i][0]+min(dp[i-1][1],dp[i-1][2])
            blueCost=costs[i][1]+min(dp[i-1][0],dp[i-1][2])
            greenCost=costs[i][2]+min(dp[i-1][0],dp[i-1][1])
            dp.append((redCost,blueCost,greenCost))
        return min(dp[n-1])

# 但是上面的这个方法的space是O(n)，但是实际上我们只需要存目前这个house的tuple的三种颜色对应的
# 总cost及上一个house的三种颜色对应的总cost就好了，这样space可以被优化成O(1)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or len(costs) == 0:
            return 0
        # 这里我们只用prevHouseCost这个3个elements的list 来存将上一个house paint成
        # 某个颜色，且上一个house之前的所有house也配合这个颜色所需的最小总cost
        prevHouseCost = costs[0][:]
        n = len(costs)
        for i in range(1, n):
            redCost = costs[i][0] + min(prevHouseCost[1], prevHouseCost[2])
            blueCost = costs[i][1] + min(prevHouseCost[0], prevHouseCost[2])
            greenCost = costs[i][2] + min(prevHouseCost[0], prevHouseCost[1])
            # 算完新的house paint三种颜色且之前的house也都配合的最小cost以后
            # 把prevHouseCost更新成新的house的cost，之后开始计算下一个house的cost
            prevHouseCost = [redCost, blueCost, greenCost]
        # 最后，最后一个house paint成三种颜色且之前所有的house都配合的cost就会被存在
        # prevHouseCost里，return最小值即可
        return min(prevHouseCost)
