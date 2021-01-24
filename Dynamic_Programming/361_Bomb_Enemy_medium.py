# 我们一个row一个row的traverse这个grid，对于一个position A，只有它是每个row的第一个position
# 或者它是一堵墙右边的第一个position，我们才会以它为起点，向右继续traverse，直到碰到一堵墙
# 或者到达这个row的结尾位置，在traverse的过程中，记录下遇到了多少个敌人，将rowHits更新成
# 遇到的敌人的数量。这样对于在同一个row上position A右边的positions们，只要它们不是本row的第一个
# 或者一堵墙的紧右边那一个，它在这个row上能炸死的就还是刚才得出的rowHits。所以对于它们来说
# 我们不用触发重新traverse一次这个row的操作。但是如果position B是A同一个row上A右边的某一个
# 位置，且B左边就是一堵墙。那么我们在A时触发的那个row traversal里记录的敌人的数量跟B是没关系的
# 因为B处引爆的炸弹有B左边的墙当着，炸不死墙左边那些row taversal里记录的敌人。因此对于B，我们
# 要将rowHits清零并触发一个新的row traversal，这个row traversal从B开始，
# 不断向右，直到撞到一堵新的墙，或者到达本row的终点，同样记录遇到敌人的数量

# 我们对于一个position的row要这样记录rowHits，对于col也一样要记录colHits
# 但是因为我们是一个row 一个row traverse的，一个row的rowHits对于这个row的positions
# 用完就没用了，所以rowHits是一个普通的variable就可以了。但是对于cols的记录，我们在
# A row的这个位置用了这个colHits，等下到B row的同一位置还得用，因此我们得时刻给每一个col
# 都存一个colHits，因此colHits得是一个list

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        rowHits = 0
        colHits = [0 for _ in range(0, m)]
        maxHits = 0

        for r in range(0, n):
            for c in range(0, m):
                # 不能只对是empty的cell才触发，因为如果那样的话
                # 假设一个敌人是在row的开始或者一个墙的紧右边
                # 那它就触发不了traversal了，这个敌人就永远都没有机会被计算进去
                if c == 0 or grid[r][c - 1] == 'W':
                    rowHits = 0
                    for col in range(c, m):
                        if grid[r][col] == 'E':
                            rowHits += 1
                        elif grid[r][col] == 'W':
                            break
                if r == 0 or grid[r - 1][c] == 'W':
                    colHits[c] = 0
                    for row in range(r, n):
                        if grid[row][c] == 'E':
                            colHits[c] += 1
                        elif grid[row][c] == 'W':
                            break
                # 我们在这里看一个位置是不是empty，如果是，给它计算一个totalHits
                # 之后和目前最大的比较一下，有需要就update
                if grid[r][c] == '0':
                    maxHits = max(maxHits, rowHits + colHits[c])
        return maxHits