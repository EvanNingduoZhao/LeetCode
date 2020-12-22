# 这道题这里一共写了三种写法，主体思路都是一样的，但是每一个都比上一个在空间复杂度上更加的精简了
# 都看一看，可以更好的理解DP题的空间复杂度是怎么一步步优化到最优的，很多时候一次就写出来最优的很难
# 可以先写出来不是最优的，在写的过程中就会更加理解，真的需要存的value都是那些，这样就可以再改进，写出最优的了

# 先说主体思路：对于grid上的每一个位置A而言，都只有两个位置可以走一步就到达A，这两个位置就是A左边的和A上边的两个位置
# （当然这是有例外的第一个row上的位置们就没有上面的，第一个column的位置们就没有左边的，但是特殊情况特殊处理就好了）
# 因此到达每个位置A的最小cost路径的cost都等于min（走到A上面那个位置的cost，走到A左边那个位置的cost）+ A这个位置的cost
# 而我们可以一个row 一个row的traverse这个grid (像第一个solution一样)，也可以一个col一个col的traverse grid（像后两个
# solutions一样）
# 比如说对于：
# [1,3,1]
# [1,5,1]
# [4,2,1]
#这个grid而言，在我traverse了第一个row以后，知道了到达第一个row每个位置的总cost，在traverse第二个row，第二个row的第一个
#位置 1只能从上面的1过来，cost是2，第二个row的第二个5，可以从左边的1过来，也可以从上面的3过来，而且到达这两个位置的的总cost
# 我们都已经知道了，那么我就选更小的那个，即从左边的1过来，这样到达5的cost就是2+5=7。这样一次类推最后就可以得到到达最右下角
# 的位置的最小总cost
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dp={}
        #到达第一个row的第一个位置的cost就等于他自己的value
        dp[(0,0)]=grid[0][0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #第一个row的第一个位置已经看过了，直接continue
                if r==0 and c==0:
                    continue
                #第一个row的位置没有上面的，所以直接cost等于到达自己左边的位置的cost+自己的value
                if r==0:
                    dp[(r,c)]=dp[(r,c-1)]+grid[r][c]
                # 第一个col的位置没有左面的，所以直接cost等于到达自己上边的位置的cost+自己的value
                elif c==0:
                    dp[(r,c)]=dp[(r-1,c)]+grid[r][c]
                # 其他的位置的cost等于min（走到A上面那个位置的cost，走到A左边那个位置的cost）+ A这个位置的cost
                else:
                    dp[(r,c)]=min(dp[(r-1,c)],dp[(r,c-1)])+grid[r][c]
        return dp[(len(grid)-1,len(grid[0])-1)]

# 但从以上的那个solution可以看到我们我们计算到达一个位置的cost，只需要它上面的位置和它左面的位置的cost
# 因此实际上只要始终存着，目前在traverse的那一个row和它上面那个row的每个位置的到达cost就够了
# 不用浪费那么多space去存m*n每个位置的

#下面这个solution是按照一个col一个col traverse的方式来写的，但是本质上和row by row的是一样的
# 这里我们需要始终存着的相对应的就是自己这个col和自己左边的col的每个位置的到达cost

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # prev是目前在traverse的col的左边那个col的每个位置的到达cost
        prev=[-1 for _ in range(len(grid))]
        prev[0]=grid[0][0]
        # curr是目前在traverse的col的每个位置的到达cost
        curr=[-1 for _ in range(len(grid))]
        # 先把第一个col的cost都填到prev里
        for r in range(1,len(grid)):
            prev[r]=prev[r-1]+grid[r][0]
        # 真正的traversal从第二个col开始
        for c in range(1,len(grid[0])):
            #每个col的第一个位置因为是在top edge，即第一个row的，没有上面的位置，所以其到达cost直接等于自己左边
            #那个位置的到达cost+自己的value
            curr[0]=prev[0]+grid[0][c]
            #对于每个col里剩下的位置的cost等于min（走到A上面那个位置的cost，走到A左边那个位置的cost）+ A这个位置的cost
            for r in range(1,len(grid)):
                curr[r]=min(curr[r-1],prev[r])+grid[r][c]
            #每次traverse完一个col以后，现在这个col就变成下一个col的prev了
            prev=curr
        return prev[len(grid)-1]

# 在第二种solution里，我们只有在要用到A位置的左边那个位置的到达cost的时候才会用到prev
# 而curr的每个value在traverse一个新的col的每一个位置是，每到一个新的位置，就更新对应的那个位置的curr的值
# 比如走到一个新的col的第五个位置时，才会更新curr[4](0是第一个位置)，那么在计算curr[4]应该更新成什么的时候
# curr[4]里存的其实还是上一个col的第五个位置的到达cost，而这就真是我们唯一需要prev去知道的地方
# 因此在计算curr[r]时，我们根本不用curr[r]=min(curr[r-1],prev[r])+grid[r][c]
# 用 curr[r]=min(curr[r-1],curr[r])+grid[r][c]就够了，因为curr[r]在被assign新的value之前就等于prev[r]
# 所以我们只用一个curr这个array就够了，用不着prev
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        curr=[-1 for _ in range(len(grid))]
        curr[0] = grid[0][0]
        #把第一个col的cost都填到curr里
        for r in range(1,len(grid)):
            curr[r]=curr[r-1]+grid[r][0]
        ## 真正的traversal从第二个col开始
        for c in range(1,len(grid[0])):
            #每一个col的第一个位置的到达cost实际上就等于上一个col的第一个位置的到达cost
            #加上自己的value，而在给curr[0]assign新的值之前，curr[0]里存的就是上一个col的第一个位置的到达cost
            #因此直接把新一个col的第一个位置的value加到自己身上，就等于新一个col的第一个位置的到达cost了
            curr[0]+=grid[0][c]
            #traverse每个col剩下的位置，道理还是一样
            for r in range(1,len(grid)):
                curr[r]=min(curr[r-1],curr[r])+grid[r][c]
        return curr[len(grid)-1]