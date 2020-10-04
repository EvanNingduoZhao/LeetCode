#这道题本质上和第130题差不多，它们都属于是大海里找小岛的变形题，它们共同的特点是：都对和border相连的位置感兴趣，只不过
#130题里相连的条件是自己和邻居都是'O'，而这道题里相连的条件是，地势要逐渐降低，让海水能够流过。
#对于这样对和border相连的位置感兴趣的题目，我们不能像做普通的大海里找小岛的题目那样traverse整个matrix，以每一个没有被
#visited过的，且符合条件的（是陆地的）position都作为dfs的起点。在这种题目中，我们应该以所有在border上的位置为起点，用
#dfs找到并标记出所有和border上的位置相连的为符合条件的位置
#具体到这道题上，我们要把左侧和上方的border跟右侧和下方的border分开来看，跟左侧及上方的border上的位置相连的位置A们，是
#以位置A们为起点，水能流到太平洋里的，跟右侧及下方的border上的位置相连的位置B们，是以位置B们为起点，水能流到大西洋里的
#我们把所有位置A们都存起来，所有位置B们也存起来，最后我们把即在A里也在B里的位置放到result里return
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        def dfs(visited, row, col):
            if (row, col) in visited:
                return
            stack = [(row, col)]
            visited.add((row, col))
            while stack:
                currRow, currCol = stack.pop()
                for d in directions:
                    newRow = currRow + d[0]
                    newCol = currCol + d[1]
                    #出界的邻居不考虑
                    if newRow < 0 or newRow >= m or newCol < 0 or newCol >= n:
                        continue
                    #已经visited过的不考虑，地势比curr位置还低的不考虑
                    #因为这里我们是从海边往内陆反推的，所以地势得越来越高才行
                    if (newRow, newCol) in visited or matrix[newRow][newCol] < matrix[currRow][currCol]:
                        continue
                    #经过两轮筛选以后，能够被加到visited里的位置P就是从P开始水能流到对应的大洋里的位置
                    visited.add((newRow, newCol))
                    stack.append((newRow, newCol))


        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])
        pacific_visited = set()
        atlantic_visited = set()
        result = []
        #以左右两侧的border上的所有位置为起点进行dfs
        for row in range(0, m):
            #这里的dfs helper function不return任何东西
            #只是负责modify 对应的visited set
            dfs(pacific_visited, row, 0)
            dfs(atlantic_visited, row, n - 1)
        #以上下两端的border上的所有位置为起点进行dfs
        for col in range(0, n):
            dfs(pacific_visited, 0, col)
            dfs(atlantic_visited, m - 1, col)
        #最后找出即在位置A们里的也在位置B们里的位置，放到result里return
        for r in range(0, m):
            for c in range(0, n):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])
        return result