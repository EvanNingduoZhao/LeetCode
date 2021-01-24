# 这道题就是256题的第二部分，这部分的和256的区别在于不只是三个颜色了，而是一共有k个可选的颜色
# 要求solution的time是n*K，要求space是constant
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or len(costs) == 0 or len(costs[0]) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        # 为了让space是constant我们不能用array来存上一个house paint成每种颜色，且之前的所有house都配合
        # 的min cost了。我们这里用三个variable来存min cost，min cost对应的color，以及第二小的cost
        # 之所以要存第二小的cost是因为，如果下一个house我们想paint的颜色和这个house的min cost的color重了
        # 那我们就不得不只能采用这个house的第二小的cost了，注意第二小的cost的color是什么不用存，因为用不上
        prev_min_cost = float('inf')
        prev_second_min_cost = None
        prev_min_color = None
        # 先过一遍第一个house paint成各种颜色所需的cost，得出对于第一个house的
        # min_cost, min cost的color和第二小的cost
        for color in range(0, k):
            if costs[0][color] < prev_min_cost:
                prev_second_min_cost = prev_min_cost
                prev_min_cost = costs[0][color]
                prev_min_color = color
            # 这里要多check一步目前所在这个color的cost是否小于第二小的cost
            # 该更新要更新
            elif costs[0][color] < prev_second_min_cost:
                prev_second_min_cost = costs[0][color]
        # 下面开始一个house一个house的过
        for i in range(1, n):
            # 对于每个house我们都要维持对于这个house的min cost，min cost color和第二小的cost
            curr_min_cost = float('inf')
            curr_min_color = None
            curr_second_min_cost = None
            for j in range(0, k):
                # 如果上一个house的min cost的color和我们目前想要给这个house paint的color重了
                # 那么我们只能给上一个house paint它的第二小cost的color，之后在前面的house配合
                if prev_min_color == j:
                    currColorCost = costs[i][j] + prev_second_min_cost
                # 如果没重，直接paint min cost color，前面的house都配合
                else:
                    currColorCost = costs[i][j] + prev_min_cost
                # 注意更新目前house的min cost，min cost color以及第二小cost
                if currColorCost < curr_min_cost:
                    curr_second_min_cost = curr_min_cost
                    curr_min_cost = currColorCost
                    curr_min_color = j
                elif currColorCost < curr_second_min_cost:
                    curr_second_min_cost = currColorCost
            # 当前house的所有color都过完了以后，用当前house的三个值去更新prev_min_cost,prev_min_color和
            # prev_second_min_cost
            prev_min_cost = curr_min_cost
            prev_min_color = curr_min_color
            prev_second_min_cost = curr_second_min_cost

        return prev_min_cost